#!/usr/bin/env python
from os.path import normpath, basename, ismount
import subprocess

devices = subprocess.Popen(["lsblk | awk '{print $7}' | grep /"], shell=True, stdout=subprocess.PIPE)

print ("${voffset 4}")

for device in devices.stdout:
    device = device.rstrip().decode("utf-8")
    if device == u'/boot/efi':
        continue
    if (ismount(device)):
        if (device == u"/"):
            devicename="Root"
        else:
            devicename = basename(normpath(device)).capitalize()

        print ("${voffset -10}${offset 0}${color0}${font ConkyColors:size=15}i${font}${color}${offset 6}${voffset -10}${font Ubuntu:style=Bold:size=8}"+devicename+": ${color1}${fs_free_perc "+device+"}%${color}${font}\n")
        print ("${voffset -10}${offset 1}${color0}${fs_bar 4,17 "+device+"}${color}${offset 8}${voffset -2}${font Ubuntu:style=Bold:size=8}Free: ${color2}${fs_free "+device+"}${color}${font} ${alignr}${font Ubuntu:style=Bold:size=8}Used: ${color2}${fs_used "+device+"}${font}${color}\n")

print ("${voffset -10}")
