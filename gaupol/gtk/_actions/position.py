# Copyright (C) 2005-2007 Osmo Salomaa
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


"""Time and frame editing actions."""


import gtk
from gettext import gettext as _

from gaupol.gtk import conf
from gaupol.gtk.index import *
from ._action import UIMAction


class AdjustDurationsAction(UIMAction):

    """Lengthen or shorten durations."""

    action_item = (
        "adjust_durations",
        None,
        _("A_djust Durations..."),
        None,
        _("Lengthen or shorten durations"),)

    paths = ["/ui/menubar/tools/adjust_durations"]

    @classmethod
    def is_doable(cls, application, page):
        """Return True if action can be done."""

        return (page is not None)


class AdjustPositionsAction(UIMAction):

    """Adjust positions by linear two-point correction."""

    action_item = (
        "adjust_positions",
        None,
        _("_Adjust Positions..."),
        "A",
        _("Adjust positions by linear two-point correction"),)

    paths = ["/ui/menubar/tools/adjust_positions"]

    @classmethod
    def is_doable(cls, application, page):
        """Return True if action can be done."""

        if page is not None:
            return (len(page.project.times) > 1)
        return False


class ConvertFramerateAction(UIMAction):

    """Convert framerate."""

    action_item = (
        "convert_framerate",
        gtk.STOCK_CONVERT,
        _("Con_vert Framerate..."),
        None,
        _("Convert framerate"),)

    paths = ["/ui/menubar/tools/convert_framerate"]

    @classmethod
    def is_doable(cls, application, page):
        """Return True if action can be done."""

        if page is not None:
            return (page.project.main_file is not None)
        return False


class PreviewAction(UIMAction):

    """Preview from selected position with a video player."""

    action_item = (
        "preview",
        gtk.STOCK_MEDIA_PLAY,
        _("_Preview"),
        "P",
        _("Preview from selected position with a video player"),)

    paths = [
        "/ui/menubar/tools/preview",
        "/ui/main_toolbar/preview",
        "/ui/view_popup/preview"]

    @classmethod
    def is_doable(cls, application, page):
        """Return True if action can be done."""

        try:
            assert page is not None
            assert page.project.video_path is not None
            if not conf.preview.use_predefined:
                assert conf.preview.custom_command
            if page.view.get_focus()[1] == TTXT:
                return (page.project.tran_file is not None)
            return (page.project.main_file is not None)
        except AssertionError:
            return False


class ShiftPositionsAction(UIMAction):

    """Make subtitles appear earlier or later."""

    action_item = (
        "shift_positions",
        None,
        _("_Shift Positions..."),
        "H",
        _("Make subtitles appear earlier or later"),)

    paths = ["/ui/menubar/tools/shift_positions"]

    @classmethod
    def is_doable(cls, application, page):
        """Return True if action can be done."""

        return (page is not None)
