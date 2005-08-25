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


"""Subtitle file format determiner."""


import re

try:
    from psyco.classes import *
except ImportError:
    pass

from gaupol.constants import FORMAT
from gaupol.lib.files.subfile import SubtitleFile


microdvd = r'^\{\d+\}\{\d+\}.*?$'
mpl2     = r'^\[\d+\]\[\d+\].*?$'
subrip   = r'^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\s*$'

RE_IDS = {
    FORMAT.MICRODVD: re.compile(microdvd),
    FORMAT.MPL2    : re.compile(mpl2),
    FORMAT.SUBRIP  : re.compile(subrip),
}


class FileFormatDeterminer(SubtitleFile):
    
    """Subtitle file format determiner."""
    
    def determine_file_format(self):
        """
        Determine the file format.
        
        Read file and once an identifier assiciated with a specific subtitle
        format is found, return that format.

        Raise IOError if reading fails.
        Raise UnicodeError if decoding fails.
        Raise UnknownFileFormatError if unable to detect file format.
        """
        lines = self._read_lines()

        for line in lines:
            for format, re_id in RE_IDS.items():
                if re_id.match(line) is not None:
                    return format

        raise UnknownFileFormatError

        
class UnknownFileFormatError(Exception):
    
    """Error raised when encountered a subtitle file of an unkown format."""
    
    pass