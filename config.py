# Developers Information - This information makes it a ease when creating things like a Packages file because you won't need to enter your name, email, or homepage the script will use the info you enter here for that.
Author = "Dev1337 <dev1337@email.com>" # Name of the auther who developed the package. Eg: Brian Leek <brianleek2016@gmail.com>
Maintainer = "Dev1337 <dev1337@email.com>" # Name of the package maintainer. Eg: Brian Leek <brianleek2016@gmail.com>
Homepage = "https://dev1137website.com/" # Package developers website/homepage. Eg: https://brianleek.me/. Trending slash "/" at the end of url is required!
RepoURLPath = "repo/" # This is not the same as "RepoPath". This is only if you want the script to know where your repo is hosted by using the homepage url and add RepoURLPath to the end.

# Package Information - This information will be used in inputs where nothing is typed.
PackageDepends = "" # List of package depends that will be used when creating Packages or control files. You can choose to addon to the list when that part of the script is ran.
PackageSection = "Tweaks" # Default to use in package section input. To use it just press enter whenever the question comes up.
PackageVersion = "1.0" # Default package version to be used if nothing is entered in the version input.

RepoSuite = "stable" # Default repo suite to be used if nothing is entered in the repo suite input.
RepoVersion = "1.0" # Default package version to be used if nothing is entered in the version input.
RepoCodeName = "ios" # Default repo codename to be used if nothing is entered in the codename input.
RepoComponents = "main" # Default repo components to be used if nothing is entered in the roei components input.
RepoArchitecture = "iphoneos-arm" # Default repo architecture to be used if nothing is entered in the rpeo architecture input.

# Save Paths - These paths are used to save files that may be generated or files that might need to be used later.
DebsPath = "debs/" # Path to where you want the script to search for debs files you uploaded. Make sure to include the trending slash "/" at the end of your path.
ControlPath = "DEBIAN/" # Path to where you want the script to save the control file. Make sure to include the trending slash "/" at the end of your path.
RepoPath = "repo/" # Path which to save a repo after it is created.
RepoTemplatePath = "templates/repos/" # Path where the repo templates are stored.
DefaultRepoTemplate = "default/"
TemplatesPath = "templates/depictions/" # Path to the templates folder. Make sure to include the trending slash "/" at the end of your path.
SaveDepictionPath = "depictions/user/templates/" # Path where the depition file will be saved to once it's created. Make sure to include the trending slash "/" at the end of your path or it wont save the depiction file in the right place.

# Display Options - Choose to display items within the script or not.
ShowWelcomeText = True # Show welcome text each time the script runs. True or False.
ShowDepictionGenText = True # Show depiction generater text each time the depiction gen script is ran. True or False.

# .md Files - You probably won't need to edit theses but this is just the paths to the .md files that stores text to be displayed later.
WelcomeTextFile = "markdown/welcome.md" # File that stores the welcome text that will be displayed.
DepictionGenTextFile = "markdown/depiction_gen_wel.md" # File that stores the text that will be displayed when the depiction gen script is ran.
DocsTextFile = "markdown/docs.md" # File that stores the text for the docs that will be displayed.
