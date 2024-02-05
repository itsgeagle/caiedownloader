# CAIE Downloader
# Made by @itsgeagle on GitHub
# A simple Python GUI-based utility tool to allow users to download and compile CAIE past papers.
# Enter subject code, year range, and paper, and a PDF will be generated.

# Imports
import requests
from modules.FileHandler import downloadPaper, compileTemp, clearTemp
from modules.VersionChecker import compare_version
from modules.PopupMessage import versionPopup
from modules.GUI import *

VERSION = 'v0.1.2-beta'


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


# Main method for the program
def main():
    if validateInput():
        clearTemp()
        subCode = subjectVar.get()
        paperCode = paperVar.get()
        start = int(startYear.get()) if len(startYear.get()) == 2 else int(startYear.get()[-2:])
        end = int(endYear.get()) if len(endYear.get()) == 2 else int(endYear.get()[-2:])
        successStatus.set(f'Attempting to fetch all paper {paperCode}s for the subject code {subCode} '
                          f'for the years 20{start}-{end}')
        for year in range(start, end + 1):
            if year >= 15:
                downloadPaper(subCode, paperCode, year, '2', 'm')
            downloadPaper(subCode, paperCode, year, '1', 's')
            downloadPaper(subCode, paperCode, year, '2', 's')
            downloadPaper(subCode, paperCode, year, '3', 's')
            downloadPaper(subCode, paperCode, year, '1', 'w')
            downloadPaper(subCode, paperCode, year, '2', 'w')
            downloadPaper(subCode, paperCode, year, '3', 'w')

        compileTemp(subCode, paperCode, str(start), str(end))

        successStatus.set("Done processing your request!")


sub_btn = Button(root, text='Submit', pady=10, command=main)
sub_btn.pack(side=BOTTOM)

versionStatus = compare_version(VERSION)
if not versionStatus[0]:
    versionPopup(versionStatus[1])

root.mainloop()
