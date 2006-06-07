# Copyright (C) 2005 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# Gaupol is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaupol; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA 02110-1301, USA.


"""Support and information."""


try:
    from psyco.classes import *
except ImportError:
    pass

from gettext import gettext as _
import re

import gtk

from gaupol.base.error        import TimeoutError
from gaupol.base.util         import wwwlib
from gaupol.gtk.delegate      import Delegate, UIMAction
from gaupol.gtk.dialog.about import AboutDialog
from gaupol.gtk.util          import gtklib
from gaupol                   import __version__


re_version = re.compile(r'^\d+\.\d+\.\d+$')

BUG_REPORT_URL = 'http://gna.org/bugs/?func=additem&group=gaupol'
DOWNLOAD_URL   = 'http://home.gna.org/gaupol/download.html'
VERSION_URL    = 'http://download.gna.org/gaupol/latest.txt'


class HelpAction(UIMAction):

    """Base class for help actions."""

    @classmethod
    def is_doable(cls, application, page):
        """Return whether action can or cannot be done."""

        return True


class CheckLatestVersionAction(HelpAction):

    """Checking latest version online."""

    uim_action_item = (
        'check_latest_version',
        None,
        _('_Check Latest Version'),
        None,
        _('Check if you have the latest version'),
        'on_check_latest_version_activated'
    )

    uim_paths = ['/ui/menubar/help/check_latest_version']


class ReportABugAction(HelpAction):

    """Reporting a bug online."""

    uim_action_item = (
        'report_a_bug',
        None,
        _('_Report A Bug'),
        None,
        _('Submit a bug report online'),
        'on_report_a_bug_activated'
    )

    uim_paths = ['/ui/menubar/help/report_a_bug']


class ViewAboutDialogAction(HelpAction):

    """Displaying the about dialog."""

    uim_action_item = (
        'view_about_dialog',
        gtk.STOCK_ABOUT,
        _('_About'),
        None,
        _('Information about Gaupol'),
        'on_view_about_dialog_activated'
    )

    uim_paths = ['/ui/menubar/help/about']


class VersionCheckErrorDialog(gtk.MessageDialog):

    """Dialog to inform that version check failed."""

    def __init__(self, parent, message):

        gtk.MessageDialog.__init__(
            self,
            parent,
            gtk.DIALOG_MODAL|gtk.DIALOG_DESTROY_WITH_PARENT,
            gtk.MESSAGE_ERROR,
            gtk.BUTTONS_NONE,
            _('Failed to check latest version')
        )

        self.format_secondary_text(message)
        self.add_button(_('_Go to Download Page'), gtk.RESPONSE_ACCEPT)
        self.add_button(gtk.STOCK_OK             , gtk.RESPONSE_OK    )
        self.set_default_response(gtk.RESPONSE_OK)


class VersionCheckInfoDialog(gtk.MessageDialog):

    """Dialog to inform whether user has the latest version or not."""

    def __init__(self, parent, local_version, remote_version):

        if remote_version > local_version:
            title = _('A newer version is available')
        else:
            title = _('You have the latest version')
        message = _('The latest version is %s.\nYou are using %s.') \
                  % (remote_version, local_version)

        gtk.MessageDialog.__init__(
            self,
            parent,
            gtk.DIALOG_MODAL|gtk.DIALOG_DESTROY_WITH_PARENT,
            gtk.MESSAGE_INFO,
            gtk.BUTTONS_NONE,
            title
        )

        self.format_secondary_text(message)
        self.add_button(_('_Go to Download Page'), gtk.RESPONSE_ACCEPT)
        self.add_button(gtk.STOCK_OK            , gtk.RESPONSE_OK    )
        self.set_default_response(gtk.RESPONSE_OK)


class HelpDelegate(Delegate):

    """Support and information."""

    def on_check_latest_version_activated(self, *args):
        """Check latest version online."""

        gtklib.set_cursor_busy(self.window)
        dialog = None

        # Read remote file containing latest version number.
        try:
            text = wwwlib.read_url(VERSION_URL, 15)
        except IOError, instance:
            message = _('Failed to connect to URL "%s": %s.') \
                      % (VERSION_URL, instance.args[1][1])
            dialog = VersionCheckErrorDialog(self.window, message)
        except TimeoutError:
            message = _('Connection timed out. Please try again later or '
                        'check the download page.')
            dialog = VersionCheckErrorDialog(self.window, message)

        # Show error dialog.
        if dialog is not None:
            gtklib.set_cursor_normal(self.window)
            response = dialog.run()
            dialog.destroy()
            if response == gtk.RESPONSE_ACCEPT:
                wwwlib.browse_url(DOWNLOAD_URL)
            return

        remote_version = text.strip()
        if re_version.match(remote_version):
            args = self.window, __version__, remote_version
            dialog = VersionCheckInfoDialog(*args)
        else:
            message = _('No version information found at URL "%s".') \
                      % VERSION_URL
            dialog = VersionCheckErrorDialog(self.window, message)

        # Show info or error dialog.
        gtklib.set_cursor_normal(self.window)
        response = dialog.run()
        dialog.destroy()
        if response == gtk.RESPONSE_ACCEPT:
            wwwlib.browse_url(DOWNLOAD_URL)

    def on_report_a_bug_activated(self, *args):
        """Report a bug online."""

        wwwlib.browse_url(BUG_REPORT_URL)

    def on_view_about_dialog_activated(self, *args):
        """Display the about dialog."""

        dialog = AboutDialog(self.window)
        dialog.run()
        dialog.destroy()
        gtklib.destroy_gobject(dialog)


if __name__ == '__main__':

    from gaupol.gtk.application import Application
    from gaupol.test            import Test

    class TestDialog(Test):

        def test_init(self):

            VersionCheckErrorDialog(gtk.Window(), 'test')
            VersionCheckInfoDialog(gtk.Window(), '0.0.1', '0.0.2')

    class TestHelpDelegate(Test):

        def test_all(self):

            application = Application()
            application.on_check_latest_version_activated()
            application.on_view_about_dialog_activated()
            application.window.destroy()

    TestDialog().run()
    TestHelpDelegate().run()