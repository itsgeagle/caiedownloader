# CAIE Downloader
# Made by @itsgeagle on GitHub
# A simple Python GUI-based utility tool to allow users to download and compile CAIE past papers.
# Enter subject code, year range, and paper, and a PDF will be generated.

# Imports
import requests
from modules.file_handler import download_paper, compile_pdf, clear_temp_files
from modules.version_checker import compare_version
from modules.popup_handler import version_popup, error_popup
from modules.gui import *

VERSION = 'v0.2.0-beta'


def validate_input():
    try:
        requests.get("https://google.com", timeout=5)
    except requests.ConnectionError:
        error_popup("You are not connected to the internet!")
        return False
    if not subject_var.get().isnumeric():
        error_popup("The subject code must be a number! Try again.")
        return False
    if not len(subject_var.get()) == 4:
        error_popup("The subject code must be a 4-digit number! Try again.")
        return False
    if not paper_var.get().isnumeric():
        error_popup("The paper code must be a number! Try again.")
        return False
    if not len(paper_var.get()) == 1:
        error_popup("The paper code must be a 1-digit number! Try again.")
        return False
    if not start_year.get().isnumeric():
        error_popup("The start year must be a number! Try again.")
        return False
    if not (len(start_year.get()) == 4 or len(start_year.get()) == 2):
        error_popup("The start year must be a 4-digit or 2-digit number! Try again.")
        return False
    if not end_year.get().isnumeric():
        error_popup("The end year must be a number! Try again.")
        return False
    if not (len(end_year.get()) == 4 or len(end_year.get()) == 2):
        error_popup("The end year must be a 4-digit or 2-digit number! Try again.")
        return False
    if not int(end_year.get()) >= int(start_year.get()):
        error_popup("The end year must be greater or equal to the start year! Try again.")
        return False
    if feb_march.get() == 'N' and may_june.get() == 'N' and may_june.get() == 'N':
        error_popup("You must select at least one exam series! Try again.")
        return False
    return True


# Main method for the program
def main():
    if validate_input():
        clear_temp_files()
        subCode = subject_var.get()
        paperCode = paper_var.get()
        start = int(start_year.get()) if len(start_year.get()) == 2 else int(start_year.get()[-2:])
        end = int(end_year.get()) if len(end_year.get()) == 2 else int(end_year.get()[-2:])
        print(f'Attempting to fetch all paper {paperCode}s for the subject code {subCode} '
              f'for the years 20{start}-{end}')
        for year in range(start, end + 1):
            if feb_march.get() == 'Y':
                download_paper(subCode, paperCode, year, '2', 'm')
            if may_june.get() == 'Y':
                download_paper(subCode, paperCode, year, '1', 's')
                download_paper(subCode, paperCode, year, '2', 's')
                download_paper(subCode, paperCode, year, '3', 's')
            if may_june.get() == 'Y':
                download_paper(subCode, paperCode, year, '1', 'w')
                download_paper(subCode, paperCode, year, '2', 'w')
                download_paper(subCode, paperCode, year, '3', 'w')

        if not compile_pdf(subCode, paperCode, str(start), str(end)):
            error_popup("Your query did not end up downloading any valid files. Please try again.")
        else:
            error_popup("Done processing your request!")


sub_btn = Button(root, text='Submit', pady=10, command=main)
sub_btn.pack(side=BOTTOM)

version_status = compare_version(VERSION)
if not version_status[0]:
    print(version_status[2])
    if version_status[1]:
        version_popup(version_status[1])
    else:
        error_popup(version_status[2])

root.mainloop()
