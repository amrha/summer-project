import os
import object
def register():
	l=[]
	for root, dirs, files in os.walk("./static/base/"):
		for name in files:
			l.append(name)
	k=0
	for i in l:
		with open('register.txt') as myfile:
			if not(i in (myfile.read()).split()[::6]):
				with open("register.txt", "a") as myfile2:
					l2=object.itl("static/base/"+i)
					myfile2.write(i+" "+l2[0]+" "+l2[1]+" "+l2[2]+" "+l2[3]+" "+l2[4]+"\n")
register()
