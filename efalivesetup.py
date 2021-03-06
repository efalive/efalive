#!/usr/bin/env python3
'''
Created on 26.08.2010

Copyright (C) 2010-2016 Kay Hannay

This file is part of efaLiveSetup.

efaLiveSetup is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
efaLiveSetup is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with efaLiveSetup.  If not, see <http://www.gnu.org/licenses/>.
'''
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import logging
import sys

from efalive.setuptool import maingui

if __name__ == "__main__":
    logging.basicConfig(filename="efaLiveSetup.log", level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s: %(message)s')
    controller = maingui.SetupController(sys.argv)
    Gtk.main()

