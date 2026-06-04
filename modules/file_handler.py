# Contains all the file handling methods, such as downloading and compiling PDFs
import os

import fitz
import requests

from modules.dictionaries import IGCSE, ALevel, OLevel
from modules.popup_handler import browse_path, message_popup

HOMEPATH = os.path.join(os.path.expanduser("~"), ".caiedownloader")
TEMPPATH = os.path.join(HOMEPATH, "temp")

TIMEOUT = 20
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/pdf,*/*',
}

_BEH_LEVELS = {
    'igcse': 'cambridge-igcse',
    'igcse91': 'cambridge-igcse-9-1',
    'alevel': 'cambridge-international-a-level',
    'olevel': 'cambridge-o-level',
}


def _is_valid_pdf(content):
    return content[:4] == b'%PDF'


def _try_download(url, filename):
    try:
        paper = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if paper.status_code == 200 and _is_valid_pdf(paper.content):
            print(f'Downloading {filename} from {url}')
            path = os.path.join(TEMPPATH, filename)
            with open(path, 'wb') as f:
                f.write(paper.content)
            return True
        elif paper.status_code == 404:
            print(f'Not found at {url}')
        else:
            print(f'Status {paper.status_code} from {url}')
    except requests.exceptions.Timeout:
        print(f'Timed out connecting to {url}')
    except requests.exceptions.RequestException as e:
        print(f'Request error for {url}: {e}')
    return False


def _bestexamhelp_url(subCode, year, filename):
    if subCode in IGCSE:
        raw = IGCSE[subCode]
        level = _BEH_LEVELS['igcse91'] if '(9-1)' in raw else _BEH_LEVELS['igcse']
    elif subCode in ALevel:
        level = _BEH_LEVELS['alevel']
        raw = ALevel[subCode]
    elif subCode in OLevel:
        level = _BEH_LEVELS['olevel']
        raw = OLevel[subCode]
    else:
        return None
    slug = raw.rstrip('/').replace('(9-1)', '').replace('&', 'and').replace('(', '').replace(')', '').replace('--', '-').strip('-')
    return f'https://bestexamhelp.com/exam/{level}/{slug}/20{year:02d}/{filename}'


# Function to download the paper which matches the entered type
def download_paper(subCode, paperCode, year, variant, series, paperType):
    filename = f'{subCode}_{series}{year}_{paperType}_{paperCode}{variant}.pdf'

    dp_url = f'https://dynamicpapers.com/wp-content/uploads/2015/09/{filename}'
    if _try_download(dp_url, filename):
        return

    print(f'Not found on Dynamic Papers - trying Best Exam Help.')
    beh_url = _bestexamhelp_url(subCode, year, filename)
    if beh_url and _try_download(beh_url, filename):
        return

    print(f'Failed to download {filename} - not found on any source.')


# Function to take all the PDFs currently in the /temp/ folder and compile them into a single PDF
def compile_pdf(subCode, paperCode, start, end, delete_blanks, delete_additional, delete_formulae, output_path=None):
    compiled = output_path
    if not compiled:
        defaultName = f'{subCode} Paper {paperCode} 20{start}-{end}.pdf'
        compiled = browse_path(defaultName)
        while compiled == '':
            message_popup("Please select a path to save the file to!", "Error")
            compiled = browse_path(defaultName)

    print(f"Attempting to save compiled PDF to {compiled}")

    files = sorted(os.listdir(TEMPPATH))
    outFile = fitz.open()

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

    pages_to_remove = []

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
                if 'Mathematical Formulae' in word_list or 'Formula List' in word_list:
                    print(f'Deleting mathematical formulae: page {page.number + 1}')
                    pages_to_remove.append(page.number)

    if status:
        outFile.delete_pages(pages_to_remove)
        outFile.save(compiled)
    return status


# Function to clear the /temp/ folder at the beginning of each program run
def clear_temp_files():
    if os.path.exists(TEMPPATH):
        files = os.listdir(TEMPPATH)
        for filename in files:
            os.remove(os.path.join(TEMPPATH, filename))
    else:
        os.makedirs(TEMPPATH)
