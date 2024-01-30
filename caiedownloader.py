# CAIE Downloader
# Made by @thegeagle on GitHub
# A simple Python GUI-based utility tool to allow users to download and compile CAIE past papers.
# Enter subject code, year range, and paper, and a PDF will be generated.
import tkinter
# Imports
from tkinter import *

# Initialize GUI window
window = Tk()
window.title("CAIE Downloader by Geagle")
window.geometry("500x450")

# Initialize StringVars
subjectVar = tkinter.StringVar()
paperVar = tkinter.StringVar()
startYear = tkinter.StringVar()
endYear = tkinter.StringVar()
successStatus = tkinter.StringVar()

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

start_year_label = Label(window, text="\nYear to start downloading from", font=('Montserrat', 16))
start_year_label.pack()
start_year_input = Entry(window, textvariable=startYear, font=('Montserrat', 16))
start_year_input.pack()

end_year_label = Label(window, text="\nYear to end downloading from", font=('Montserrat', 16))
end_year_label.pack()
end_year_input = Entry(window, textvariable=endYear, font=('Montserrat', 16))
end_year_input.pack()

success_label = Label(window, textvariable=successStatus, font=('Montserrat', 20))
success_label.pack(side=BOTTOM)
sub_btn = Button(window, text='Submit', pady=10)
sub_btn.pack(side=BOTTOM)

window.mainloop()
