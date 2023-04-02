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

import glob
import libcalamares
import os
import subprocess

def run():
    """ Remove some fll leftovers - thats what the fll-installer would do.

    :return:
    """

    # set root_mount_point
    user = libcalamares.globalstorage.value("username")
    instHome ='/home/%s' % (user)
    # home of user on live media
    # local LIVEHOME="/home/${DEFAULT_USER}" --> /home/siducer
    liveHome = '/home/siducer'
    chroot = libcalamares.globalstorage.value("rootMountPoint")
    path = chroot + instHome

    if not os.path.isdir(path):
        # move livehome --> insthome
        libcalamares.utils.target_env_call(['/bin/mv', '%s' % (liveHome), '%s' % (instHome)])

        # fix /home/user paths in various config files
        command = '/usr/bin/find %s -type f -exec /bin/sed -i \'s|%s|%s|g\' {} \;' % (instHome, liveHome, instHome)
        libcalamares.utils.target_env_call(['/bin/sh', '-c', '%s' % command])

        # remove unwanted files
        # ${TARGET_MNT_POINT}${INSTHOME}/Desktop/${FLL_DISTRO_NAME}.desktop
        unwanted = os.path.join( instHome, 'Desktop/calamares.desktop' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/Desktop/chtoot-helper.desktop
        unwanted = os.path.join( instHome, 'Desktop/chroot-helper.desktop' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.config/autostart/${FLL_DISTRO_NAME}.desktop
        # OUTDATED - RELEASE-NOTES???
        unwanted = os.path.join( instHome, '.config/autostart/siduction.desktop' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.gitconfig
        unwanted = os.path.join( instHome, '.gitconfig' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.hushlogin
        unwanted = os.path.join( instHome, '.hushlogin' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/SingletonLock
        unwanted = os.path.join( instHome, '.config/chromium/SingletonLock' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/Local State
        unwanted = os.path.join( instHome, '.config/chromium/Local State' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.config/chromium/First Run
        unwanted = os.path.join( instHome, '.config/chromium/First Run' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.config/emaildefaults
        unwanted = os.path.join( instHome, '.config/emaildefaults' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.config/emailidentities
        unwanted = os.path.join( instHome, '.config/emailidentities' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}/root/.hushlogin
        unwanted = '/root/.hushlogin'
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # remove content of some dirs
        unwanted = os.path.join( instHome, '.cache' )
        libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s'  % (unwanted)])

        unwanted = os.path.join( instHome, '.local/state' )
        libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s'  % (unwanted)])

        # revert sudo workarounds
        unwanted = os.path.join( instHome, '.config/kdesurc' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.kde/share/config/kdesurc
        unwanted = os.path.join( instHome, '.kde/share/config/kdesurc' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.kde/share/apps/konsole/sumc.desktop
        unwanted = os.path.join( instHome, '.kde/share/apps/konsole/sumc.desktop' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.kde/share/apps/konsole/su.desktop
        unwanted = os.path.join( instHome, '.kde/share/apps/konsole/su.desktop' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.gconf/apps/gksu/%gconf.xml
        unwanted = os.path.join( instHome, '.gconf/apps/gksu/%gconf.xml' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # ${TARGET_MNT_POINT}${INSTHOME}/.su-to-rootrc
        unwanted = os.path.join( instHome, '.su-to-rootrc' )
        libcalamares.utils.target_env_call(['/bin/rm', '-f', '%s'  % (unwanted)])

        # revert gksu sudo mode hack
        command = 'sudo -u siducer gconftool-2 -s -t bool /apps/gksu/sudo-mode false'
        libcalamares.utils.target_env_call(['/bin/sh', '-c', '%s'  % (command)])
        command = 'sudo -u siducer gconftool-2 -s -t bool /apps/gksu/display-no-pass-info true'
        libcalamares.utils.target_env_call(['/bin/sh', '-c', '%s'  % (command)])

        # remove installer from fluxbox menu // we dont check
        wanted = os.path.join( instHome, '.bashrc' )
        command = '/bin/sed -i \'s|\(.*sudo.*\)||\' %s'  % (wanted)
        libcalamares.utils.target_env_call(['/bin/sh', '-c', '%s'  % (command)])

        # We don't check existence, -p handles that
        wanted = os.path.join( instHome, '.config/autostart' )
        libcalamares.utils.target_env_call(['/bin/mkdir', '-p', '%s'  % (wanted)])
