# Virtual Environments and Python Packages

## Installing with pip
The PyPA recommended tool for installing Python packages; A Python-specific package manager.
[Documentation](https://pip.pypa.io/){:target="_blank"}

## What is an Environment?
 A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.
A virtual environment is a directory tree which contains Python executable files and other files which indicate that it is a virtual environment.

Common installation tools such as `Setuptools` and pip work as expected with virtual environments. In other words, when a virtual environment is active, they install Python packages into the virtual environment without needing to be told to do so explicitly.

When a virtual environment is active (i.e., the virtual environment’s Python interpreter is running), the attributes `sys.prefix` and `sys.exec_prefix` point to the base directory of the virtual environment, whereas `sys.base_prefix` and `sys.base_exec_prefix` point to the non-virtual environment Python installation which was used to create the virtual environment. If a virtual environment is not active, then `sys.prefix` is the same as `sys.base_prefix` and `sys.exec_prefix` is the same as `sys.base_exec_prefix` (they all point to a non-virtual environment Python installation).

When a virtual environment is active, any options that change the installation path will be ignored from all `distutils` configuration files to prevent projects being inadvertently installed outside of the virtual environment.

When working in a command shell, users can make a virtual environment active by running an activate script in the virtual environment’s executables directory (the precise filename is shell-dependent), which prepends the virtual environment’s directory for executables to the `PATH` environment variable for the running shell. There should be no need in other circumstances to activate a virtual environment—scripts installed into virtual environments have a “shebang” line which points to the virtual environment’s Python interpreter. This means that the script will run with that interpreter regardless of the value of `PATH`. On Windows, “shebang” line processing is supported if you have the Python Launcher for Windows installed (this was added to Python in 3.3 - see PEP 397 for more details). Thus, double-clicking an installed script in a Windows Explorer window should run the script with the correct interpreter without there needing to be any reference to its virtual environment in `PATH`.

## PipEnv (as opposed to the built-in `venv` with Python3)
See: [PipEnv: Python Dev Workflow for Humans](https://docs.pipenv.org/){:target="_blank"}

**Pipenv** — the tool for managing application dependencies from [PyPA](https://www.pypa.io/en/latest/){:target="_blank"}, free (as in freedom).

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. _Windows is a first-class citizen, in our world_.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your `Pipfile` as you install/uninstall packages. It also generates the ever-important `Pipfile.lock`, which is used to produce deterministic builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to setup a working environment. For the distinction between libraries and applications and the usage of `setup.py` vs `Pipfile` to define dependencies, see [☤ Pipfile vs setup.py](https://docs.pipenv.org/advanced/#pipfile-vs-setuppy){:target="_blank"}.

## Working with Virtual Environments
*Note: See [Python3 Virtual Environment Docs](https://docs.python.org/3/library/venv.html#creating-virtual-environments){:target="_blank"} for Windows CLI Instructions*

#### Creating a new Virtual Environment
1. _Navigate to a new project directory where you will create a virtual environment._
```sh
$ pipenv shell
Creating a virtualenv for this project…
Using /usr/local/Cellar/pipenv/2018.5.18/libexec/bin/python3.6 (3.6.5) to create virtualenv…
⠋Already using interpreter /usr/local/Cellar/pipenv/2018.5.18/libexec/bin/python3.6
Using real prefix '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/username/.local/share/virtualenvs/demo_env-eGvuWVvz/bin/python3.6
Also creating executable in /Users/username/.local/share/virtualenvs/demo_env-eGvuWVvz/bin/python
Installing setuptools, pip, wheel...done.

Virtualenv location: /Users/username/.local/share/virtualenvs/demo_env-eGvuWVvz
Creating a Pipfile for this project…
Spawning environment shell (/bin/bash). Use 'exit' to leave.
. /Users/username/.local/share/virtualenvs/demo_env-eGvuWVvz/bin/activate
~/Codefellows/demo_env
$ . /Users/username/.local/share/virtualenvs/demo_env-eGvuWVvz/bin/activate
(demo_env-eGvuWVvz) ~/Codefellows/demo_env $
# Notice that PipEnv has created the environment (demo_env-eGvuWVvz) and activated it for visually as part of the prompt
```
#### Exiting a Virtual Environment
_Note: must have an active virtual environment_
```sh
(demo_env-eGvuWVvz) ~/Codefellows/demo_env $ exit
~/Codefellows/demo_env $
```

_Note: it's okay if you don't see the exact same output when creating your environments. It may vary slightly, but you should see something similar._
