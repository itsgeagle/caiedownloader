# Functions to deal with validating and verifying content, input, and program version
# Author: @itsgeagle
import requests

from modules.dictionaries import IGCSE, ALevel, OLevel
from modules.gui import *
from modules.popup_handler import message_popup


#  Compare the current version with the latest version
def compare_version(current_version):
    repo = "itsgeagle/caiedownloader"
    url = f"https://api.github.com/repos/{repo}/releases"

    try:
        response = requests.get(url)
    except requests.RequestException:
        return False, None, "Unable to connect to the internet! Please check your internet connection and then re-run " \
                            "the program! "
    else:
        if response.status_code == 200:
            releases = response.json()
            if releases:
                latest_version = releases[0]["tag_name"]
                if latest_version != current_version:
                    return False, latest_version, f'Installation is outdated! A new version ({latest_version}) ' \
                                                  f'has been released! Get it here - ' \
                                                  f'https://github.com/itsgeagle/caiedownloader/releases/ '
                return True, None
            else:
                return False, None, "No releases were found. How did you even get the program?"
        else:
            return False, None, "Failed to fetch version. You can continue to use the program, but it is recommended " \
                                "to " \
                                "check GitHub for newer versions here - https://github.com/itsgeagle/caiedownloader/" \
                                "releases/latest"


# Ensure input entered is sensible
def validate_input():
    try:
        requests.get("https://google.com", timeout=5)
    except requests.ConnectionError:
        message_popup("You are not connected to the internet!", "Error")
        return False
    if not subject_var.get().isnumeric():
        message_popup("The subject code must be a number! Try again.", "Error")
        return False
    if not len(subject_var.get()) == 4:
        message_popup("The subject code must be a 4-digit number! Try again.", "Error")
        return False
    if not (subject_var.get() in IGCSE or subject_var.get() in ALevel or subject_var.get() in OLevel):
        message_popup("The subject code entered does not match a supported subject! Try again.", "Error")
        return False
    for paper_code in paper_var.get().split(','):
        paper_code = paper_code.strip(" ")
        if not paper_code.isnumeric():
            message_popup("The paper code must be a number! Try again.", "Error")
            return False
        if not len(paper_code) == 1:
            message_popup("The paper code must be a 1-digit number! Try again.", "Error")
            return False
    if not start_year.get().isnumeric():
        message_popup("The start year must be a number! Try again.", "Error")
        return False
    if not (len(start_year.get()) == 4 or len(start_year.get()) == 2):
        message_popup("The start year must be a 4-digit or 2-digit number! Try again.", "Error")
        return False
    if not end_year.get().isnumeric():
        message_popup("The end year must be a number! Try again.", "Error")
        return False
    if not (len(end_year.get()) == 4 or len(end_year.get()) == 2):
        message_popup("The end year must be a 4-digit or 2-digit number! Try again.", "Error")
        return False
    if not int(end_year.get()) >= int(start_year.get()):
        message_popup("The end year must be greater or equal to the start year! Try again.", "Error")
        return False
    if feb_march.get() == 'N' and may_june.get() == 'N' and oct_nov.get() == 'N':
        message_popup("You must select at least one exam series! Try again.", "Error")
        return False
    return True
