#!/usr/bin/python -tt

# create_for508_mounts.py will generate custom mount point directories for exercises in the SANS FOR508 class.  Run "python create_for508_mounts.py -h" for usage details.
# By Mike Pilkington
# Version 1.0mik

import os
import argparse

parser=argparse.ArgumentParser()

parser.add_argument('dir_suffix', help='Provide a descriptive suffix to append to new mount point directories.  For example, "nfury" will create /mnt/ewf_nfury, /mnt/windows_nfury, /mnt/vss_nfury, /mnt/shadow_nfury, and /mnt/shadow_nfury/vss* directories. This argument is required.')
parser.add_argument('-n','--vss-number', type=int, nargs="?", dest="number", default=40, help='Optionally provide the number of vss subdirectories to create. The default is 40.')
parser.add_argument('-b','--base-path', nargs="?", dest="base", default='/mnt', help='Optionally provide the base path to create the mount directories. The default is "/mnt" (and must be run as root).')


args=parser.parse_args()

# Remove trailing slash if provided in base-path argument:
if args.base[-1] is "/":
    base_path = args.base[0:-1]
else:
    base_path = args.base


def createdir(directory):
    try:
        if os.path.exists(directory):
            print ('Error: Directory already exists: ' +  directory)
        else:
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory + ' (Must run as root for default base-path of /mnt)')

# Generate base mount point directories:
createdir(base_path + '/ewf_' + args.dir_suffix)
createdir(base_path + '/windows_' + args.dir_suffix)
createdir(base_path + '/vss_' + args.dir_suffix)
createdir(base_path + '/shadow_' + args.dir_suffix)
# Generate vss* subdirectories:
for num in range(args.number):
    createdir(base_path + '/shadow_' + args.dir_suffix +'/vss' + str(num + 1))
