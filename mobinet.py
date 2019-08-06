import object
#import fill
def diff(l1,l2):
	s=0
	if l1[0]==l2[0]:
		s=s+16*16
	if l1[0]==l2[1]:
		s=s+16*8
	if l1[0]==l2[2]:
		s=s+16*4
	if l1[0]==l2[3]:
		s=s+16*2
	if l1[0]==l2[4]:
		s=s+16*1
	if l1[1]==l2[0]:
		s=s+8*16
	if l1[1]==l2[1]:
		s=s+8*8
	if l1[1]==l2[2]:
		s=s+8*4
	if l1[1]==l2[3]:
		s=s+8*2
	if l1[1]==l2[4]:
		s=s+8*1
	if l1[2]==l2[0]:
		s=s+4*16
	if l1[2]==l2[1]:
		s=s+4*8
	if l1[2]==l2[2]:
		s=s+4*4
	if l1[2]==l2[3]:
		s=s+4*2
	if l1[2]==l2[4]:
		s=s+4*1
	if l1[3]==l2[0]:
		s=s+2*16
	if l1[3]==l2[1]:
		s=s+2*8
	if l1[3]==l2[2]:
		s=s+2*4
	if l1[3]==l2[3]:
		s=s+2*2
	if l1[3]==l2[4]:
		s=s+2*1
	if l1[4]==l2[0]:
		s=s+1*16
	if l1[4]==l2[1]:
		s=s+1*8
	if l1[4]==l2[2]:
		s=s+1*4
	if l1[4]==l2[3]:
		s=s+1*2
	if l1[4]==l2[4]:
		s=s+1*1
	return(s)
def main(path):
	d={}
	for i in range(1,342):
		d[i]=[]
	#fill.register()
	predictions=object.itl(path)
	with open('register.txt') as myfile:
		file_content = myfile.readlines()
	l=[]
	for i in file_content:
		l.append(i.split())
	for i in l:
		n=diff(predictions,i[1:])
		if n!=0:
			d[n].append(i[0])	
	result=[]
	probs=[]
	i=341
	while i!=0:
		if d[i]!=[]:
			for j in d[i]:
				result.append(j)
				probs.append(i)
		i=i-1
	return([result,predictions[0],probs])
