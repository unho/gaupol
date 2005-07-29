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


"""File closer to close documents and quit application."""

try:
    from psyco.classes import *
except ImportError:
    pass

import gtk

from gaupol.gui.delegates.delegate import Delegate
from gaupol.gui.dialogs.warning import CloseMainDocumentWarningDialog
from gaupol.gui.dialogs.warning import CloseTranslationDocumentWarningDialog
from gaupol.gui.multiclose import MultiCloseWarningDialog
from gaupol.gui.project import Project
from gaupol.gui.util import gui


class FileCloser(Delegate):

    """File closer to close documents and quit application."""

    def _close_all_projects(self):
        """
        Close all projects.
        
        Return: False if cancelled, otherwise True
        """
        unsaved_count = 0

        for project in self.projects:

            if project.main_changed:
                unsaved_prj = project
                unsaved_count += 1

            if project.tran_changed:
                unsaved_prj = project
                unsaved_count += 1

            if unsaved_count > 1:
                break

        if unsaved_count == 1:
            success = self._close_project(unsaved_prj)
            if not success:
                return False

        elif unsaved_count > 1:
            success = self._close_multiple_documents(self.projects)
            if not success:
                return False

        self.projects = []
        
        while self.notebook.get_current_page() > -1:
            self.notebook.remove_page(0)

        return True

    def _close_multiple_documents(self, projects):
        """
        Close all documents of given projects.
        
        Return: False is cancelled, otherwise True
        """
        dialog = MultiCloseWarningDialog(self.window, projects)
        response = dialog.run()

        # "Cancel" or dialog close button clicked.
        if response != gtk.RESPONSE_YES and response != gtk.RESPONSE_NO:
            dialog.destroy()
            return False

        # "Close without saving" clicked.
        elif response == gtk.RESPONSE_NO:
            dialog.destroy()
            return True
            
        # "Save" clicked.
        main_prjs = dialog.get_main_projects_to_save()
        tran_prjs = dialog.get_translation_projects_to_save()
        dialog.destroy()

        gui.set_cursor_busy(self.window)

        for project in main_prjs:
            self.save_main_document(project)

        for project in tran_prjs:
            self.save_translation_document(project)

        gui.set_cursor_normal(self.window)

        return True

    def _close_project(self, project):
        """
        Close project after asking for confirmation.
        
        Return: False if cancelled, otherwise True
        """
        # Main document close dialog.
        if project.main_changed and not project.tran_changed:

            basename = project.get_main_basename()
            
            dialog = CloseMainDocumentWarningDialog(self.window, basename)
            response = dialog.run()
            dialog.destroy()
            
            if response != gtk.RESPONSE_YES and response != gtk.RESPONSE_NO:
                return False
            elif response == gtk.RESPONSE_YES:
                success = self.save_main_document(project)
                if not success:
                    return False
        
        # Translation document close dialog.
        elif not project.main_changed and project.tran_changed:
        
            basename = project.get_translation_basename()
            
            dialog = CloseTranslationDocumentWarningDialog(self.window,
                                                           basename)
            response = dialog.run()
            dialog.destroy()
            
            if response != gtk.RESPONSE_YES and response != gtk.RESPONSE_NO:
                return False
            elif response == gtk.RESPONSE_YES:
                success = self.save_translation_document(project)
                if not success:
                    return False

        # Multidocument close dialog.
        elif project.main_changed and project.tran_changed:

            success = self._close_multiple_documents([project])
            if not success:
                return False
        
        notebook_index = self.notebook.get_current_page()
        project_index  = self.projects.index(project)

        # Notebook widget doesn't seem to be able to handle post page close
        # page switching smoothly. So, as a workaround, we'll switch to next
        # page if we're closing the current page.
        if notebook_index == project_index:
            self.notebook.next_page()
        
        self.projects.remove(project)
        self.notebook.remove_page(project_index)

        return True

    def on_close_activated(self, *args):
        """Close project after asking for confirmation."""
        
        project = self.get_current_project()
        success = self._close_project(project)

        if success:
            self.set_sensitivities()

    def on_close_all_activated(self, *args):
        """Close all currently open projects."""
        
        success = self._close_all_projects()
        
        if success:
            self.set_sensitivities()

    def on_notebook_tab_close_button_clicked(self, project):
        """Close project after asking for confirmation."""

        success = self._close_project(project)

        if success:
            self.set_sensitivities()

    def on_quit_activated(self, *args):
        """Quit application."""

        success = self._close_all_projects()
        if not success:
            return

        if not self.config.getboolean('main_window', 'maximized'):

            size = self.window.get_size()
            self.config.setlistint('main_window', 'size', size)

            position = self.window.get_position()
            self.config.setlistint('main_window', 'position', position)

        self.config.write_to_file()

        gtk.main_quit()

    def on_window_delete_event(self, *args):
        """Quit application."""
        
        self.on_quit_activated()

        # Return True to stop other handlers.
        return True