# Calibre FTFY

## About

This is a Calibre editing plugin to run the [ftfy](http://ftfy.readthedocs.org/) algorithm on book content.

It can be used to fix "mojibake" and other gitches in Unicode text, for instance turning text like this:

> â€œâ€™Sides, â€™tis only for a moon. That ainâ€™t long.â€?

Into this:

> "'Sides, 'tis only for a moon. That ain't long."

## Usage

1. Install the plugin
2. Open Calibre, and open a book for editing
3. In the plugins menu, click the "FTFY Fix Text" entry.
4. If you like the changes that have been made, save the book or save a copy. If not, you can revert changes from the Edit->Revert to... menu item.


## Development

1. Install python 3.12 or later
2. Install poetry
3. Run `poetry install`
4. Run `./vendor_deps.sh`
5. Run `calibre-debug --edit-book`
6. Most logic is in main.py

## Building a release
1. Edit version numbers in pyproject.toml, __init__.py, and bundle_release.sh
2. Run `./bundle_release.sh`
3. Upload resulting zip file manually to github
