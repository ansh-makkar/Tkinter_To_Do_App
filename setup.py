import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [Executable("To_Do_app.py", base=base)]

options = {
    'build_exe': {
        'packages': [],
        'include_files': []
    },
}

setup(
    name="test",
    version="1.0",
    description="Description of your app",
    options=options,
    executables=executables
)

# To build the Exe-file for To_Do_App :-
#     1: Install ("pip install cx_Freeze")
#     2: In Terminal Enter ("python setup.py build")
