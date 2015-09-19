# Run the build process by running the command 'python setupwin.py build'

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('main.py', base=base)
]

setup(name='Meadery MTG Stream Dashboard',
      version='0.1',
      description='A tool for quickly changing information on MTG streams.',
      options=options,
      executables=executables
      )
