# Copyright (C) 2005 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Gaupol is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gaupol; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


"""About dialog to display application information."""


#import locale

try:
    from psyco.classes import *
except ImportError:
    pass

import gtk

from gaupol.constants import VERSION
from gaupol.gui.util import gui


NAME         = 'Gaupol'
COPYRIGHT    = u'Copyright \xa9 2005 Osmo Salomaa'
COMMENTS     = _('Subtitle editor')
WEBSITE      = 'http://home.gna.org/gaupol/'
AUTHORS      = ['Osmo Salomaa <otsaloma@cc.hut.fi>']
#DOCUMENTERS = []
#ARTISTS     = []
#TRANSLATORS = {'fi_FI': 'Osmo Salomaa <otsaloma@cc.hut.fi>'}
LICENSE      = \
_('''Gaupol is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

Gaupol is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Gaupol; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA''')


class AboutDialog(gtk.AboutDialog):

    """About dialog to display application information."""

    def __init__(self, parent):

        gtk.AboutDialog.__init__(self)

        self.set_transient_for(parent)

        self.set_name(NAME)
        self.set_version(VERSION)
        self.set_copyright(COPYRIGHT)
        self.set_comments(COMMENTS)
        self.set_license(LICENSE)

        gtk.about_dialog_set_url_hook(self._on_url_clicked)
        self.set_website_label(WEBSITE)
        
        self.set_authors(AUTHORS)
        #self.set_documenters(DOCUMENTERS)
        #self.set_artists(ARTISTS)

        #lang = locale.getdefaultlocale()[0]

        #try:
        #    self.set_translator_credits(TRANSLATORS[lang])
        #except KeyError:
        #    pass
        
    def _on_url_clicked(self, *args):
        """Open website in browser when user clicks on URL."""

        gui.open_url(WEBSITE)