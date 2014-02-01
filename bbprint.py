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

from auth import authenticate

s = authenticate('https://blackboard.andrew.cmu.edu')
#print s

#TODO Remove
bbGrades = json.loads(s.post('https://blackboard.andrew.cmu.edu/webapps/streamViewer/streamViewer', data={'cmd': 'loadStream', 'streamName': 'mygrades', 'forOverview': False, 'providers': {}}).content)

print s.get('https://blackboard.andrew.cmu.edu/').content

# Sometimes blackboard fails for unknown reasons, raise exception in this case
if len(bbGrades['sv_extras']['sx_filters']) == 0:
	raise Exception('blackboard connection failed')

for course_id, course in bbGrades['sv_extras']['sx_filters'][0]['choices'].iteritems():
	print course
