# Jazzmin Tm Edition

Jazzmin TM Edition is a modification of the popular Django admin panel Jazzmin, with added support for the Turkmen language, an updated look, and a feature that displays how many times you've logged into the site.

## Main functions

- **Turkmen language support:** Fully localized interface for Turkmen users.
- **Updated appearance:** Modern and responsive interface design.
- **Login monitoring** A dashboard widget that shows how many times login actions have been performed on the site.

## Installation

To use Jazzmin Tm Edition in your Django project, follow these steps:
pip install JazzminTM

## Instructions

1. Open the 'settings.py' file in your project.
2. Find there: INSTALLED_APPS. and insert 'JazzminTM' into the first line:

``
  INSTALLED_APPS = [
    'JazzminTM'
   ... other applications
``

]
4. If you want to set the Turkmen language, then in the same 'setting.py' find: LANGUAGE_CODE. and write: LANGUAGE_CODE = 'tk' # set the Turkmen language.



