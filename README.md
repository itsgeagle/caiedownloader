# CAIE Downloader

## A simple Python-based utility tool which can be used to download CAIE (IGCSE, AS and A Level) past papers and compile them into a single PDF.

This project provides a simple GUI-based utility tool which allows students of the CAIE high school curriculum (IGCSEs, O Levels, AS and A Levels) to download past papers and compile them into a single PDF file, which can then be printed, solved on a tablet, or used in any other way. The tool allows you to customize:

* The **subject code** being downloaded (_e.g. 9701_)
* The **paper code** being downloaded (_e.g. 1_)
* The **years** for which papers are to be downloaded (_e.g. 2020-23_)

When run, the program produces a simple, elegant and intuitive GUI window, where you can enter the details of what you would like to download. The file will automatically be created and output to the `/outfiles/` directory of your project folder.

<img width="568" alt="GUI preview" src="https://github.com/itsgeagle/caiedownloader/assets/119720547/6f674480-e673-4528-9fdc-440314b9c38c">

## Installation

First, clone the repository:
```
git clone https://github.com/itsgeagle/caiedownloader.git
```

Navigate into the repository folder you just created:
```
cd ./caiedownloader/
```

Install dependencies using the pip process manager:
```
python3 -m pip install -r requirements.txt
```

And that's it! Hopefully, if everything went right, you should be ready to use the CAIE Downloader!
To use the application, simply run the `caiedownloader.py` file.

## Housekeeping

CAIE Downloader uses [Dynamic Papers](https://dynamicpapers.com/) to fetch and download papers. This is because of the convenient manner in which Dynamic Papers stores past papers. Unfortunately, this also means that the usage of this application is limited to a specific list of subjects:

  - IGCSEs:
    - Accounting
    - Agriculture
    - Arabic
    - Art and Design
    - Biology
    - Business
    - Chemistry
    - Combined Science
    - Computer Science
    - Economics
    - English - First Language
    - English as a Second Language
    - English Literature
    - Environmental Management
      
  - O Levels:
    - Accounting
    - Additional Mathematics
    - Arabic
    - Biology
    - Business
    - Chemistry
    - Computer Science
    - Computer Studies
    - D-Maths
    - Economics
    - English
    - English Literature
    - French
    - German
    - Islamiyat
    - Physics
    - Sociology
    - Travel and Tourism

  - AS and A Levels:
    - Accounting
    - Arabic
    - Biology
    - Business
    - Chemistry
    - Computer Science
    - Economics
    - History
    - Information Technology
    - Literature in English
    - Maths
    - Physics
    - Psychology
    - Sociology

I am planning to hopefully migrate to a broader paper source, but that will likely not be any time soon. 

In the case of any bugs or issues, feel free to report them here on GitHub. Alternatively, for any questions, bug reports, issues, and so on, you can find me over on Discord (@thegeagle).
