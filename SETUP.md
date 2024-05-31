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

### Setup the initial Python Virtual Environment and installing Jupyter

If you've used python and jupyter before, feel free to use your own method to get a working version of jupyter, directly installing, using andaconda or using a virtualenv as below.

If you work on multiple Python projects, you'll likely have encountered Python virtual environments (venvs) and/or conda. You can think of these as ways to have a separate Python "install" or more accurately, an environment for each project. There are numerous reasons to use a venv or conda such as keeping different versions of a library separate. However, my favorite reason is reproducibility.

If you move to another computer, High-Performance Computing (HPC) system, or have a collaborator working with you, you'll need to know which versions of which libraries are necessary to install to make your project work. Venvs help solve this problem with requirements files. Conda can also save its environment. For this example, we'll use venvs and pip as they are lightweight and require less to install. That being said, Conda is a great option too.

Let's start by creating a venv, assuming you have a fairly recent version of Python 3 installed, everything you need should already be included.

```bash
python3 -m venv env #create a venv called env

ls #see the env folder
```

To actually use the venv, you'll need to know some particular commands. These aren't too complicated and eventually, you'll remember them. There are helper scripts available to simplify this process, and Conda is also a bit simpler. We'll do it in a generic, lightweight way:

```bash
source env/bin/activate
```

Notice the leading `env` on your prompt.

![Activated venv](docs/images/activated_env.png "Activated Virtual Environment")


#### Installing and starting Jupyter

Now we can install Jupyter which we'll be using for most of the session.

in your terminal
```bash
pip install jupyter
```

If that doesn't work, you might need to specify ```pip3``` instead.

Now we can start Jupyter, though depending on your operating system, you might need to deactivate and reactivate your virtual environment first

```
deactivate

#then
source env/bin/activate # just as before
```

To start Jupyter

```
jupyter-lab
```

This should open a tab in your browser with Jupyter, otherwise you might need to copy paste the line from the terminal, it'll look something like this

![jupyter start text](docs/images/Jupyter-start.png "jupyter start text")

#### Extra dependancies

After installing Jupyter, you'll need to install pillow - a library we'll be using to do image manipulation

```
pip install pillow
```

#### Reusing your venv

If you close your terminal window or otherwise deactivate your python virtaul enviroment, you'll need to reactivate it.  Just follow the steps when activated it before.  In your project directory:

```bash
source env/bin/activate
```

Notice the leading `env` on your prompt.

![Activated venv](docs/images/activated_env.png "Activated Virtual Environment")
