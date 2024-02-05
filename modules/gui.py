from tkinter import *

# Initialize GUI window
root = Tk()
root.title("CAIE Downloader by Geagle")
root.geometry("1000x1000")

# Initialize StringVars
subjectVar = StringVar()
paperVar = StringVar()
startYear = StringVar()
endYear = StringVar()
success_status = StringVar()

# GUI
title_label = Label(root, text="CAIE Downloader", font=('Montserrat', 25))
title_label.pack()

subject_label = Label(root, text="\nSubject code to download (for example, 9701)", font=('Montserrat', 16))
subject_label.pack()
subject_input = Entry(root, textvariable=subjectVar, font=('Montserrat', 16))
subject_input.pack()

paper_label = Label(root, text="\nPaper code to download (for example, 2)", font=('Montserrat', 16))
paper_label.pack()
paper_input = Entry(root, textvariable=paperVar, font=('Montserrat', 16))
paper_input.pack()

start_year_label = Label(root, text="\nYear to start downloading from (for example, 2022 or 22)",
                         font=('Montserrat', 16))
start_year_label.pack()
start_year_input = Entry(root, textvariable=startYear, font=('Montserrat', 16))
start_year_input.pack()

end_year_label = Label(root, text="\nYear to end downloading from (for example, 2022 or 22)", font=('Montserrat', 16))
end_year_label.pack()
end_year_input = Entry(root, textvariable=endYear, font=('Montserrat', 16))
end_year_input.pack()

success_label = Label(root, textvariable=success_status, font=('Montserrat', 20))
success_label.pack(side=BOTTOM)
