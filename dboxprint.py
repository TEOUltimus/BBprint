import dropbox
import urllib
import os

def doWeAlreadyHaveThisFile(dir, fname):
	md = dc.metadata(dir, list=True, file_limit=5000, hash=None, rev=None, include_deleted=False)
	#print len(md['contents'])
	ls = []
	for x in md['contents']:
		if not x['is_dir']:
			#print os.path.basename(x['path'])
			ls.append(os.path.basename(x['path']))
	if fname in ls:
		return True
	else:
		return False
	
#Save the file at the url locally in the directory this code is saved in
#Concatenate DB's Public folder with filename to create a path in DB
#Then save the file to that path
def downloadFile(dir, fname):
	urllib.urlretrieve(url, fname) #local save
	path = dir + fname #concatenate
	f = open(fname, 'rb')
	response = dc.put_file(path, f) #DB save
	#print "uploaded:", response
	

#This hardcodes access token, which only gives you access to johanne's db.
#In final version this needs to be replaced with code similar to dboxtest.py
access_token = 'KgNLVgGC_AUAAAAAAAAAAeSERS4ujKiOw2VLxpgozNCXR8uPGrUDb_xJ8xS0el7-'
user_id = '102785560'

#make a dropbox client (and account info object)
dc=dropbox.client.DropboxClient(access_token)
ai=dc.account_info()

#save the url so we don't have to write long string many times.
#use the url to get a good filename
url = "https://dl.dropboxusercontent.com/u/14522752/Presentation.pdf"
course = url.split('/')[-2].split('#')[0].split('?')[0]
docname = url.split('/')[-1].split('#')[0].split('?')[0]
filename = course + docname

#if want specific subfolder of public, change this line (and create that subfolder when user installs)
dbdirectory = '/Public/'
if not doWeAlreadyHaveThisFile(dbdirectory,filename):
	downloadFile(dbdirectory,filename)

