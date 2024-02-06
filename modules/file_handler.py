# Contains all the file handling methods, such as downloading and compiling PDFs
import os
import requests
import fitz
from modules.dictionaries import IGCSE, ALevel, OLevel


HOMEPATH = os.path.dirname(__file__)[:-8]
TEMPPATH = HOMEPATH + "/temp/"


# Function to download the paper which matches the entered type
def download_paper(subCode, paperCode, year, variant, series):
    filename = f'{subCode}_{series}{year}_qp_{paperCode}{variant}.pdf'
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
            path = TEMPPATH + filename
            with open(path, 'wb') as f:
                f.write(paper.content)
        else:
            print(f"Failed to download {filename} - 404 error, paper was not found.")
    except requests.exceptions.RequestException as e:
        print(e)


# Function to take all the PDFs currently in the /temp/ folder and compile them into a single PDF
def compile_pdf(subCode, paperCode, start, end):
    compiled = HOMEPATH + f'/outfiles/{subCode} Paper {paperCode}s 20{start}-{end}.pdf'
    outFile = fitz.open(HOMEPATH + "/assets/blank.pdf")

    files = os.listdir(TEMPPATH)
    files.remove('.gitignore')

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

    if status:
        outFile.delete_page(0)
        outFile.save(compiled)
    return status


# Function to clear the /temp/ folder at the beginning of each program run
def clear_temp_files():
    files = os.listdir(TEMPPATH)
    files.remove('.gitignore')
    for filename in files:
        os.remove(TEMPPATH + filename)
