#from pyquery import PyQuery as pq
from datetime import datetime
from urllib import urlencode
import re, json, os, sys
print os.getcwd()
try:
	usr = sys.argv.index('-u') + 1
	pwd = sys.argv.index('-p') + 1
	username = sys.argv[usr]
	password = sys.argv[pwd]
	credentials = open('user.py', 'w')
	credentials.write('USERNAME = \'' + username + '\'\n')
	credentials.write('PASSWORD = \'' + password + '\'\n')
	credentials.close()
except:
	print 'Username and password not detected.'

#from auth import authenticate
import auth

auth.usr()
