#!/usr/bin/python3
import time
import sys
from io import StringIO
import contextlib

#@contextlib.contextmanager
#def stdoutIO(stdout=None):
##    old = sys.stdout
#    if stdout is None:
#        stdout = io.StringIO()
#    sys.stdout = stdout
#    yield stdout
#    sys.stdout = old

# code = """
# i = [0,1,2]
# for j in i :
    # print(j)
# """
# with stdoutIO() as s:
    # try:
        # exec(code)
    # except:
        # print("Something wrong with the code")
# print("out:", s.getvalue())

with open('bd_prov_6nodes.py') as f:
	for line in f:		
		if line.startswith("#prompt"):
			input("Please get board ready and hit enter...")
			continue
		elif line.startswith("#endprovisioning"):
			break
		elif line.startswith("#"):
			continue
		print("Please hit enter to execute ", line) 
		input()
		stIO = StringIO()
		with contextlib.redirect_stdout(stIO):
			exec(line)
	#	try:
	#			exec(line)
     #       except:
	#			print("Something wrong with the code")
		print("out:", stIO.getvalue())
		del stIO		
   