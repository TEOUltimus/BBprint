'''from pyquery import PyQuery as pq
from auth import authenticate
from datetime import datetime
from urllib import urlencode'''
import re, json, os, sys

try:
	usr = sys.argv.index('-u') + 1
	pwd = sys.argv.index('-p') + 1
except ValueError:
	print 'Username and password not detected.'


