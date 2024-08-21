#!/usr/bin/env python
# vim:fileencoding=utf-8

__license__ = 'GPL v3'
__copyright__ = '2024, Scott Stephens <stephens.js@gmail.com>'

import os
import sys
dir_name = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_name + "/" + "deps")

# The base class that all tools must inherit from
from calibre.gui2.tweak_book.plugin import Tool
from calibre.ebooks.oeb.polish.container import OEB_DOCS
from qt.core import QAction
import ftfy

class FixText(Tool):
    name = 'fix-text'

    allowed_in_toolbar = True

    allowed_in_menu = True

    def create_action(self, for_toolbar=True):
        ac = QAction(get_icons('images/fix-encoding.png'), 'FTFY Fix Text', self.gui)
        ac.triggered.connect(self.fix_text)
        return ac
    
    def fix_text(self):
        self.boss.add_savepoint('Before: FTFY Fix Text')
        container = self.current_container

        for name, media_type in container.mime_map.items():
            if media_type in OEB_DOCS:

                raw = container.raw_data(name)
                fixed = ftfy.fix_text(raw)

                file = container.open(name, "w")
                rc = file.write(fixed)
                file.close()

                # parsed = container.parsed(name)
                # container.dirty(name)
        self.boss.apply_container_update_to_gui(mark_as_modified=True)