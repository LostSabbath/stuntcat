from setuptools import setup, find_packages
from os import path
import sys

here = path.abspath(path.dirname(__file__))

name = "stuntcat"

from io import open
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

freeze_cmds = ["bdist_dmg", "bdist_msi", 'build_exe', 'bdist_mac']
if any(x in sys.argv for x in freeze_cmds):
    # https://cx-freeze.readthedocs.io/en/latest/distutils.html
    # Note: we needed to use git cx_freeze because it does not work on mac py3.7.
    #
    #     git+https://github.com/anthony-tuininga/cx_Freeze.git
    from cx_Freeze import setup, Executable

    # Dependencies are automatically detected, but it might need fine tuning.
    build_exe_options = {
        "packages": ["os", "pygame", "sys", "random", "pyscroll", "pytmx", "thorpy"],
        "excludes": ["tkinter"],
    }
    # GUI applications require a different base on Windows (the default is for a
    # console application).
    base = None
    if sys.platform == "win32":
        base = "Win32GUI"

    options = {
        "build_exe": build_exe_options
    }
    executables = [Executable("run_game.py", base=base)]
else:
    options = {}
    executables = []




setup(
    name=name,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: pygame',
        'Topic :: Games/Entertainment :: Arcade',
    ],
    license='LGPL',
    author='stuntcat team',
    author_email='stuntcat@pygame.org',
    maintainer='stuntcat team',
    maintainer_email='stuntcat@pygame.org',
    description='Stuntcat is the first pygame 2 community game.',
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    options=options,
    executables=executables,
    package_dir={name: name},
    packages=find_packages(),
    # package_data={'stuntcat': []},
    url='https://github.com/pygame/stuntcat',
    install_requires=['pygame', "pyscroll", "pytmx", "thorpy"],
    version='0.0.6',
    entry_points={
        'console_scripts': [
            '%s=%s.cli:main' % (name, name),
        ],
    },
)
