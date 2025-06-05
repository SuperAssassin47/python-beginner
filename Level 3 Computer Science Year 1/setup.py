from cx_Freeze import setup, Executable

base = 'Win32GUI'

executables = [Executable('U10 App.py', base=base)]

packages = ['idna']
options = {
    'build.exe': {
        'packages':packages,
        'include_files':'python39.dll'
    },
}

setup (
    name = 'AMAP Directions',
    options = options,
    version = '1.0.0',
    description = 'AMAP Shopping Centre',
    executables =[Executable('U10 App.py')]
)
