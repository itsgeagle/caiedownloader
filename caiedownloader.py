# CAIE Downloader
# Author: @itsgeagle
# A simple Python GUI-based utility tool to allow users to download and compile CAIE past papers.
# Enter subject code, year range, and paper, and a PDF will be generated.

# Imports
from modules.file_handler import download_paper, compile_pdf, clear_temp_files
from modules.gui import *
from modules.popup_handler import version_popup, message_popup, edit_config
from modules.verification_handler import compare_version, validate_input
from modules.config_handler import init_config

VERSION = 'v1.3.0'


# Main method for the program
def main():
    if validate_input():
        clear_temp_files()
        subCode = subject_var.get()
        paperCode = paper_var.get()
        start = int(start_year.get()) if len(start_year.get()) == 2 else int(start_year.get()[-2:])
        end = int(end_year.get()) if len(end_year.get()) == 2 else int(end_year.get()[-2:])
        paperType = paper_type.get()
        paperType = 'qp' if paperType == 'Question Papers' else 'ms'
        fm = feb_march.get()
        mj = may_june.get()
        on = oct_nov.get()
        remove_blanks = True if remove_blank.get() == 'Y' else False
        remove_additionals = True if remove_additional.get() == 'Y' else False
        remove_formulae = True if remove_formula.get() == 'Y' else False
        for this_code in paperCode.split(","):
            this_code = this_code.strip(" ")
            print(f'Attempting to fetch all {paperType} with code {this_code}s for the subject code {subCode} '
                  f'for the years 20{start}-{end}')
            for year in range(start, end + 1):
                if fm == 'Y' and year > 15:
                    download_paper(subCode, this_code, year, '2', 'm', paperType)
                if mj == 'Y':
                    download_paper(subCode, this_code, year, '1', 's', paperType)
                    download_paper(subCode, this_code, year, '2', 's', paperType)
                    download_paper(subCode, this_code, year, '3', 's', paperType)
                if on == 'Y':
                    download_paper(subCode, this_code, year, '1', 'w', paperType)
                    download_paper(subCode, this_code, year, '2', 'w', paperType)
                    download_paper(subCode, this_code, year, '3', 'w', paperType)
        if not compile_pdf(subCode=subCode, paperCode=paperCode, start=str(start), end=str(end), delete_blanks=remove_blanks, delete_additional=remove_additionals, delete_formulae=remove_formulae):
            message_popup("Your query did not end up downloading any valid files. Please try again.", "Error")
        else:
            message_popup("Done processing your request!", "Success")

Button(root, text='Edit Config', command=edit_config).pack(side=BOTTOM, pady=10)

sub_btn = Button(root, text='Submit', command=main)
sub_btn.pack(side=BOTTOM, pady=10)


version_status = compare_version(VERSION)
if not version_status[0]:
    print(version_status[2])
    if version_status[1]:
        version_popup(version_status[1])
    else:
        message_popup(version_status[2], "Error")

init_config()

root.mainloop()
