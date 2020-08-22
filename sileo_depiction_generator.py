#!/usr/bin/env python3
from functions import *
from rich.console import Console
from rich.markdown import Markdown
from rich import print
import main_app
import os
import sys
import json
import datetime
import fileinput
import config

####################
# Thanks to everybody who has contributed to Sileo Native Depiction Generater!
#
# Brian Leek - Developer (https://brianleek.me/)
# Mathsh - Contributed Code (https://www.reddit.com/user/Mathsh)
#   - Helped with adding screenshot support.
#   - Helped with adding changelog support.
#   - Helped fixed some bugs.
#   - Helped with some questions I had.
# Jon Betts - Contributed Code (https://stackoverflow.com/users/3569627/jon-betts)
#   - Helped with some code and a question I had.
####################

console = Console()

def sileodepictiongeneraterfunc():
    depictiongentext = config.DepictionGenTextFile

    if config.ShowDepictionGenText == True:
        with open(depictiongentext, encoding="utf8") as depictiongentext:
            depictiongen_markdown = Markdown(depictiongentext.read())
        console.print(depictiongen_markdown)
    else:
        pass

    print("\nYou may leave some fields blank.")
    print("Pick Template:")
    # List all files in the templates folder that end in .json.
    templatepath = config.TemplatesPath
    for templates in os.listdir(templatepath):
        if templates.endswith(".json"):
            print(" -", os.path.join(templates))
    template = input("\nTemplate Number: ")

    # Start Template 1
    if template == "1":
        # The name of the template that is being used.
        TemplateFileName = "template1.json"
        DefaultTintColor = "#2cb1be"

        try:
            # Call the questions that are in the functions above to ask the user some information to add to the depiction file later.
            TintColorQuestion()
            PackageIDQuestion()
            HeaderImageQuestion()
            PackageNameQuestion()
            PackageDescripionQuestion()
            LatestVersionQuestion()
            LatestReleasedDateQuestion()
            PriceQuestion()
            DeveloperQuestion()
            SupportURLQuestion()

            # Get the placeholder text in the template file and tells the script to replace that with what the user inputs.
            replacements = {'Tint Color':tintcolor, 'Header Image URL':headerimage, 'Package Name':packagename, 'Package Description':description, 'Latest Version Number':latestversion, 'Latest Release Date':latestreleasedate, 'Package Price':price, 'Package Developer':developer, 'Support URL':supporturl}
            # Remove placeholder text if input field is left blank.
            removeplaceholdertext = {'Header Image URL':'', 'Support URL':''}

            # If the folder to save the depiction file doesn't exists create it.
            try:
                if not os.path.exists(config.SaveDepictionPath):
                    os.makedirs(config.SaveDepictionPath)
            except ValueError:
                print("Failed to create the folder to save your depiction file. Please check config.py.")

            # Try and create the depiction file with the input entered in the package id question.
            with open(config.TemplatesPath+TemplateFileName) as infile, open(config.SaveDepictionPath+packageid, 'w') as outfile:
                # Replace the placeholder text that was entered in "replacements" with the information the user inputs.
                try:
                    for createdepictionfile in infile:
                        for src, target in replacements.items():
                            createdepictionfile = createdepictionfile.replace(src, target)
                        outfile.write(createdepictionfile)
                    print("Successfully created "+ packageid +" in "+ config.SaveDepictionPath+".")
                except ValueError:
                    print("Failed to create "+ packageid +" in "+ config.SaveDepictionPath+".")

                # Try and remove the placeholder text that was entered in "removeplaceholdertext".
                try:
                    for removeplaceholders in infile:
                        for placeholder, removeplaceholder in removeplaceholdertext.items():
                            removeplaceholders = removeplaceholders.replace(placeholder, removeplaceholder)
                        outfile.write(removeplaceholders)
                    print("Successfully removed placeholder text.")
                except ValueError:
                    print("Failed to remove placeholder text.")

            # Load the data
            file_name = config.SaveDepictionPath+packageid
            with open(file_name) as fh:
                full_data = json.load(fh)

            screenshot_template = full_data['tabs'][0]['views'][1]['screenshots'][0]
            full_data['tabs'][0]['views'][1]['screenshots'].pop(0)
            screenshot_url = input("Screenshot URL: ")
            while screenshot_url != "":
                modified_screenshot_template = screenshot_template
                modified_screenshot_template['url'] = screenshot_url
                modified_screenshot_template['fullSizeURL'] = screenshot_url
                full_data['tabs'][0]['views'][1]['screenshots'].append(modified_screenshot_template.copy())
                screenshot_url = input("Screenshot URL (Enter a blank string when you are finished): ")
            if full_data['tabs'][0]['views'][1]['screenshots'] == []:
                full_data['tabs'][0]['views'].pop(1)

            # Thanks Mathsh for the code! (https://www.reddit.com/user/Mathsh)
            changelog_header_template = full_data['tabs'][1]['views'].pop(0)
            changelog_body_template = full_data['tabs'][1]['views'].pop(0)
            version_number = input('Version Number (Newest to oldest): ')
            while version_number != '':
                print("Please enter one change at a time once you entered some info you can hit return/enter to input another change or don't enter anything and just press return/enter when finished.")
                changes = ''
                change = input(version_number + ' Changes (Enter a blank string when you are finished): ')
                while change != '':
                    changes = changes + '\t\n\u2022 ' + change + ' '
                    change = input(version_number + ' Changes (Enter a blank string when you are finished): ')
                changes = changes + ''
                modified_changelog_header_template = changelog_header_template
                modified_changelog_header_template['title'] = version_number
                modified_changelog_body_template = changelog_body_template
                modified_changelog_body_template['markdown'] = changes
                full_data['tabs'][1]['views'].append(changelog_header_template.copy())
                full_data['tabs'][1]['views'].append(changelog_body_template.copy())
                version_number = input('Version Number (Newest to oldest) (Enter a blank string when you are finished): ')
            if full_data['tabs'][1]['views'] == []:
                full_data['tabs'].pop(1)

            # Save the data
            with open(file_name, 'w') as fh:
                json.dump(full_data, fh, indent=4)

            print("Successfully generated your depiction file.")
        except ValueError:
            print("Failed to generate your depiction file.")

        # Don't close the window until the user wants to.
        input("Press enter to exit.")
    # End Template 1

    # Start Template 2
    elif template == "2":
        # The name of the template that is being used.
        TemplateFileName = "template2.json"
        DefaultTintColor = "#2cb1be"

        try:
            # Call the questions that are in the functions above to ask the user some information to add to the depiction file later.
            TintColorQuestion()
            PackageIDQuestion()
            HeaderImageQuestion()
            PackageDescripionQuestion()
            LatestVersionQuestion()
            PriceQuestion()
            DeveloperQuestion()
            SupportURLQuestion()

            # Get the placeholder text in the template file and tells the script to replace that with what the user inputs.
            replacements = {'Tint Color':tintcolor, 'Header Image URL':headerimage, 'Package Description':description, 'Latest Version Number':latestversion, 'Package Price':price, 'Package Developer':developer, 'Support URL':supporturl}
            # Remove placeholder text if input field is left blank.
            removeplaceholdertext = {'Header Image URL':'', 'Support URL':''}

            # If the folder to save the depiction file doesn't exists create it.
            try:
                if not os.path.exists(config.SaveDepictionPath):
                    os.makedirs(config.SaveDepictionPath)
            except ValueError:
                print("Failed to create the folder to save your depiction file. Please check config.py.")

            # Try and create the depiction file with the input entered in the package id question.
            with open(config.TemplatesPath+TemplateFileName) as infile, open(config.SaveDepictionPath+packageid, 'w') as outfile:
                # Replace the placeholder text that was entered in "replacements" with the information the user inputs.
                try:
                    for createdepictionfile in infile:
                        for src, target in replacements.items():
                            createdepictionfile = createdepictionfile.replace(src, target)
                        outfile.write(createdepictionfile)
                    print("Successfully created "+ packageid +" in "+ config.SaveDepictionPath+".")
                except ValueError:
                    print("Failed to create "+ packageid +" in "+ config.SaveDepictionPath+".")

                # Try and remove the placeholder text that was entered in "removeplaceholdertext".
                try:
                    for removeplaceholders in infile:
                        for placeholder, removeplaceholder in removeplaceholdertext.items():
                            removeplaceholders = removeplaceholders.replace(placeholder, removeplaceholder)
                        outfile.write(removeplaceholders)
                    print("Successfully removed placeholder text.")
                except ValueError:
                    print("Failed to remove placeholder text.")

            # Load the data
            file_name = config.SaveDepictionPath+packageid
            with open(file_name) as fh:
                full_data = json.load(fh)

            # Thanks Mathsh for the code! (https://www.reddit.com/user/Mathsh)
            screenshot_template = full_data['tabs'][0]['views'][3]['screenshots'][0]
            full_data['tabs'][0]['views'][3]['screenshots'].pop(0)
            screenshot_url = input("Screenshot URL: ")
            while screenshot_url != "":
                modified_screenshot_template = screenshot_template
                modified_screenshot_template['url'] = screenshot_url
                modified_screenshot_template['fullSizeURL'] = screenshot_url
                full_data['tabs'][0]['views'][3]['screenshots'].append(modified_screenshot_template.copy())
                screenshot_url = input("Screenshot URL (enter a blank string when you are finished): ")
            if full_data['tabs'][0]['views'][3]['screenshots'] == []:
                full_data['tabs'][0]['views'].pop(3)

            # Thanks Mathsh for the code! (https://www.reddit.com/user/Mathsh)
            changelog_header_template = full_data['tabs'][1]['views'].pop(0)
            changelog_body_template = full_data['tabs'][1]['views'].pop(0)
            version_number = input('Version Number (Newest to oldest): ')
            while version_number != '':
                print("Please enter one change at a time once you entered some info you can hit return/enter to input another change or don't enter anything and just press return/enter when finished.")
                changes = '<ul>'
                change = input(version_number + ' Changes: ')
                while change != '':
                    changes = changes + '\n<li>' + change + '<\/li>'
                    change = input(version_number + ' Changes: ')
                changes = changes + '<\/ul>'
                modified_changelog_header_template = changelog_header_template
                modified_changelog_header_template['title'] = version_number
                modified_changelog_body_template = changelog_body_template
                modified_changelog_body_template['markdown'] = changes
                full_data['tabs'][1]['views'].append(changelog_header_template.copy())
                full_data['tabs'][1]['views'].append(changelog_body_template.copy())
                version_number = input('Version Number (Newest to oldest) (Enter a blank string when you are finished): ')
            if full_data['tabs'][1]['views'] == []:
                full_data['tabs'].pop(1)

            # Save the data
            with open(file_name, 'w') as fh:
                json.dump(full_data, fh, indent=4)

            print("Successfully generated your depiction file.")
        except ValueError:
            print("Failed to generate your depiction file.")

        # Don't close the window until the user wants to.
        input("Press enter to exit.")
    # End Template 2
    # NOT WORKING
    elif template == "exitapp":
        clear_console()
        import subprocess
        # if __name__ == '__main__':
        #     main_app.mainappfunc()
        subprocess.call("main_app.py")



    # Show the user a error if they enter a number for a template that can't be found.
    else:
        print("The template you are looking for can not be found!")
        # Don't close the window until the user wants to.
        input("Press enter to exit.")

if __name__ == '__main__':
    sileodepictiongeneraterfunc()
