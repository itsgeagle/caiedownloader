# CAIE Downloader
# Author: @itsgeagle
# A simple Python GUI-based utility tool to allow users to download and compile CAIE past papers.
# Enter subject code, year range, and paper, and a PDF will be generated.

# Imports
from modules.file_handler import download_paper, compile_pdf, clear_temp_files
from modules.verification_handler import compare_version, validate_input
from modules.popup_handler import version_popup, message_popup
from modules.gui import *

VERSION = 'v0.2.0-beta'


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
            message_popup("Your query did not end up downloading any valid files. Please try again.", "Error")
        else:
            message_popup("Done processing your request!", "Success")


sub_btn = Button(root, text='Submit', pady=10, command=main)
sub_btn.pack(side=BOTTOM)

version_status = compare_version(VERSION)
if not version_status[0]:
    print(version_status[2])
    if version_status[1]:
        version_popup(version_status[1])
    else:
        message_popup(version_status[2])

root.mainloop()
