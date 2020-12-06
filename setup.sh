#!/bin/bash
echo "IOS Repo Utilities Setup"
echo ""
if [ ! -f .is_setup ]; then
    echo "Give us a second to install the Python dependencies."
    pip3 install -r requirements.txt
    if [ $? -eq 2 ]; then
        echo "Error: Something went wrong. We may need root to continue. Please put in your password to continue."
        sudo pip3 install -r requirements.txt
        if [ $? -eq 2 ]; then
            echo "Error: Cannot install Python dependencies. Check your permissions and try again."
            exit
        fi
    fi
    echo "Installed all required packages! Now, just a few questions about you. You can edit these later in config.py."
    echo ""
	echo "* = Can leave blank (press enter) and will auto fill the default data for that input in config.py."
	echo ""
  echo "Developers Information - This information makes it a ease when creating things like a Packages file because you won't need to enter your name, email, or homepage the script will use the info you enter here for that."
  echo ""
  echo "Example: Dev123 <dev123@email.com>"
	while true; do
		printf "Author: "
		read author
	if [[ "$author"  != "" ]]
	then
		break
	fi
	done

	echo "Example: Dev123 <dev123@email.com>"
	while true; do
		printf "Maintainer:* "
		read maintainer
	if [[ "$maintainer"  != "" ]]
	then
		break
	else
		maintainer="$author"
		break
	fi
	done

	echo "Example: https://dev123website.com/"
	while true; do
		printf "Homepage: "
		read homepage
	if [[ "$homepage"  != "" ]]
	then
		break
	fi
	done

	echo ""
	echo "Package Information - This information will be used in inputs where nothing is typed when creating things like a Packages file."
  echo ""
	echo "You can choose to addon to the list below when that part of the script is ran."
	printf "Package Depends:* "
	read packagedepends
	if [[ "$packagedepends" = "" ]]
	then
		packagedepends=""
	fi

	echo "Example: Tweaks"
	printf "Packages Section:* "
	read packagesection
	if [[ "$packagesection" = "" ]]
	then
		packagesection="Tweaks"
	fi

	echo "Example: 1.0"
	printf "Package Version:* "
	read packageversion
	if [[ "$packageversion" = "" ]]
	then
		packageversion="1.0"
	fi

	echo "# Developers Information - This information makes it a ease when creating things like a Packages file because you won't need to enter your name, email, or homepage the script will use the info you enter here for that.
Author = \"$author\" # Name of the auther who developed the package. Eg: Brian Leek <brianleek2016@gmail.com>
Maintainer = \"$maintainer\" # Name of the package maintainer. Eg: Brian Leek <brianleek2016@gmail.com>
Homepage = \"$homepage\" # Package developers website/homepage. Eg: https://brianleek.me/. Trending slash "/" at the end of url is required!
RepoURLPath = \"repo/\" # This is not the same as \"RepoPath\". This is only if you want the script to know where your repo is hosted by using the homepage url and add RepoURLPath to the end.

# Package Information - This information will be used in inputs where nothing is typed.
PackageDepends = \"$packagedepends\" # List of package depends that will be used when creating Packages or control files. You can choose to addon to the list when that part of the script is ran.
PackageSection = \"$packagesection\" # Default to use in package section input. To use it just press enter whenever the question comes up.
PackageVersion = \"$packageversion\" # Default package version to be used if nothing is entered in the version input.

RepoSuite = \"stable\" # Default repo suite to be used if nothing is entered in the repo suite input.
RepoVersion = \"1.0\" # Default repo version to be used if nothing is entered in the version input.
RepoCodeName = \"ios\" # Default repo codename to be used if nothing is entered in the codename input.
RepoComponents = \"main\" # Default repo components to be used if nothing is entered in the roei components input.
RepoArchitecture = \"iphoneos-arm\" # # Default repo architecture to be used if nothing is entered in the repo architecture input. Also used when generating a control or Packages file.

# GPG Information - This information will be used for the control file that will be made when GPG signing is ran.
GPGKeyringFileName = \"keyring\" # GPG keyring name to be used when creating the keyring folder. If changed please update it in \"gen_key_gpg\".
GPGRepoName = \"Repositorie APT Keyring\" # Default repo name to be used in the control file.
GPGRepoDescription = \"GnuPG key for repositorie.\" # Default repo description to be usedd in the control file.

# Save Paths - These paths are used to save files that may be generated or files that might need to be used later.
DebsPath = \"debs/\" # Path to where you want the script to search for debs files you uploaded. Make sure to include the trending slash "/" at the end of your path.
ControlPath = \"DEBIAN/\" # Path to where you want the script to save the control file. Make sure to include the trending slash "/" at the end of your path.
RepoPath = \"repo/\" # Path which to save a repo after it is created.
RepoTemplatePath = \"templates/repos/\" # Path where the repo templates are stored.
DefaultRepoTemplate = \"default/\"
TemplatesPath = \"templates/depictions/\" # Path to the templates folder. Make sure to include the trending slash "/" at the end of your path.
SaveDepictionPath = \"depictions/user/templates/\" # Path where the depition file will be saved to once it's created. Make sure to include the trending slash "/" at the end of your path or it wont save the depiction file in the right place.

# Display Options - Choose to display items within the script or not.
ShowWelcomeText = True # Show welcome text each time the script runs. True or False.
ShowDepictionGenText = True # Show depiction generater text each time the depiction gen script is ran. True or False.

# .md Files - You probably won't need to edit theses but this is just the paths to the .md files that stores text to be displayed later.
WelcomeTextFile = \"markdown/welcome.md\" # File that stores the welcome text that will be displayed.
DepictionGenTextFile = \"markdown/depiction_gen_wel.md\" # File that stores the text that will be displayed when the depiction gen script is ran.
DocsTextFile = \"markdown/docs.md\" # File that stores the text for the docs that will be displayed.
" > config.py

	mkdir "debs"

  echo ""
  echo "Thank you! Now let us generate you some GPG keys. Keep these somewhere safe or you may not be able to edit your repo anymore!"
  echo "   ENTROPY NOTICE: Please do stuff in the meantime like spam some keys or wiggling your mouse. We need entropy!"
  gpg --batch --gen-key util/gpg.batchgen
  echo "Exported key into your GPG keyring."
	echo ""
	echo "Credit goes to Shuga (https://github.com/Shugabuga) for the setup.sh file."
  echo "IOS Repo Utilities was successfully setup! Remember you can edit theses options at anytime in config.py."
  echo ""
	touch .is_setup
else
	echo "IOS Repo Utilities has already been set up. Aborting..."
fi
