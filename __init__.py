#!/usr/bin/env python
# vim:fileencoding=utf-8

__license__ = 'GPL v3'
__copyright__ = '2024, Scott Stephens <stephens.js@gmail.com>'

from calibre.customize import EditBookToolPlugin

class FtfyEncodingFixerPlugin(EditBookToolPlugin):
    name = 'FTFY Encoding Fixer'
    version = (1, 0, 0)
    author = 'Scott Stephens'
    supported_platforms = ['windows', 'osx', 'linux']
    description = 'Fixes encoding and other Unicode issues in book text using ftfy.'
    minimum_calibre_version = (1, 46, 0)
