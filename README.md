# CAIE Downloader

## A simple Python-based utility tool which can be used to download CAIE (IGCSE, AS and A Level) past papers and compile them into a single PDF.

This project provides a simple GUI-based utility tool which allows students of the CAIE high school curriculum (IGCSEs, O Levels, AS and A Levels) to download past papers and compile them into a single PDF file, which can then be printed, solved on a tablet, or used in any other way. The tool allows you to customize:

* The **subject code** being downloaded (_e.g. 9701_)
* The **paper code** being downloaded (_e.g. 1_)
* The **years** for which papers are to be downloaded (_e.g. 2020-23_)

When run, the program produces a simple, elegant and intuitive GUI window, where you can enter the details of what you would like to download. The file will automatically be created and output to the `/outfiles/` directory of your project folder.

<img width="568" alt="GUI preview" src="https://github.com/itsgeagle/caiedownloader/assets/119720547/6f674480-e673-4528-9fdc-440314b9c38c">

## Installation


### MacOS/Linux


Open Terminal by going into `Finder -> Applications -> Utilities -> Terminal` (MacOS) or by using the `CTRL + ALT + T` shortcut (Linux).

Ensure you have python installed by running:

```
python3 --version
```

If you have Python installed, this should return your local Python version. If not, you can download and install Python [here.](https://www.python.org/downloads/)

Navigate to the directory where you wish to store the files by either:
- Using the `cd /path/to/folder/` command in terminal, where `/path/to/folder` is the path to the directory.
- On MacOS, navigating to the directory in Finder, then right-clicking the folder and selecting the 'New Terminal at Folder' option under 'Services'.

First, either clone the repository using the following command or download the [latest program release](https://github.com/itsgeagle/caiedownloader/releases/latest/):
```
git clone https://github.com/itsgeagle/caiedownloader.git
```

Navigate into the repository folder you just created:
```
cd ./caiedownloader/
```
Note that depending on how you downloaded the files, the folder may be named `caiedownloader-beta` or  `caiedownloader-main`, in which case you should change the command above to be appropriate.

Install dependencies using the pip process manager:
```
python3 -m pip install -r requirements.txt
```

And that's it! Hopefully, if everything went right, you should be ready to use the CAIE Downloader!

To use the application, simply run the `caiedownloader.py` file using the following command:

```
python3 caiedownloader.py
```


### Windows

Open the Command Prompt by entering the Start Menu and entering `cmd`.

Ensure you have python installed by running:

```
python3 --version
```

If you have Python installed, this should return your local Python version. If you do not have Python installed, please install the latest Python version from the Microsoft Store.

Navigate to the directory where you wish to store the files by either:
- Using the `cd C:\path\to\folder\` command in Command Prompt, where `C:\path\to\folder\` is the path to the directory.
- Navigating to the directory in File Explorer, then right-clicking the folder and selecting the 'Open in Terminal' option.

First, either clone the repository using the following command or download the [latest program release](https://github.com/itsgeagle/caiedownloader/releases/latest/):
```
git clone https://github.com/itsgeagle/caiedownloader.git
```

Navigate into the repository folder you just created:
```
cd .\caiedownloader\
```
Note that depending on how you downloaded the files, the folder may be named `caiedownloader-beta` or  `caiedownloader-main`, in which case you should change the command above to be appropriate.

Install dependencies using the pip process manager:
```
python3 -m pip install -r requirements.txt
```

And that's it! Hopefully, if everything went right, you should be ready to use the CAIE Downloader!

To use the application, simply run the `caiedownloader.py` file using the following command:

```
python3 caiedownloader.py
```

## Supported Subjects

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
