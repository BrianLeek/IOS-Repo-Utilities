# How To Setup IOS Repo Utilities

To setup **IOS Repo Utilities** you need to run **setup.sh** and that will install all needed dependencies to run the script and also allow you to setup the needed files. The script can still run without these files at times and if it does some functions of the script might be broke or don't work at all so keep that in mind. After the script is setup all you need to do is run **main_app.py**.

# Options

**IOS Repo Utilities** provides a few tools to help IOS jailbreak developers who run a repo or for people who want to create a repo. Want a create a "Packages" file, then compress it so its ready to use instantly? Well, create a new folder called "debs", copy your .deb files there and run the script. Want to create a whole repo without messing with files? Now you can, run the script and choose to use a template or not and the script will walk you through the rest, like creating a "Release" and "Packages" files, etc. You can even create depictions for Sileo (https://getsileo.app/).

## Generate Release File

To generate a release file just run **main_app.py** and input the number **1**. The script will then walk you through some questions for your release file, after you answers those questions the script will then ask you if you want to export the data to a new **release** file. You can enter **y for yes** and **n for no**. If you enter **y** the script will create a new file in your scripts root folder called **Release** and that will be your **release** file.

## Generate or Add To Packages File

To generate or add to an existing Packages file just run **main_app.py** and input the number **2**. The script will then walk you through some questions for your Packages file, after you answers those questions the script will then ask you if you want to export the data to a new **Packages** file. You can enter **y for yes** and **n for no**. If you enter **y** the script will create a new file in your scripts root folder called **Packages** and compress it as well and that will create a file called "Packages.bz2".

## Compress Existing Package File

To compress an existing Packages file just run **main_app.py** and input the number **3**. The script will then compress the **Packages** that you uploaded to the scripts root folder. This will create a new file called **Packages.bz2**.

## Generate Release File

To generate a release file just run **main_app.py** and input the number **4**. The script will then walk you through some questions for your release file, after you answers those questions the script will then ask you if you want to export the data to a new **release** file. You can enter **y for yes** and **n for no**. If you enter **y** the script will create a new file in your scripts root folder called **Release** and that will be your release file.

## Generate Control File

To generate a control file just run **main_app.py** and input the number **6**. The script will then walk you through some questions for your control file, after you answers those questions the script will then ask you if you want to export the data to a new **control** file. You can enter **y for yes** and **n for no**. If you enter **y** the script will create a new folder in your scripts root folder called **DEBIAN** and inside that will be your control file.
