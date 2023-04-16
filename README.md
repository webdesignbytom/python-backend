# python-backend

All information and shortcuts for Python Language.

## Installation

1. Install Python for OS
2. Install django for OS
3. Use .py files to write
4. Run files using the > icon and they appear in the terminal

### Aditionals

1. Python shell
2. PIP - get modules from online packages
3. django - a web frame work for building with python `pip install django`
4. flask - framework

- `pip install <package-name> --user` packages error free
- install virtual environment using pip `py -m pip install --user virtualenv`

## Start new environment

- Start new file
- Open terminal to cmd
- `python -m venv projectName` wait for files to install
- -new environment `py -m venv projectName`
- To activate your virtual environment `.\projectName\Scripts\activate` - You’ll see “(myproject)” next to the command prompt.
- Deactivate your virtual environment `deactivate`
- cntr shift p - set interpreter

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