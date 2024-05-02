# Contains the primary GUI elements
from tkinter import *
from modules.config_handler import fetch_from_config

# Initialize GUI window
root = Tk()
root.title("CAIE Downloader by Geagle")

menuOptions = ["Question Papers", "Mark Schemes"]

# Initialize StringVars
subject_var = StringVar()
paper_var = StringVar()
start_year = StringVar()
end_year = StringVar()
feb_march = StringVar()
feb_march.set('N')
may_june = StringVar()
may_june.set('N')
oct_nov = StringVar()
oct_nov.set('N')
paper_type = StringVar()
paper_type.set("Question Papers")
remove_blank = StringVar()
remove_additional = StringVar()
remove_formula = StringVar()

def refresh_config_data():
    remove_blank.set(fetch_from_config("remove_blank"))
    remove_additional.set(fetch_from_config("remove_additional"))
    remove_formula.set(fetch_from_config("remove_formula"))

refresh_config_data()

# GUI
title_label = Label(root, text="CAIE Downloader", font=('Montserrat', 25))
title_label.pack()

subject_label = Label(root, text="\nSubject code to download (for example - 9701)", font=('Montserrat', 16))
subject_label.pack()
subject_input = Entry(root, textvariable=subject_var, font=('Montserrat', 16))
subject_input.pack()

paper_label = Label(root, text="\nPaper code(s) to download (for example - 2 or 1,2,4)", font=('Montserrat', 16))
paper_label.pack()
paper_input = Entry(root, textvariable=paper_var, font=('Montserrat', 16))
paper_input.pack()

start_year_label = Label(root, text="\nYear to start downloading from (for example - 2022 or 22)",
                         font=('Montserrat', 16))
start_year_label.pack()
start_year_input = Entry(root, textvariable=start_year, font=('Montserrat', 16))
start_year_input.pack()

end_year_label = Label(root, text="\nYear to end downloading from (for example - 2022 or 22)", font=('Montserrat', 16))
end_year_label.pack()
end_year_input = Entry(root, textvariable=end_year, font=('Montserrat', 16))
end_year_input.pack()

select_type = OptionMenu(root, paper_type, *menuOptions)
select_type.pack(pady=10)

series_label = Label(root, text="\nExam series to download", font=('Montserrat', 16))
Checkbutton(root, text='Feb/March', variable=feb_march, onvalue='Y', offvalue='N').pack(pady=5)
Checkbutton(root, text='May/June', variable=may_june, onvalue='Y', offvalue='N').pack(pady=5)
Checkbutton(root, text='Oct/Nov', variable=oct_nov, onvalue='Y', offvalue='N').pack(pady=5)
Checkbutton(root, text='Remove Blank Pages', variable=remove_blank, onvalue='Y', offvalue='N').pack(pady=10)
Checkbutton(root, text='Remove Additional Pages', variable=remove_additional, onvalue='Y', offvalue='N').pack(pady=5)
Checkbutton(root, text='Remove Formula Pages', variable=remove_formula, onvalue='Y', offvalue='N').pack(pady=5)

