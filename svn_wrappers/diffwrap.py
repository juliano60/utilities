#!/usr/bin/env python3
import sys
import os
import subprocess

# Configure diff program
DIFF = r'C:\Program Files\SourceGear\Common\DiffMerge\sgdm.exe'

# Subversion provides the paths we need 
LEFT = sys.argv[-2]
RIGHT = sys.argv[-1]

#for arg in sys.argv:
#	print('DEBUG: {}'.format(arg))

# call the diff command 
args = ['-t1="Original"',
		'-t2="Mine"',
		LEFT,
		RIGHT]
args = ' '.join(args)
#os.execv(DIFF, args)
subprocess.run(DIFF + ' ' + args)

# return an errorcoe of 0 if no differences were detected,
# 1 if some were