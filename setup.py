from cx_Freeze import setup, Executable

base = None

executables = [Executable('Bobo Counter.py', base=base)]

packages = ['idna']
options = {
    'build.exe': {
        'packages':packages,
    },
}

setup (
    name = 'Bobo Counter',
    options = options,
    version = '1.0.0',
    description = 'Bobo Counter',
    executables = executables
)
