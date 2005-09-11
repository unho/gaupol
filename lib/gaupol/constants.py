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
# along with Gaupol; if falset, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


"""
gaupol-wide constants.

There are several common attributes that can be used in the constant classes.
CLASS_NAMES correspond to the names of classes in code. ID_NAMES are lower
case identifying names for use as e.g. parts of function names or in
configuration files. UI_NAMES are names to be used in the user interface. If
needed, UI_NAMES are gettext strings. VALUES are values of the attributes in
the correct Python data type.
"""


# Extension and Format class constants must have the same order.

class EXTENSION(object):

    VALUES = ['.sub', '.txt', '.srt']
    
    MICRODVD = 0
    MPL2     = 1
    SUBRIP   = 2

class FORMAT(object):

    CLASS_NAMES = ['MicroDVD', 'MPL2', 'SubRip']
    ID_NAMES    = ['microdvd', 'mpl2', 'subrip']
    UI_NAMES    = ['MicroDVD', 'MPL2', 'SubRip']
    
    MICRODVD = 0
    MPL2     = 1
    SUBRIP   = 2

class FRAMERATE(object):

    ID_NAMES = [  '23.976'     ,   '25'     ,   '29.97'     ]
    UI_NAMES = [_('23.976 fps'), _('25 fps'), _('29.97 fps')]
    VALUES   = [   23.976      ,    25.0    ,    29.97      ]
    
    FR_23_976 = 0
    FR_25     = 1
    FR_29_97  = 2

class MODE(object):

    ID_NAMES     = ['time', 'frame']
    
    TIME  = 0
    FRAME = 1

class NEWLINE(object):

    ID_NAMES = ['mac', 'unix', 'windows']
    UI_NAMES = ['Mac', 'Unix', 'Windows']
    VALUES   = ['\r' , '\n'  , '\r\n'   ]
    
    MAC     = 0
    UNIX    = 1
    WINDOWS = 2

class POSITION(object):

    ID_NAMES = ['above', 'below']
    
    ABOVE = 0
    BELOW = 1

class TYPE(object):

    ID_NAMES = ['main', 'translation']
    
    MAIN = 0
    TRAN = 1
