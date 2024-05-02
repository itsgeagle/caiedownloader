# Contains all the file handling methods, such as downloading and compiling PDFs
import os

import fitz
import requests

from modules.dictionaries import IGCSE, ALevel, OLevel
from modules.popup_handler import browse_path, message_popup

HOMEPATH = os.path.dirname(__file__)[:-8]
TEMPPATH = HOMEPATH + "/temp/"


# Function to download the paper which matches the entered type
def download_paper(subCode, paperCode, year, variant, series, paperType):
    filename = f'{subCode}_{series}{year}_{paperType}_{paperCode}{variant}.pdf'
    if subCode in IGCSE:
        url = f'https://papers.gceguide.net/Cambridge%20IGCSE/{IGCSE.get(subCode)}20{year}/{filename}'
    elif subCode in ALevel:
        url = f'https://papers.gceguide.net/A%20Levels/{ALevel.get(subCode)}20{year}/{filename}'
    else:
        url = f'https://papers.gceguide.net/O%20Levels/{OLevel.get(subCode)}20{year}/{filename}'

    try:
        paper = requests.get(url)
        if paper.status_code != 404:
            print(f'Downloading {filename} from {url}')
            path = TEMPPATH + filename
            with open(path, 'wb') as f:
                f.write(paper.content)
        else:
            print("File not found on GCE Guide - attempting to download from Dynamic Papers.")
            url = f'https://dynamicpapers.com/wp-content/uploads/2015/09/{filename}'
            paper = requests.get(url)
            if paper.status_code != 404:
                print(f'Downloading {filename} from {url}')
                path = TEMPPATH + filename
                with open(path, 'wb') as f:
                    f.write(paper.content)
            else:
                print("File not found on Dynamic Papers - attempting to download from Papa Cambridge.")
                url = f'https://pastpapers.papacambridge.com/directories/CAIE/CAIE-pastpapers/upload/{filename}'
                paper = requests.get(url)
                if paper.status_code != 404:
                    print(f'Downloading {filename} from {url}')
                    path = TEMPPATH + filename
                    with open(path, 'wb') as f:
                        f.write(paper.content)
                else:
                    print(f"Failed to download {filename} - 404 error, paper was not found.")
    except requests.exceptions.RequestException as e:
        print(e)


# Function to take all the PDFs currently in the /temp/ folder and compile them into a single PDF
def compile_pdf(subCode, paperCode, start, end, delete_blanks, delete_additional, delete_formulae):
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
            f = fitz.open(TEMPPATH + filename)
        except fitz.FileDataError:
            print(f"Failed to compile {filename}")
        else:
            status = True
            outFile.insert_file(f)
            f.close()

    pages_to_remove = [0]

    if delete_blanks or delete_additional or delete_formulae:
        for page in outFile:
            word_list : str = page.get_text("text", delimiters=None)
            if delete_blanks:
                if 'BLANK PAGE' in word_list:
                    print(f"Deleting blank page: page {page.number + 1}")
                    pages_to_remove.append(page.number)
            if delete_additional:
                if 'Additional Page' in word_list:
                    print(f"Deleting additional page: page {page.number + 1}")
                    pages_to_remove.append(page.number)
            if delete_formulae:
                if 'The Periodic Table of Elements' in word_list:
                    print(f"Deleting periodic table of elements: page {page.number + 1}")
                    pages_to_remove.append(page.number)
                if 'Important values, constants and standards' in word_list and not 'Important values, constants and standards are printed in the question paper.' in word_list:
                    print(f"Deleting important values, constants and standards: page {page.number + 1}")
                    pages_to_remove.append(page.number)
                if 'Stefan–Boltzmann constant' in word_list:
                    print(f'Deleting data and constants: page {page.number + 1}')
                    pages_to_remove.append(page.number)
                if 'Mathematical Formulae' in word_list:
                    print(f'Deleting mathematical formulae: page {page.number + 1}')
                    pages_to_remove.append(page.number)


    if status:
        outFile.delete_pages(pages_to_remove)
        outFile.save(compiled)
    return status


# Function to clear the /temp/ folder at the beginning of each program run
def clear_temp_files():
    files = os.listdir(TEMPPATH)
    files.remove('.gitignore')
    for filename in files:
        os.remove(TEMPPATH + filename)
