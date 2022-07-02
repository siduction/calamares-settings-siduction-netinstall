#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2017, Alf Gaida <agaida@siduction.org>
#
import libcalamares
import os

def run():
    """ Remove some fll leftovers - thats what the fll-installer would do.

    :return:
    """

    # set root_mount_point
    root_mount_point = libcalamares.globalstorage.value("rootMountPoint")

    # via tmpfs - in mounts
    # valid - /disks/*      -- done in mount.conf
    # valid - /media/*      -- done in mount.conf
    # valid - /mnt/*        -- done in mount.conf
    # valid - /run/*        -- done in mount.conf
    # valid - /run/.*       -- done in mount.conf
    # valid - /sys/*        -- done in mount.conf
    # valid - /tmp/*        -- done in mount.conf
    # valid - /var/tmp/*    -- done in mount.conf

    # /etc/network/run/*
    path = '/etc/network/run/*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/.DCOPserver_*
    path = '/home/*/.DCOPserver_*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/.local/share/akonadi*
    path = '/home/*/.local/share/akonadi*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/.gvfs*
    path = '/home/*/.gvfs*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/.kde/cache-*
    path = '/home/*/.kde/cache-*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/.kde/socket-*
    path = '/home/*/.kde/socket-*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/.kde/tmp-*
    path = '/home/*/.kde/tmp-*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/.*uthority
    path = '/home/*/.*uthority'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/Desktop/calamares.desktop - former sidu-installer.desktop
    path = '/home/*/Desktop/calamares.desktop'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /home/*/.kaxtv*
    path = '/home/*/.kaxtv*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /lib/init/rw/*
    path = '/lib/init/rw/*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])

    # /var/cache/gdm/*
    path = '/var/cache/gdm/*'
    libcalamares.utils.target_env_call(['/bin/rm', '-rf', '%s' % (path)])
