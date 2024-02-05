# Contains all the file handling methods for the CAIE Downloader, such as downloading and compiling PDFs

import os
import requests
import fitz

TEMPPATH = os.path.dirname(__file__)[:-8] + "/temp/"


# Function to download the paper which matches the entered type
def downloadPaper(subCode, paperCode, year, variant, series):
    filename = f'{subCode}_{series}{year}_qp_{paperCode}{variant}.pdf'
    url = f'https://dynamicpapers.com/wp-content/uploads/2015/09/{filename}'
    try:
        print(f'Downloading {filename}')
        paper = requests.get(url)
        path = TEMPPATH + filename
        with open(path, 'wb') as f:
            f.write(paper.content)
    except requests.exceptions.RequestException as e:
        print(e)


# Function to take all the PDFs currently in the /temp/ folder and compile them into a single PDF
def compileTemp(subCode, paperCode, start, end):
    compiled = os.path.dirname(__file__) + f'/outfiles/{subCode} Paper {paperCode}s 20{start}-{end}.pdf'
    outFile = fitz.open(os.path.dirname(__file__) + "/assets/blank.pdf")

    files = os.listdir(TEMPPATH)
    files.remove('.gitignore')
    for filename in files:
        print(f'Compiling {filename}')
        try:
            f = fitz.open(TEMPPATH + filename)
        except fitz.FileDataError:
            print(f"Failed to compile {filename}")
        else:
            outFile.insert_file(f)
            f.close()

    outFile.delete_page(0)
    outFile.save(compiled)


# Function to clear the /temp/ folder at the beginning of each program run
def clearTemp():
    files = os.listdir(TEMPPATH)
    files.remove('.gitignore')
    for filename in files:
        os.remove(TEMPPATH + filename)
