# Function to check program version.
import requests  # to make HTTP requests to GitHub API


#  Function to compare the current version with the latest version
def compare_version(current_version):

    # Fetch the latest version from GitHub API
    repo = "itsgeagle/caiedownloader"
    url = f"https://api.github.com/repos/{repo}/releases"

    # Check for latest version
    response = requests.get(url)
    if response.status_code == 200:
        releases = response.json()
        if releases:
            latest_version = releases[0]["tag_name"]
            # Compare versions and display message accordingly
            if latest_version != current_version:
                return False, latest_version
            return True, None
        else:
            return False, "No releases were found. How did you even get the program?"
    else:
        return False, "Failed to fetch version. You can continue to use the program, but it is recommended to check " \
                      "GitHub for newer versions here - https://github.com/itsgeagle/caiedownloader/releases/latest"
