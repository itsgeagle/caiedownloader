# CAIE Downloader
# Author: @itsgeagle
# A simple Python GUI-based utility tool to allow users to download and compile CAIE past papers.
# Enter subject code, year range, and paper, and a PDF will be generated.

import threading

from modules.file_handler import download_paper, compile_pdf, clear_temp_files
from modules.gui import *
from modules.popup_handler import version_popup, message_popup, edit_config, browse_path
from modules.verification_handler import compare_version, validate_input
from modules.config_handler import init_config

VERSION = 'v1.3.1'


def _run_download(subCode, paperCode, start, end, paperType, fm, mj, on,
                  remove_blanks, remove_additionals, remove_formulae, save_path, on_progress):
    for this_code in paperCode.split(","):
        this_code = this_code.strip(" ")
        print(f'Attempting to fetch all {paperType} with code {this_code}s '
              f'for subject {subCode} for years 20{start}-{end}')
        for year in range(start, end + 1):
            if fm == 'Y' and year > 15:
                download_paper(subCode, this_code, year, '2', 'm', paperType)
                on_progress()
            if mj == 'Y':
                download_paper(subCode, this_code, year, '1', 's', paperType)
                on_progress()
                download_paper(subCode, this_code, year, '2', 's', paperType)
                on_progress()
                download_paper(subCode, this_code, year, '3', 's', paperType)
                on_progress()
            if on == 'Y':
                download_paper(subCode, this_code, year, '1', 'w', paperType)
                on_progress()
                download_paper(subCode, this_code, year, '2', 'w', paperType)
                on_progress()
                download_paper(subCode, this_code, year, '3', 'w', paperType)
                on_progress()

    success = compile_pdf(subCode=subCode, paperCode=paperCode,
                          start=str(start), end=str(end),
                          delete_blanks=remove_blanks,
                          delete_additional=remove_additionals,
                          delete_formulae=remove_formulae,
                          output_path=save_path)

    def _finish():
        sub_btn.configure(state='normal', text='Download  ▶')
        status_label.configure(text='')
        progress_var.set(0)
        if success:
            message_popup("Done! Your PDF has been saved.", "Success")
        else:
            message_popup("Your query did not download any valid files. Please try again.", "Error")

    root.after(0, _finish)


def main():
    if not validate_input():
        return

    subCode   = subject_var.get()
    paperCode = paper_var.get()
    start     = int(start_year.get()) if len(start_year.get()) == 2 else int(start_year.get()[-2:])
    end       = int(end_year.get())   if len(end_year.get())   == 2 else int(end_year.get()[-2:])
    paperType = 'qp' if paper_type.get() == 'Question Papers' else 'ms'
    fm = feb_march.get()
    mj = may_june.get()
    on = oct_nov.get()
    remove_blanks      = remove_blank.get()      == 'Y'
    remove_additionals = remove_additional.get() == 'Y'
    remove_formulae    = remove_formula.get()    == 'Y'

    default_name = f'{subCode} Paper {paperCode} 20{start}-20{end}.pdf'
    save_path = browse_path(default_name)
    if not save_path:
        return

    clear_temp_files()

    total_steps = sum(
        (1 if fm == 'Y' and year > 15 else 0) +
        (3 if mj == 'Y' else 0) +
        (3 if on == 'Y' else 0)
        for _ in paperCode.split(",")
        for year in range(start, end + 1)
    )

    progress_var.set(0)
    progress_bar.configure(maximum=total_steps)
    status_label.configure(text=f'0 / {total_steps} attempted')
    sub_btn.configure(state='disabled', text='Downloading...')

    step = [0]

    def on_progress():
        step[0] += 1
        s, t = step[0], total_steps
        root.after(0, lambda: progress_var.set(s))
        root.after(0, lambda: status_label.configure(text=f'{s} / {t} attempted'))

    threading.Thread(
        target=_run_download,
        args=(subCode, paperCode, start, end, paperType, fm, mj, on,
              remove_blanks, remove_additionals, remove_formulae, save_path, on_progress),
        daemon=True,
    ).start()


config_btn.configure(command=edit_config)
sub_btn.configure(command=main)

version_status = compare_version(VERSION)
if not version_status[0]:
    print(version_status[2])
    if version_status[1]:
        version_popup(version_status[1])
    else:
        message_popup(version_status[2], "Error")

init_config()

root.mainloop()
