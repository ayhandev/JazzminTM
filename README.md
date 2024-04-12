# Jazzmin Tm Edition

Jazzmin Tm Edition — This is a modification of the popular Django Jazzmin admin panel with the addition of support for the Turkmen language, an updated appearance and a function to display memory usage. This is a modification of the popular Django Jazzmin admin theme with the addition of support for the Turkmen language, an updated appearance and a function to display memory usage.

## Main functions

- **Turkmen language support:** Fully localized interface for Turkmen users.
- **Updated appearance:** Modern and responsive interface design.
- **Memory monitoring:** A widget on the control panel that shows how many percent of the device’s RAM is full.

## Installation

To use Jazzmin Tm Edition in your Django project, follow the steps below:

1. Install the package via git clone:
   in the terminal write git clone https://github.com/ayhandev/Jazzmin-TM-Edition.git.
2. install the original "jazzmin" into your virtual environment.
3. delete the jazzmin folder that you just installed in your virtual environment, it is located in venv/lib/python3.10(or other version)/site-packages/jazzmin.
4. after you have deleted the original jazzmin, insert the modified jazzmin in its place, and rename it 'jazzmin'.

## Instructions

1. Open the 'settings.py' file in your project.
2. Find there: INSTALLED_APPS. and insert 'jazzmin' into the first line:
  INSTALLED_APPS = [
    'jazzmin'
   ... other applications
]
3. If you want to set the Turkmen language, then in the same 'setting.py' find: LANGUAGE_CODE. and write: LANGUAGE_CODE = 'tk' # set the Turkmen language.
