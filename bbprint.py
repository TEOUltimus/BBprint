#from pyquery import PyQuery as pq
from datetime import datetime
from urllib import urlencode
from cryptor import encode
from dboxprint import dropbox_print
import re, json, os, sys

# check for credentials, encode and store them if found
try:
	usr = sys.argv.index('-u') + 1
	pwd = sys.argv.index('-p') + 1
	username = sys.argv[usr]
	password = sys.argv[pwd]
	credentials = open('user.py', 'w')
	credentials.write('USERNAME = 0x' + str(encode(username)) + '\n')
	credentials.write('PASSWORD = 0x' + str(encode(password)) + '\n')
	credentials.close()
except:
	pass #no-op
	#print 'Username and password not detected. Loading stored credentials.'
	#print 'If you want to use a new username and password use the \'-u\' and \'-p\' tags'

from auth import authenticate

s = authenticate('https://blackboard.andrew.cmu.edu')
#print 'Blackboard authentication failed.  Ensure your username and password are correct.'


'''print s.get('https://blackboard.andrew.cmu.edu/webapps').text

TODO Remove everything after this
bbGrades = json.loads(s.post('https://blackboard.andrew.cmu.edu/webapps/streamViewer/streamViewer', data={'cmd': 'loadStream', 'streamName': 'mygrades', 'forOverview': False, 'providers': {}}).content)

# Sometimes blackboard fails for unknown reasons, raise exception in this case
if len(bbGrades['sv_extras']['sx_filters']) == 0:
	raise Exception('blackboard connection failed')

for course_id, course in bbGrades['sv_extras']['sx_filters'][0]['choices'].iteritems():
	print course
'''
