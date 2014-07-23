import os,sys,json
def getConfig(args):
	stream = open("config.json", 'r')
	config = json.load(stream)
	generateFolders(config,args)
def generateFolders(config,args):
	for (i,v) in enumerate(config["paths"]):
		generateFolder(v,args)
def init():
	args = sys.argv
	debug = 0
	for (i,v) in enumerate(args):
		if v == "--debug":
			debug = 1
	data = {"debug":debug}
	getConfig(data)
def generateFolder(path , data):
	if os.path.exists(path):
			if data["debug"] == 1:
    				print "[\033[93mWARN\033[0m]" + path + " already existed!"
   	else:
    		os.makedirs(path)
    		if data["debug"] == 1:
    				print "[\033[92mDONE\033[0m]" + path + " generated"
init()