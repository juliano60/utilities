#!/usr/bin/env python3
import sys
import os

# Configure diff program
DIFF = r'C:\Program Files\SourceGear\Common\DiffMerge\sgdm.exe'

# Subversion provides the paths we need 
LEFT = sys.argv[-2]
RIGHT = sys.argv[-1]

# call the diff command 
args = ['-no-splash',
		'-t1="Original"',
		'-t2="Mine"',
		LEFT,
		RIGHT]
os.execv(DIFF, args)

# return an errorcoe of 0 if no differences were detected,
# 1 if some were