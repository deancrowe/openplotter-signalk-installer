#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2019 by sailoog <https://github.com/sailoog/openplotter>
#                     e-sailing <https://github.com/e-sailing/openplotter>
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.
from openplotterSettings import platform

class Ports:
	def __init__(self,conf):
		self.usedPorts=[]
		platform2 = platform.Platform()

		if platform2.skPort:
			self.usedPorts=[{'description':_('Signal K - Server'), 'type':'TCP', 'address':'localhost', 'port':platform2.skPort, 'direction':'out'},
			{'description':_('Signal K - NMEA 0183 output'), 'type':'TCP', 'address':'localhost', 'port':'10110', 'direction':'out'}]


