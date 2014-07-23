import os,sys,json

def addList(path):
	generateFolder(path)
def getConfig():
	stream = open("config.json", 'r')
	config = json.load(stream)
	generateFolders(config)
def generateFolders(config):
	for (i,v) in enumerate(config["paths"]):
		addList(v)
def init():
	getConfig()
def generateFolder(path):
	if os.path.exists(path):
    		print "[\033[93mWARN\033[0m]" + path + " already existed!"
   	else:
    		os.makedirs(path)
    		print "[\033[92mDONE\033[0m]" + path + " generated"
init()