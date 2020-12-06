# IOS Repo Utilities - 0.2 BETA
**IOS Repo Utilities** provides a few tools to help IOS jailbreak developers who run a repo or for people looking to create a repo. Want a create a "Packages" file, then compress it so its ready to use instantly? Well, create a new folder called "debs", copy your .deb files there and run the script. Want to create a whole repo without messing with files? Now you can, run the script and choose to use a template or not and the script will walk you through the rest, like creating a "Release" and "Packages" files, etc. You can even create depictions for [Sileo](https://getsileo.app/).

![IOS Repo Utilities](https://brianleek.me/images/iosrepoutilities.png)

## Installation

To setup **IOS Repo Utilities** you should run **setup.sh** and that will install all needed dependencies to run the script and also allow you to setup the needed files. The script can still run without these files at times and if it does some functions of the script might be broke or don't work at all so keep that in mind. After the script is setup all you need to do is run **main_app.py**.

You can also install the dependencies using the package manager [pip](https://pip.pypa.io/en/stable/) to install the `requirements.txt` file. I recommend creating a virtual environment then installing the stuff in the `requirements.txt` by running the command below.

```
pip install -r requirements.txt
```

## Usage

To run the script run the following commend:

```
python main_app.py
```

## To Do
 - Package DEB files
 - Deploy repo to GitHub
 - Add more documentation
 - Add more templates
 - Generate web depictions
 - DEB to ZIP
 - ZIP to DEB

## Contributing
Thanks to everybody who has contributed to IOS Repo Utilities so far!
  - Brian Leek - Developer (https://brianleek.me/)
  - Shuga - Contributed Code (https://shuga.co/)
    - Provided setup.sh file along with util/gpg.batchgen.
    -Provided some tips and recommendations.
  - @KatriCameron - Contributed Code (https://twitter.com/KatriCameron)
    - Helped with adding GPG signing.
    - Helped with some questions I had.

If you would like to contribute to this project in any way, feel free too. You will be credited for any work you do. Please make sure to test your code before submitting it. Thanks!
