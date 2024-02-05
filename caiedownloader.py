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
    if not subjectVar.get().isnumeric():
        error_popup("The subject code must be a number! Try again.")
        return False
    if not len(subjectVar.get()) == 4:
        error_popup("The subject code must be a 4-digit number! Try again.")
        return False
    if not paperVar.get().isnumeric():
        error_popup("The paper code must be a number! Try again.")
        return False
    if not len(paperVar.get()) == 1:
        error_popup("The paper code must be a 1-digit number! Try again.")
        return False
    if not startYear.get().isnumeric():
        error_popup("The start year must be a number! Try again.")
        return False
    if not (len(startYear.get()) == 4 or len(startYear.get()) == 2):
        error_popup("The start year must be a 4-digit or 2-digit number! Try again.")
        return False
    if not endYear.get().isnumeric():
        error_popup("The end year must be a number! Try again.")
        return False
    if not (len(endYear.get()) == 4 or len(endYear.get()) == 2):
        error_popup("The end year must be a 4-digit or 2-digit number! Try again.")
        return False
    if not int(endYear.get()) >= int(startYear.get()):
        error_popup("The end year must be greater or equal to the start year! Try again.")
        return False
    return True


# Main method for the program
def main():
    if validate_input():
        clear_temp_files()
        subCode = subjectVar.get()
        paperCode = paperVar.get()
        start = int(startYear.get()) if len(startYear.get()) == 2 else int(startYear.get()[-2:])
        end = int(endYear.get()) if len(endYear.get()) == 2 else int(endYear.get()[-2:])
        success_status.set(f'Attempting to fetch all paper {paperCode}s for the subject code {subCode} '
                           f'for the years 20{start}-{end}')
        for year in range(start, end + 1):
            if year >= 15:
                download_paper(subCode, paperCode, year, '2', 'm')
            download_paper(subCode, paperCode, year, '1', 's')
            download_paper(subCode, paperCode, year, '2', 's')
            download_paper(subCode, paperCode, year, '3', 's')
            download_paper(subCode, paperCode, year, '1', 'w')
            download_paper(subCode, paperCode, year, '2', 'w')
            download_paper(subCode, paperCode, year, '3', 'w')

        compile_pdf(subCode, paperCode, str(start), str(end))

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
