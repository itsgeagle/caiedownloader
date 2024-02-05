# Function to check program version.
import requests  # to make HTTP requests to GitHub API
from modules.gui import *
from modules.popup_handler import error_popup
from modules.dictionaries import SLUGS


#  Function to compare the current version with the latest version
def compare_version(current_version):
    # Fetch the latest version from GitHub API
    repo = "itsgeagle/caiedownloader"
    url = f"https://api.github.com/repos/{repo}/releases"

    # Check for latest version
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
                # Compare versions and display message accordingly
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


def validate_input():
    try:
        requests.get("https://google.com", timeout=5)
    except requests.ConnectionError:
        error_popup("You are not connected to the internet!")
        return False
    if not subject_var.get().isnumeric():
        error_popup("The subject code must be a number! Try again.")
        return False
    if not len(subject_var.get()) == 4:
        error_popup("The subject code must be a 4-digit number! Try again.")
        return False
    if not subject_var.get() in SLUGS:
        error_popup("The subject code entered does not match a supported subject! Try again.")
        return False
    if not paper_var.get().isnumeric():
        error_popup("The paper code must be a number! Try again.")
        return False
    if not len(paper_var.get()) == 1:
        error_popup("The paper code must be a 1-digit number! Try again.")
        return False
    if not start_year.get().isnumeric():
        error_popup("The start year must be a number! Try again.")
        return False
    if not (len(start_year.get()) == 4 or len(start_year.get()) == 2):
        error_popup("The start year must be a 4-digit or 2-digit number! Try again.")
        return False
    if not end_year.get().isnumeric():
        error_popup("The end year must be a number! Try again.")
        return False
    if not (len(end_year.get()) == 4 or len(end_year.get()) == 2):
        error_popup("The end year must be a 4-digit or 2-digit number! Try again.")
        return False
    if not int(end_year.get()) >= int(start_year.get()):
        error_popup("The end year must be greater or equal to the start year! Try again.")
        return False
    if feb_march.get() == 'N' and may_june.get() == 'N' and may_june.get() == 'N':
        error_popup("You must select at least one exam series! Try again.")
        return False
    return True
