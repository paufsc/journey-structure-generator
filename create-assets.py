import os,sys

def addList(path):
	generateFolder(path)
def generateFolders():
	addList("docs")
	addList("docs/en")
	addList("docs/tr")
	addList("assets/css")
	addList("assets/js")
	addList("assets/img")
def generateFolder(path):
	if os.path.exists(path):
    		print "[\033[93mWARN\033[0m]" + path + " already existed!"
   	else:
    		os.makedirs(path)
    		print "[\033[92mDONE\033[0m]" + path + " generated"
generateFolders()
print ""