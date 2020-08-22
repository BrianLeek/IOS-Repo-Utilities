#!/usr/bin/env python3
from functions import *
import os, sys, errno, bz2
from os import path
import pyinputplus as pyip
import sileo_depiction_generator
import config

console = Console()

def mainappfunc():
    global packagedebpath, source_file_, destination_file_, stop_script_error

    def exportdatainput():
        global new_file, new_file_packages
        new_file = input(f"Export data to a new {new_} file? ({answers}): ")

    def exportdatainputpackages():
        global new_packages_file
        new_packages_file = input(f"Export data to a new {new_} file or add to existing? ({answers}): ")

    def compress_packages_file():
        global compressionLevel, source_file, destination_file, tarbz2contents, fh

        compressionLevel = 9
        source_file = f"{source_file_}"
        destination_file = f"{destination_file_}"

        tarbz2contents = bz2.compress(open(source_file, 'rb').read(), compressionLevel)
        fh = open(destination_file, "wb")
        fh.write(tarbz2contents)
        fh.close()

        print("Packages files has been created and compressed.")

    welcometextfunc()
    print("\n * = Can leave blank (press enter) and auto fills with the data set in config.py.")

    createdebsfolder()

    options = input("1. Generate Release file\n2. Generate/Add to Packages file\n3. Compress Package File\n4. Generate control file\n5. Generate Sileo Depiction (possibly outdated but works)\n6. Generate repo from scratch or template\n7. ZIP to DEB (coming soon)\n8. DEB to ZIP (coming soon)\n\nPlease choose a option by entering the number: ")
    print(" ")

    if options == "1":
        # Ask the user for data for the release file, then ask if they want to export it or not.
        releasequestions()
        release_data = releasefiledata()

        new_ = "Release"
        answers = "y/n"

        exportdatainput()

        if new_file == "y":
            # Create the Release file and add the data to it.
            with open("Release", "w") as f:
                savedata = f.write(release_data)
                f.close()
        elif new_file == "n":
            stop_script()
    elif options == "2":
        # Ask the user for data for the Packages file, then ask if they want to export it or not.
        debquestions()
        data = packagefiledata()
        new_ = "Packages"
        answers = "n/e"
        source_file_ = "Packages"
        destination_file_ = "Packages.bz2"

        exportdatainputpackages()

        if new_packages_file == "n":
            # Create the Packages file and add the data to it.
            with open("Packages", "w") as f:
                savedata = f.write(data)
                f.close()

            compress_packages_file()
        elif new_packages_file == "e":
            with open("Packages", "a") as f:
                savedata = f.write(data)
                f.close()

            compress_packages_file()
    elif options == "3":
        if path.exists("Packages"):
            source_file_ = "Packages"
            destination_file_ = "Packages.bz2"

            compress_packages_file()
        else:
            stop_script_error = '\nFileNotFoundError: "Packages" file could not be found. Make sure it is uploaded to the root folder of the script and try again.'
            stop_script()
    elif options == "4":
        # Ask the user for data for the control file, then ask if they want to export it or not.
        controlquestions()
        control_data = controlfiledata()

        new_ = "control"
        answers = "y/n"

        exportdatainput()

        if new_file == "y":
            # Create the "control" file and add the data to it.
            os.makedirs(config.ControlPath)
            with open(f"{config.ControlPath}control", "w") as f:
                savedata = f.write(control_data)
                f.close()

                print("Successfully generated a control file.")
        elif new_file == "n":
            stop_script()
    elif options == "5":
        # Clear the console and start the sileo depiction generator script.
        clear_console()
        if __name__ == '__main__':
            sileo_depiction_generator.sileodepictiongeneraterfunc()
    elif options == "6":
        # Ask the user if they want to use a template or not, then run the functions based on their input.
        use_template = pyip.inputStr("Would you like to generate a repo using a template or from scratch? (template/scratch): ", allowRegexes=['template', 'scratch'], blockRegexes=[""])

        if use_template == "template" or "t":
            createrepotemplates()
        elif use_template == "new" or "n":
            createrepofolder()
            createrepoquestions()
            createrepo()
    elif options == "7":
        pass
    elif options == "8":
        pass
    elif options == "docs":
        clear_console()
        docstextfunc()

    # Don't close the window until the user wants to.
    input("Press enter to exit.")

if __name__ == '__main__':
    mainappfunc()
