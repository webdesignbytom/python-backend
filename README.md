# python-backend

All information and shortcuts for Python Language.

## Installation

1. Install Python for OS
2. Install django for OS
3. Use .py files to write
4. Run files using the > icon and they appear in the terminal

### Installing python
1. download python
2. cmd - create directory for python to be installed `mkdir pyver`
3. use custom install on python - comes with pip
   1. tick install for all users
   2. set install location to created directory plus `/py<versionNumber>`
4. once installed go to cmd and cd to project folder/create directory
5. install the environment `c:\User\Tom\pyver\<versionNumber>\python -m venv projectName`
6. a folder projectName will be created
7. `<projectName>\Scripts\activate` activate the environment
8. create a file in cmd `type nul > script.py`
9. `echo var1 = 10 >> script.py` add code in cmd
   
### Aditionals

1. Python shell
2. PIP - get modules from online packages
3. django - a web frame work for building with python `pip install django`
4. flask - framework

- `pip install <package-name> --user` packages error free
- install virtual environment using pip `py -m pip install --user virtualenv`

## Start new environment

Environments are a sandbox where you can install packages and test code.

- Start new file
- Open terminal to cmd
- `python -m venv projectName` wait for files to install
- -new environment `py -m venv projectName`
- To activate your virtual environment `.\projectName\Scripts\activate` - You’ll see “(myproject)” next to the command prompt.
- Deactivate your virtual environment `deactivate`
- cntr shift p - set interpreter

## Project dependencies
- numpy - math module `pip install numpy`
## Conda commands
- 
## Pip commands
- `pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U` update all 
- `pip list --outdated --format=freeze | findstr -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U` update all 
- `pip freeze --local | Select-String -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U` ## cmd update
## Flask commands
- `pip install flask`
- `pip install flask-login`
- `pip install flask-sqlalchemy`
### Data notes
- file modes 'w (write)', 'r (read)', 'a (append)'
- a will write to the end of the file or create a new file
- `__init__.py` makes website folder a package

### Extensions
- jinja - html python injection script