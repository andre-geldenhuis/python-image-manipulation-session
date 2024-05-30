# Setup

Before we start our session, there are a few essential tools and programs you need to set up on your computer.

### On Your Computer

Make sure your laptop or desktop is equipped with the necessary tools. If you already have a terminal, Python installation, and Git, you can skip the installations. Just use what you already have to avoid confusion. Otherwise, install what's missing.

#### Terminal

You will need a terminal for this session. Although Windows comes with a terminal, it operates differently from those in MacOS and Linux. Windows users, please set up one of the following:

##### Windows Terminal Options for This Session:

* WSL2 (Windows Subsystem for Linux) - preferred
* Git Bash

#### Python

Python is essential for our activities. MacOS and Linux users can generally use the system's default Python. For Windows, if you're using WSL2, you should be ready to go. Otherwise, download and install Python from the official Python website.

#### Git

* Windows: If using WSL2, follow the instructions for Linux. Otherwise, download from the official Git website.
* Linux: For Ubuntu/Debian, use ```sudo apt install git```. For RHEL-based systems, use ```sudo yum install git```. Users of Arch or other distros should refer to their specific documentation.
* MacOS: Use the official Git installer or brew install git if you have Homebrew installed.

#### On the Web

It’s advisable to have a GitHub account for version control throughout our session.

##### Configure Git

If you're already familiar with Git and use it regularly, you can skip this step.

Configure your Git username. You can use your real name or a pseudonym.

```
git config --global user.name "Your Name"
```

Finally, set your email address. You can use the one associated with your GitHub account or a noreply email provided by GitHub to keep your personal email private. [noreply email address for you provided by github to keep your personal email address secret](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)

```
git config --global user.email "YOUR_EMAIL"
```