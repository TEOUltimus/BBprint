import dropbox, os, re, requests 
#import urllib

# This hardcodes access token, which only gives you access to johanne's dropbox
#TODO replace with code similar to dboxtest.py
access_token = 'KgNLVgGC_AUAAAAAAAAAAeSERS4ujKiOw2VLxpgozNCXR8uPGrUDb_xJ8xS0el7-'
user_id = '102785560'

# Make a dropbox client (and account info object)
dc=dropbox.client.DropboxClient(access_token)
ai=dc.account_info()

# Check user's blackboard to ensure file is new
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
	
# Save the file at the url locally in the directory this code is saved in
# Concatenate DB's Public folder with filename to create a path in DB
# Then save the file to that path
def downloadFile(url, dir, fname, session=None):
	#urllib.urlretrieve(url, fname) #local save
	authenticated_download(url, fname, session)
	path = dir + fname #concatenate
	with open(fname, 'rb') as f:
		response = dc.put_file(path, f) #DB save
	#print "uploaded:", response
	
# Utilize existing session to authenticate with blackboard before downloading
def authenticated_download(url, fname, session=None):
	# NOTE the stream=True parameter
	r = session.get(url, stream=True)
	with open(fname, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
				f.flush()

# Use url splitting and replace %20, etc. to get a good filename
def url_manipulation(url):
	#url = "https://blackboard.andrew.cmu.edu/bbcswebdav/pid-609620-dt-content-rid-4015720_1/courses/S14-12623/Preview%20of%20%E2%80%9Cassignment1%E2%80%9D%281%29.pdf"
	course = url.split('/')[-2].split('#')[0].split('?')[0]
	docname = url.split('/')[-1].split('#')[0].split('?')[0]
	filename = course + docname
	filename = re.sub('%..[0-9]?', '', filename)
	return filename

# Primary method for use by outside callers
def dropbox_print(session, fileurl = 'https://dl.dropboxusercontent.com/u/14522752/Presentation.pdf'):
	filename = url_manipulation(fileurl)
	
	''' If you want a specific subfolder of public, change this line
		(And create that subfolder when user installs) '''
	dbdirectory = '/Public/'
	if not doWeAlreadyHaveThisFile(dbdirectory,filename):
		downloadFile(fileurl, dbdirectory,filename,session)

