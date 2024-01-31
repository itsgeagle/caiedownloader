# CAIE Downloader
# Made by @thegeagle on GitHub
# A simple Python GUI-based utility tool to allow users to download and compile CAIE past papers.
# Enter subject code, year range, and paper, and a PDF will be generated.

# Imports
import tkinter
from tkinter import *
import requests
import os
import fitz
import shutil

# Initialize GUI window
window = Tk()
window.title("CAIE Downloader by Geagle")
window.geometry("500x500")

# Initialize StringVars
subjectVar = tkinter.StringVar()
paperVar = tkinter.StringVar()
startYear = tkinter.StringVar()
endYear = tkinter.StringVar()
successStatus = tkinter.StringVar()


def validateInput():
    try:
        requests.get("https://google.com", timeout=5)
    except requests.ConnectionError:
        successStatus.set("You are not connected to the internet!")
        return False
    if not subjectVar.get().isnumeric():
        successStatus.set("The subject code must be a number! Try again.")
        return False
    if not len(subjectVar.get()) == 4:
        successStatus.set("The subject code must be a 4-digit number! Try again.")
        return False
    if not paperVar.get().isnumeric():
        successStatus.set("The paper code must be a number! Try again.")
        return False
    if not len(paperVar.get()) == 1:
        successStatus.set("The paper code must be a 1-digit number! Try again.")
        return False
    if not startYear.get().isnumeric():
        successStatus.set("The start year must be a number! Try again.")
        return False
    if not (len(startYear.get()) == 4 or len(startYear.get()) == 2):
        successStatus.set("The start year must be a 4-digit or 2-digit number! Try again.")
        return False
    if not endYear.get().isnumeric():
        successStatus.set("The end year must be a number! Try again.")
        return False
    if not (len(endYear.get()) == 4 or len(endYear.get()) == 2):
        successStatus.set("The end year must be a 4-digit or 2-digit number! Try again.")
        return False
    if not int(endYear.get()) >= int(startYear.get()):
        successStatus.set("The end year must be greater or equal to the start year! Try again.")
        return False
    return True


# Method to download each paper
def downloadPaper(subCode, paperCode, year, variant, series):
    files = os.listdir(os.path.dirname(__file__) + "/temp/")
    files.remove('.gitignore')
    for filename in files:
        os.remove(os.path.join(os.path.dirname(__file__) + "/temp/" + filename))
    filename = f'{subCode}_{series}{year}_qp_{paperCode}{variant}.pdf'
    print(f'Downloading {filename}')
    url = f'https://dynamicpapers.com/wp-content/uploads/2015/09/{filename}'
    try:
        paper = requests.get(url)
        path = os.path.dirname(__file__) + f'/temp/{filename}'
        with open(path, 'wb') as f:
            f.write(paper.content)
    except requests.exceptions.RequestException as e:
        print(e)


def compileTemp(subCode, paperCode, start, end):
    compiled = os.path.dirname(__file__) + f'/outfiles/{subCode} Paper {paperCode}s 20{start}-{end}.pdf'
    outFile = fitz.open(os.path.dirname(__file__) + "/assets/blank.pdf")

    files = os.listdir(os.path.dirname(__file__) + "/temp/")
    files.remove('.gitignore')
    for filename in files:
        print(filename)
        f = fitz.open(os.path.join(os.path.dirname(__file__) + "/temp/" + filename))
        outFile.insert_file(f)
        os.remove(os.path.join(os.path.dirname(__file__) + "/temp/" + filename))

    outFile.delete_page(0)
    outFile.save(compiled)


# Main method for the program
def main():
    if validateInput():
        subCode = subjectVar.get()
        paperCode = paperVar.get()
        start = int(startYear.get()) if len(startYear.get()) == 2 else int(startYear.get()[-2:])
        end = int(endYear.get()) if len(endYear.get()) == 2 else int(endYear.get()[-2:])
        successStatus.set(f'Attempting to fetch all paper {paperCode}s for the subject code {subCode} '
                          f'for the years 20{start}-{end}')
        for year in range(start, end + 1):
            if year >= 15 and not subCode == '9608' and not subCode == '9618':
                downloadPaper(subCode, paperCode, year, '2', 'm')
            downloadPaper(subCode, paperCode, year, '1', 's')
            downloadPaper(subCode, paperCode, year, '2', 's')
            downloadPaper(subCode, paperCode, year, '3', 's')
            downloadPaper(subCode, paperCode, year, '1', 'w')
            downloadPaper(subCode, paperCode, year, '2', 'w')
            downloadPaper(subCode, paperCode, year, '3', 'w')

        compileTemp(subCode, paperCode, str(start), str(end))

        successStatus.set("Done processing your request!")


# GUI
title_label = Label(window, text="CAIE Downloader", font=('Montserrat', 25))
title_label.pack()

subject_label = Label(window, text="\nSubject code to download (for example, 9701)", font=('Montserrat', 16))
subject_label.pack()
subject_input = Entry(window, textvariable=subjectVar, font=('Montserrat', 16))
subject_input.pack()

paper_label = Label(window, text="\nPaper code to download (for example, 2)", font=('Montserrat', 16))
paper_label.pack()
paper_input = Entry(window, textvariable=paperVar, font=('Montserrat', 16))
paper_input.pack()

start_year_label = Label(window, text="\nYear to start downloading from (for example, 2022 or 22)",
                         font=('Montserrat', 16))
start_year_label.pack()
start_year_input = Entry(window, textvariable=startYear, font=('Montserrat', 16))
start_year_input.pack()

end_year_label = Label(window, text="\nYear to end downloading from (for example, 2022 or 22)", font=('Montserrat', 16))
end_year_label.pack()
end_year_input = Entry(window, textvariable=endYear, font=('Montserrat', 16))
end_year_input.pack()

success_label = Label(window, textvariable=successStatus, font=('Montserrat', 20))
success_label.pack(side=BOTTOM)
sub_btn = Button(window, text='Submit', pady=10, command=main)
sub_btn.pack(side=BOTTOM)

window.mainloop()
