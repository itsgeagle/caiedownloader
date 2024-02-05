# Function to check program version.
import requests  # to make HTTP requests to GitHub API


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
