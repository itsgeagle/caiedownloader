# Contains all the file handling methods, such as downloading and compiling PDFs
import os

import fitz
import requests

from modules.dictionaries import IGCSE, ALevel, OLevel
from modules.popup_handler import browse_directory, browse_path, message_popup

HOMEPATH = os.path.expanduser("~")
TEMPPATH = os.path.join(HOMEPATH, ".caiedownloadertemp")

# Function to download the paper which matches the entered type
def download_paper(subCode, paperCode, year, variant, series, paperType):
    if not os.path.exists(TEMPPATH):
        create_temp_path()

    filename = f'{subCode}_{series}{year}_{paperType}_{paperCode}{variant}.pdf'

    if subCode in IGCSE:
        url = f'https://papers.gceguide.com/Cambridge%20IGCSE/{IGCSE.get(subCode)}20{year}/{filename}'
    elif subCode in ALevel:
        url = f'https://papers.gceguide.com/A%20Levels/{ALevel.get(subCode)}20{year}/{filename}'
    else:
        url = f'https://papers.gceguide.com/O%20Levels/{OLevel.get(subCode)}20{year}/{filename}'

    print(f'Downloading {filename} from {url}')
    try:
        paper = requests.get(url)
        if paper.status_code != 404:
            path = os.path.join(TEMPPATH, filename)
            with open(path, 'wb') as f:
                f.write(paper.content)
        else:
            print(f"Failed to download {filename} - 404 error, paper was not found.")
    except requests.exceptions.RequestException as e:
        print(e)

def transfer_papers_from_temp():
    files = os.listdir(TEMPPATH)
    path_to_save = ''

    while path_to_save == '':
        path_to_save = browse_directory()

        if path_to_save == '':
            message_popup("Please select a path to save the files to!", "Error")

    for filename in files:
        if filename == '.gitignore':
            continue
        try:
            os.rename(
                os.path.join(TEMPPATH, filename),
                os.path.join(path_to_save, filename)
            )

        except FileExistsError:
            message_popup(f"File {filename} already exists in the destination folder. Please remove it and try again.", "Error")
            continue

# Function to take all the PDFs currently in the /temp/ folder and compile them into a single PDF
def compile_pdf(subCode, paperCode, start, end, delete_blanks):
    defaultName = f'{subCode} Paper {paperCode} 20{start}-{end}.pdf'
    compiled = browse_path(defaultName)
    while compiled == '':
        message_popup("Please select a path to save the file to!", "Error")
        compiled = browse_path(defaultName)

    print(f"Attempting to save compiled PDF to {compiled}")

    files = os.listdir(TEMPPATH)
    files.remove('.gitignore')
    files = sorted(files)
    outFile = fitz.open(HOMEPATH + "/assets/blank.pdf")

    status = False
    for filename in files:
        print(f'Compiling {filename}')
        try:
            f = fitz.open(os.path.join(TEMPPATH, filename))
        except fitz.FileDataError:
            print(f"Failed to compile {filename}")
        else:
            status = True
            outFile.insert_file(f)
            f.close()

    pages_to_remove = [0]

    if delete_blanks:
        for page in outFile:
            word_list = page.get_text("words", delimiters=None)
            for i in range(0, len(word_list) - 2):
                if word_list[i][4] == "BLANK" and word_list[i+1][4] == "PAGE":
                    print(f'Removing page {page.number} (BLANK PAGE)')
                    pages_to_remove.append(page.number)
                    break
                if word_list[i][4] == "Additional" and word_list[i+1][4] == "Page":
                    print(f'Removing page {page.number} (ADDITIONAL PAGE)')
                    pages_to_remove.append(page.number)
                    break

    if status:
        outFile.delete_pages(pages_to_remove)
        outFile.save(compiled)
    return status


# Function to clear the /temp/ folder at the beginning of each program run
def clear_temp_files():
    try:
        files = os.listdir(TEMPPATH)
        files.remove('.gitignore')
        for filename in files:
            os.remove(os.path.join(TEMPPATH, filename))
    except Exception as e:
        pass

# Create the temp path if it does not exist
def create_temp_path():
    try:
        os.mkdir(TEMPPATH)
    except Exception as e:
        print(e)
