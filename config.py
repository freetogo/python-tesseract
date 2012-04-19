import platform,os
#osname=platform.uname()[0].lower()

def paths_exists(hfile) :
	if osname == 'linux' :
		return os.path.exists(os.path.join("/usr/local/include",hfile)) || os.path.exists(os.path.join("/usr/include",hfile))

	
def idefine(fp,name):
	fp.write("#ifndef __%s__\n"%name)
	fp.write("\t#define __%s__\n"%name)
	fp.write("#endif\n")


fp=open("config.h","w")
idefine(osname)

if paths_exists("opencv/cv.h")  :
	idefine("opencv")

	  
fp.close()
