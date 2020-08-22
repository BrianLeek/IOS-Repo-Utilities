from shutil import copyfile
from rich.console import Console
from rich.markdown import Markdown
from rich import print
from main_app import *
import os, sys, errno, bz2
import pyinputplus as pyip
import hashlib
import config
import errno
import shutil

console = Console()

###################################################
#     # #   User Input Data Functions             #
#   ####### Below are a set of functions          #
#     # #   that will be used to ask for user     #
#   ####### input and stores that data to be      #
#     # #   used in the script at a later time.   #
###################################################
def releasequestions(): # Ask the user a series of questions then store that data to create a "Release" file later.
    global repo_origin, repo_label, repo_suite, repo_version, repo_codename, repo_architecture, repo_components, repo_description

    repo_origin = pyip.inputStr("Repo Name: ")
    repo_label = pyip.inputStr("Label:* ", blank=True)
    if repo_label == "":
        repo_label = repo_origin
    repo_suite = config.RepoSuite
    repo_version = pyip.inputFloat("Version:* ", blank=True)
    if repo_version == "":
        repo_version = config.RepoVersion
    repo_codename = pyip.inputStr("Codename (default: ios):* ", blank=True)
    if repo_codename == "":
        repo_codename = config.RepoCodeName
    repo_architecture = config.RepoArchitecture
    repo_components = config.RepoComponents
    repo_description = pyip.inputStr("Description: ")

def debquestions(): # Ask the user a series of questions then store that data to create a "Packages" file later.
    global deb_package_name, deb_file_name, deb_package_description, does_depend_on, depends, deb_package_depends, deb_package_maintainer, deb_package_author, deb_package_version, deb_package_section, deb_package_md5hash, deb_package_sha1hash, deb_package_sha256hash, homepage, deb_package_depiction, architecture, deb_package_size, filename, stop_script_error

    deb_package_name = pyip.inputStr("Package Name (eg. Tweak Name): ")
    {deb_search()}
    deb_file_name = pyip.inputStr("Package File Name (eg. com.example.tweakname.deb): ")
    try:
        deb_package_size = os.path.getsize(f"{config.DebsPath}{deb_file_name}")
    except FileNotFoundError:
        stop_script_error = "\nFileNotFoundError: Could not get the size of the .deb file with the information provided because the file can not be found. Please try again."
        stop_script()
    str2hash = deb_file_name
    md5result = hashlib.md5(str2hash.encode())
    sha256result = hashlib.sha256(str2hash.encode())
    sha1result = hashlib.sha1(str2hash.encode())
    md5hash = md5result.hexdigest()
    sha256hash = sha256result.hexdigest()
    sha1hash = sha1result.hexdigest()
    print(" ")
    print(r'In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.')
    deb_package_description = pyip.inputStr("Package Description: ")
    does_depend_on = pyip.inputStr("Does This Package Depend on Anything? (y/n): ")
    if does_depend_on == "y":
        deb_package_depends = pyip.inputStr(f"Package Depends On:* ", blank=True)
        depends = f"\nDepends: {config.PackageDepends}{config.PackageDepends}"
    elif does_depend_on == "n":
        deb_package_depends = ""
        depends = ""
    deb_package_maintainer = config.Maintainer
    deb_package_author = config.Author
    deb_package_version = pyip.inputFloat("Package Version:* ", blank=True)
    if deb_package_version == "":
        deb_package_version = config.PackageVersion
    deb_package_section = pyip.inputStr("Package Section:* ", blank=True)
    if deb_package_section == "":
        deb_package_section = config.PackageSection
    homepage = config.Homepage
    deb_package_depiction = input("Package Depiction URL (eg. description.html?id=me.brianleek.aurora). This uses your homepage url set in config.py. No slash needed in the begeinning of the depiction url because it was added in the url in config.py : ")
    deb_package_md5hash = md5hash
    deb_package_sha1hash = sha1hash
    deb_package_sha256hash = sha256hash
    architecture = "iphoneos-arm"
    filename = f"./debs/{deb_file_name}"

    print(" ")

def controlquestions(): # Ask the user a series of questions then store that data to create a "control" file later.
    global control_package, control_name, control_version, control_section, control_architecture, control_description, control_maintainer, control_author, control_homepage

    control_name = pyip.inputStr("Package Name (eg. Tweak Name): ")
    control_package = input("Package (eg. com.example.tweakname): ")
    control_version = pyip.inputFloat("Version:* ", blank=True)
    if control_version == "":
        control_version = config.PackageVersion
    control_section = pyip.inputStr("Section:* ", blank=True)
    if control_section == "":
        control_section = config.PackageSection
    control_larchitecture = config.RepoArchitecture
    control_description = pyip.inputStr("Description: ")
    control_author = config.Author
    control_maintainer = config.Maintainer
    control_homepage = config.Homepage

def releasefiledata(): # Put the data the user entered into a variable to display later in the terminal.
    global release_data

    console.print("\n[bold]Repo Release File Data[/bold]")
    release_data = f"""Origin: {repo_origin}
Label: {repo_label}
Suite: {repo_suite}
Version: {repo_version}
Codename: {repo_codename}
Architecture: {repo_architecture}
Components: {repo_components}
Description: {repo_description}
"""

    print(release_data)
    return(release_data)

def packagefiledata(): # Put the data the user entered into a variable to display later in the terminal.
    global data, depends

    console.print("\n[bold]Packages File Data[/bold]")
    data = f"""Package: {os.path.splitext(deb_file_name)[0]}
Name: {deb_package_name}
Version: {deb_package_version}
Size: {deb_package_size}
Architecture: {architecture}
Description: {deb_package_description}{depends}
Maintainer: {deb_package_maintainer}
Author: {deb_package_author}
Section: {deb_package_section}
MD5: {deb_package_md5hash}
SHA1: {deb_package_sha1hash}
SHA256: {deb_package_sha256hash}
Homepage: {homepage}
Depiction: {config.Homepage}{deb_package_depiction}
Filename: {filename}
\n"""

    print(data)
    return(data)

def controlfiledata(): # Put the data the user entered into a variable to display later in the terminal.
    global control_data

    console.print("[bold]Package Control File Data[/bold]")
    control_data = f"""Package: {control_package}
Name: {control_name}
Version: {control_version}
Section: {control_section}
Architecture: {control_architecture}
Description: {control_description}
Author: {control_author}
Maintainer: {control_maintainer}
Homepage: {control_homepage}
"""

    print(control_data)
    return(control_data)

###################################################
#     # #   Repo Generator Functions              #
#   ####### Below are a set of functions          #
#     # #   that help generate/create repos       #
#   ####### from scratch or from a template       #
#     # #   that a user can pick from.            #
###################################################
def createrepofolder(): # Creates the folder to store the repos files.
    global stop_script_error

    if os.path.exists(config.RepoPath):
        print("\nCreating the folder to store the repo...\nRepo folder already exists.\n")
    else:
        print("\nCreating the repo folder...")
        try:
            os.makedirs(config.RepoPath)
            print("Successfully created the repo folder.\n")
        except ValueError:
            stop_script_error = "Error: There was a error creating the repo folder. Please check the config.py file and try again.\n"
            stop_script()

def createdebsfolder(): # Creates the folder to store the deb files.
    global stop_script_error

    if os.path.exists(config.DebsPath):
        print(" ")
    else:
        try:
            os.makedirs(config.DebsPath)
            print(" ")
        except ValueError:
            stop_script_error = "Error: There was a error creating the debs folder. Please check the config.py file and try again.\n"
            stop_script()

def createrepoquestions(): # Asks for data for the "Release" file, then create it. After, ask the user to create a Packages file then compress it.
    global new_, answers, source_file_, destination_file_

    print('Create "Release" file:')
    releasequestions()
    releasefiledata()

    new_ = "Release"
    answers = "y/n"

    exportdatainput()

    if new_file == "y":
        # Create the Release file and add the data to it.
        with open(f"{config.RepoPath}Release", "w") as f:
            savedata = f.write(release_data)
            f.close()
    elif new_file == "n":
        stop_script()

    createpackagefile = input("Would you like to create a Packages file? (y/n): ")

    if createpackagefile == "y":
        debquestions()
        data = packagefiledata()

        new_ = "Packages"
        answers = "n/e"

        exportdatainputpackages()

        if new_packages_file == "n":
            # Create the Packages file and add the data to it.
            with open(f"{config.RepoPath}Packages", "w") as f:
                savedata = f.write(data)
                f.close()

            source_file_ = f'{config.RepoPath}Packages'
            destination_file_ = f'{config.RepoPath}Packages.bz2'
            compress_packages_file()
        elif new_packages_file == "e":
            with open(f"{config.RepoPath}Packages", "a") as f:
                savedata = f.write(data)
                f.close()

            source_file_ = f'{config.RepoPath}Packages'
            destination_file_ = f'{config.RepoPath}Packages.bz2'
            compress_packages_file()

def createrepo(): # If no template is used, then create a index.html file, then copy over the default repo set of files.
    with open(f"{config.RepoPath}index.html", "w") as index_file:
        index_data = f'''<!DOCTYPE html>
<html><head>
<title>{config.Author}\'s Cydia Repo</title>
<link rel="stylesheet" type="text/css" href="{config.RepoPath}css/ios7.css"/>
<meta name="viewport" content="width=320; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;"/>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<script src="{config.RepoPath}jquery-3.2.1.min.js"></script>
<script src="{config.RepoPath}description.js?_=4654659"></script>
<body>
<h2> </h2>
<ul>
	<li>
		<a href="cydia://url/https://cydia.saurik.com/api/share#?source={config.Homepage}{config.RepoURLPath}">
			<img class="icon" src="{config.RepoPath}images/cydia7.png"/>
			<label>Open Cydia</label>
		</a>
	</li>
</ul>

<p style="text-align:center;">Repo: {config.Homepage}{config.RepoURLPath}</p>
<h2>Repo</h2>
<ul>
	<li>
		<a href="{config.RepoPath}packagepage/index.html">
			<img class="icon" src="{config.RepoPath}images/packages.png"/>
			<label>Packages</label></a>
	</li>
</ul>
<h2>Support Me</h2>
<ul>
	<li>
		<a href="#" target="_blank">
			<img class="icon" src="{config.RepoPath}images/pp.png"/>
			<label>Donate</label>
		</a>
	</li>
</ul>
<h2>Social</h2>
<ul>
	<li>
		<a href="#" target="_blank">
			<img class="icon" src="{config.RepoPath}images/github.png"/>
			<label>GitHub</label>
		</a>
	</li>
	<li>
		<a href="#" target="_blank">
			<img class="icon" src="{config.RepoPath}images/reddit.png"/>
			<label>Reddit</label>
		</a>
	</li>
	<li>
		<a href="#" target="_blank">
			<img class="icon" src="{config.RepoPath}images/twitter.png"/>
			<label>Twitter</label>
		</a>
	</li>
</ul>
<p style="text-align:center;">© {repo_origin}.<br />Repo code from <a target="_blank" href="https://github.com/julioverne/julioverne.github.io">julioverne.github.io</a>.</p>
</body></html>'''
        index_file.write(index_data)

    copytree(f"{config.RepoTemplatePath}{config.DefaultRepoTemplate}", f"{config.RepoPath}")

def createrepotemplatequest(): # Find the template the user selects and ask more questions if needed, then create the files needed.
    if repo_template == "Reposi3":
        with open(f"{config.RepoPath}index.html", "w") as index_file:
            index_data = f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>{repo_origin}</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
<link rel="stylesheet" href="{config.RepoPath}/style.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
</head>
<body>

<div class="container">
<h1><img src="CydiaIcon.png">{repo_origin}</h1>
</div>

<div class="container">
<div class="card">
	<div class="card-body">
		<p><span class="text-primary"><b>{repo_origin}</span></b> is a Cydia repository template.</p>
		<a class="btn btn-sm btn-primary" href="cydia://url/https://cydia.saurik.com/api/share#?source={config.Homepage}{config.RepoPath}">Add to Cydia</a>
	</div>
</div>
</div>
<p></p>
<div class="container">
<h3 id="wells" class="page-header">Featured Packages</h3>
</div>

<div class="container">
<div class="card">
	<div class="card-header">
		Old Package
	</div>
	<div class="card-body">
	  <p class="card-text">This is a sample package with minimal information.
		It also simulates an old package that's incompatible only with iOS lower than 7.0.</p>
		<a class="btn btn-xs btn-primary" href="{config.RepoPath}depictions/?p=com.supermamon.oldpackage">More info</a>
	</div>
</div>
<div class="card">
	<div class="card-header">
		New Package
	</div>
	<div class="card-body">
	  <p class="card-text">This is a sample package with lots of information.</p>
	  <a class="btn btn-xs btn-primary" href="{config.RepoPath}depictions/?p=com.supermamon.newpackage">More info</a>
	</div>
</div>

</div>

</body>
</html>
"""
            index_file.write(index_data)

        createrepoxml = pyip.inputStr("Would you like to create a repo xml file? (y/n): ", allowRegexes=["y", "n"], blockRegexes=[""])

        if createrepoxml == "y":
            twitterurl = input("Twiiter URL: ")
            with open(f"{config.RepoPath}repo.xml", "w") as repo_xml:
                xml_data = f"""<repo>
<footerlinks>
	<link>
		<name>Follow me on Twitter</name>
		<url>{twitterurl}</url>
		<iconclass>fa fa-twitter</iconclass>
	</link>
	<link>
		<name>I want this depiction template</name>
		<url>https://github.com/supermamon/Reposi3/</url>
		<iconclass>fa fa-thumbs-up</iconclass>
	</link>
</footerlinks>
</repo>
                """
                repo_xml.write(xml_data)

def createrepotemplates(): # List out the repo templates then, create the repo folder. After, find which template the user picked then copy the template files to the "repo" folder.
    global repo_template

    for repo_templates in os.listdir(config.RepoTemplatePath):
        print(" -", os.path.join(repo_templates))

    repo_template = pyip.inputStr("Which template would you like to use?: ", allowRegexes=[""], blockRegexes=["default"])

    if not repo_template == repo_templates:
        print("Repo template not found. Please check your spelling and try again.")

    while not repo_template == repo_templates:
        repo_template = pyip.inputStr("Which template would you like to use?: ", allowRegexes=[""], blockRegexes=["default"])

        if not repo_template == repo_templates:
            print("Repo template not found. Please check your spelling and try again.")

    createrepofolder()

    if repo_template == repo_templates:
        createrepoquestions()
        copytree(f"{config.RepoTemplatePath}{repo_template}", f"{config.RepoPath}") # Copy over the files from the template to the repo folder.
        copyfile(f"{config.DebsPath}{deb_file_name}", f"{config.RepoPath}debs/{deb_file_name}") # Copy over the deb file to the repo folder.
        createrepotemplatequest()

###################################################
#     # #   Miscellaneous Functions               #
#   ####### Below are a set of functions          #
#     # #   that will be used throughout the      #
#   ####### script at random times or at certin   #
#     # #   times when needed.                    #
###################################################
def deb_search(): # List all files in the debs folder that end in .deb.
    global debs, stop_script_error
    print(f"\nDebs found in {config.DebsPath}:")

    for debs in os.listdir(config.DebsPath):
        if debs.endswith(".deb"):
            print(" -", os.path.join(debs))
    if len(os.listdir(config.DebsPath)) == 0:
        stop_script_error = f'Error: No debs found in "{config.DebsPath}" Please upload some deb files to "{config.DebsPath}" and try again.'
        stop_script()

def exportdatainput():
    global new_file, new_file_packages

    new_file = pyip.inputStr(f"Export data to a new {new_} file? ({answers}): ")

def exportdatainputpackages():
    global new_packages_file

    new_packages_file = pyip.inputStr(f"Export data to a new {new_} file or add to existing? ({answers}): ")

def compress_packages_file(): # Compress the "Packages" file to "Packages.bz2".
    global compressionLevel, source_file, destination_file, tarbz2contents, fh

    compressionLevel = 9
    source_file = f"{source_file_}"
    destination_file = f"{destination_file_}"

    tarbz2contents = bz2.compress(open(source_file, 'rb').read(), compressionLevel)
    fh = open(destination_file, "wb")
    fh.write(tarbz2contents)
    fh.close()

    print("Packages files has been created.")

def clear_console():
    global clear

    clear = lambda: os.system('cls')
    clear = os.system('cls')

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def welcometextfunc():
    global welcometextfile, welcome_markdown

    welcometextfile = config.WelcomeTextFile

    if config.ShowWelcomeText == True:
        with open(welcometextfile, encoding="utf8") as welcometext:
            welcome_markdown = Markdown(welcometext.read())
        console.print(welcome_markdown)
    else:
        pass

def depictiongentextfunc():
    global depictiongentext, depictiongen_markdown

    depictiongentext = config.DepictionGenTextFile

    if config.ShowDepictionGenText == True:
        with open(depictiongentext, encoding="utf8") as depictiongentext:
            depictiongen_markdown = Markdown(depictiongentext.read())
        console.print(depictiongen_markdown)
    else:
        pass

def docstextfunc():
    global docs_markdown

    with open(config.DocsTextFile, encoding="utf8") as docstext:
        docs_markdown = Markdown(docstext.read())
    console.print(docs_markdown)

def stop_script():
    global script_stopped
    script_stopped = True

    if script_stopped == True:
        if stop_script_error == "":
            sys.exit("\nThe script has been killed.")
        else:
            sys.exit(f"\n{stop_script_error}")

###################################################
#     # #   Sileo Depiction Generator Functions   #
#   ####### Below are a set of functions          #
#     # #   that help generate/create depictions  #
#   ####### using the Sileo Native Depiction      #
#     # #   Generator script by Brian Leek        #
###################################################
def TintColorQuestion(): # Put the questions to ask the user in a function to use later. By adding them into a function it makes it might make it easier when adding a templale to the script.
    global tintcolor
    tintcolor = input("Tint Color (default: #2cb1be): ")
    while True:
        try:
            if tintcolor == "":
                tintcolor = "#2cb1be"
                continue
            else:
                break
        except ValueError:
            break


def HeaderImageQuestion():
    global headerimage
    headerimage = input("Header Image URL: ")


def PackageIDQuestion():
    # This is required to generate the depiction file and should be included in the questions on all templates.
    global packageid
    while True:
        try:
            packageid = input("Package ID (com.example.package): ")
            if packageid == '':
                print("Please enter a ID for your package.")
                continue
            else:
                break
        except ValueError:
            break


def PackageNameQuestion():
    global packagename
    while True:
        try:
            packagename = input("Package Name: ")
            if packagename == '':
                print("Please enter a name for your package.")
                continue
            else:
                break
        except ValueError:
            break


def PackageDescripionQuestion():
    global description
    while True:
        try:
            description = input("Package Description: ")
            if description == '':
                print("Please enter a description for your package.")
                continue
            else:
                break
        except ValueError:
            break


def KnownIssuesQuestion():
    global knownissues
    knownissues = input("Known Issues: ")


def FirstVersionQuestion():
    global firstversion
    while True:
        try:
            firstversion = input("First Release Version Number (Example: 1.0): ")
            if firstversion == '':
                print("Please enter the first released version number for your package.")
                continue
            elif firstversion.isalpha():
                print("Please enter a number not a string.")
                continue
            else:
                break
        except ValueError:
            break


def FirstReleaseDateQuestion():
    global firstreleasedate
    while True:
        try:
            firstreleasedate = input("First Version Release Date (YYYY/MM/DD): ")
            if firstreleasedate == '':
                print("Please enter the date your package was first released.")
                continue
            else:
                pass
            datetime.datetime.strptime(firstreleasedate, '%Y/%m/%d')
            break
        except ValueError:
            print("Incorrect date format, should be YYYY/MM/DD")
            continue


def LatestVersionQuestion():
    global latestversion
    while True:
        try:
            latestversion = input("Latest Version (Example: 1.2): ")
            if latestversion == '':
                print("Please enter the latest released version number for your package.")
                continue
            elif latestversion.isalpha():
                print("Please enter a number not a string.")
                continue
            else:
                break
        except ValueError:
            break


def LatestReleasedDateQuestion():
    global latestreleasedate
    while True:
        try:
            latestreleasedate = input("Latest Version Release Date (YYYY/MM/DD): ")
            if latestreleasedate == '':
                print("Please enter the date your latest version of your package was released.")
                continue
            else:
                pass
            datetime.datetime.strptime(latestreleasedate, '%Y/%m/%d')
            break
        except ValueError:
            print("Incorrect date format, should be YYYY/MM/DD")
            continue


def PriceQuestion():
    global price
    while True:
        try:
            price = input("Price: ")
            if price == '':
                print("Please enter a price.")
                continue
            else:
                break
        except ValueError:
            break


def DeveloperQuestion():
    global developer
    while True:
        try:
            developer = input("Developer Name: ")
            if developer == '':
                print("Please enter a name.")
                continue
            else:
                break
        except ValueError:
            break


def SupportURLQuestion():
    global supporturl
    supporturl = input("Support URL: ")
