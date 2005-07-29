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


"""Subtitle file writer."""


import logging
import os
import random
import shutil

try:
    from psyco.classes import *
except ImportError:
    pass

from gaupol.lib.constants import SHOW, HIDE, DURN, ORIG, TRAN
from gaupol.lib.delegates.delegate import Delegate
from gaupol.lib.formats.all import *
from gaupol.lib.formats.tags import TagConverter


logger = logging.getLogger()


class FileWriter(Delegate):
    
    """Subtitle file writer."""
    
    def _create_temporary_backup_file(self, path, bak_path):
        """
        Create a temporary backup file before writing.

        Return: success (True or False)
        """
        try:
            shutil.copyfile(path, bak_path)
            return True
        except IOError, (errno, detail):
            logger.warning( \
                'Failed to create temporary backup file "%s": %s.' \
                % (bak_path, detail) \
            )
            return False

    def _remove_failed_file(self, path):
        """Remove empty file after failing writing."""
        
        try:
            os.remove(path)
        except OSError, (errno, detail):
            logger.warning( \
                'Failed to remove file "%s" after failing to write it: %s.' \
                % (path, detail) \
            )
        
    def _remove_temporary_backup_file(self, bak_path):
        """Remove temporary backup file after successful writing."""
        
        try:
            os.remove(bak_path)
        except OSError, (errno, detail):
            logger.warning( \
                'Failed to remove temporary backup file "%s": %s.' \
                % (bak_path, detail) \
            )

    def _restore_original_file(self, path, bak_path):
        """Restore file from temporary backup after failing writing."""
        
        try:
            shutil.move(bak_path, path)
        except IOError, (errno, detail):
            logger.warning( \
                'Failed to restore file "%s" from temporary backup file "%s" after failing to write it: %s.' \
                % (path, bak_path, detail) \
            )
            
    def _write_file(self, text_part, keep_changes, path, format, encoding,
                    newlines):
        """
        Write a subtitle file.
        
        text_part: "original" or "translation"
        keep_changes: True or False

        Raise IOError if reading fails.
        Raise UnicodeError if encoding fails.
        """
        text_parts = ['original', 'translation']
        col = text_parts.index(text_part)
        
        files = [self.main_file, self.tran_file]
        cur_file = files[col]
        
        # Create a copy of texts, because possible tag conversions might be
        # only temporary.
        new_texts = self.texts[:]

        # Convert tags if saving in different format.
        if cur_file is not None     and \
           format   is not None     and \
           cur_file.FORMAT != format:
            
            conv = TagConverter(cur_file.FORMAT, format)
            for i in range(len(new_texts)):
                new_texts[i][col] = conv.convert_tags(new_texts[i][col])

        if path     is None or \
           format   is None or \
           encoding is None or \
           newlines is None :
           
            sub_file = cur_file
            path     = cur_file.path
            
        else:
            sub_file = eval(format)(path, encoding, newlines)

        shows = []
        hides = []
        texts = []

        if sub_file.MODE == 'time':
            for i in range(len(self.times)):
                shows.append(self.times[i][SHOW])
                hides.append(self.times[i][HIDE])
                texts.append(new_texts[i][col])

        elif sub_file.MODE == 'frame':
            for i in range(len(self.times)):
                shows.append(self.frames[i][SHOW])
                hides.append(self.frames[i][HIDE])
                texts.append(new_texts[i][col])
                
        # If the file to be written already exists, a backup copy of it is
        # be made in case writing fails. The backup file should be temporary,
        # unharmful and invisible to the user.
        #
        # If the file does not exist and writing fails, the result usually is
        # an empty file which is removed afterwards.

        file_existed = os.path.isfile(path)

        if file_existed:
            while True:
                number = int(random.random() * 1000000)
                bak_path = path + '~gaupol-%d' % number
                if not os.path.isfile(bak_path):
                    break
            bak_success = self._create_temporary_backup_file(path, bak_path)

        write_success = False
        try:
            sub_file.write(shows, hides, texts)
            write_success = True
        finally:
            if file_existed and bak_success and (not write_success):
                self._restore_original_file(path, bak_path)                
            elif (not file_existed) and (not write_success):
                self._remove_failed_file(path)
            elif file_existed and bak_success and write_success:
                self._remove_temporary_backup_file(bak_path)
                
        # After successful writing, instance variables can be set.
        if keep_changes:
            if text_part == 'original':
                self.main_file = sub_file
            elif text_part == 'translation':
                self.tran_file = sub_file
            self.texts = new_texts

    def write_main_file(
        self, keep_changes=True,
        path=None, format=None, encoding=None, newlines=None
    ):
        """
        Write times/frames and original texts to main file.
        
        Raise IOError if reading fails.
        Raise UnicodeError if encoding fails.
        """
        self._write_file(
           'original', keep_changes, path, format, encoding, newlines
        )

    def write_translation_file(
        self, keep_changes=True,
        path=None, format=None, encoding=None, newlines=None
    ):
        """
        Write times/frames and translated texts to translation file.
        
        Raise IOError if reading fails.
        Raise UnicodeError if encoding fails.
        """
        self._write_file(
           'translation', keep_changes, path, format, encoding, newlines
        )