#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2017, Alf Gaida <agaida@siduction.org>
#
#   This module is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This module is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this module. If not, see <http://www.gnu.org/licenses/>.

import libcalamares

def run():
    """ Remove not needed virt packages in target system.

    :return:
    """

    libcalamares.utils.target_env_call(['/bin/sh', '-c', 'fllremovevirt'])
