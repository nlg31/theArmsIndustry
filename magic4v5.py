def magic4(x):
	n=str(x)
	z=n
	x=0
	m1=[0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
	m2=[0,3,6,6,5,5,5,7,6,6]
	m3=[0,0,0,7,8,8,7,7,7,7,7,7,7,8,8,7,9,9,7,10,10,7,11,11,7,13]

	if(int(n)==0):
		#print(n,'is',4,'and')
		n=4
	
	elif int(n)==4:
		print ('4 is the magic number')	
		return 0
		
	elif (len(n)<4):
		n=str('0'*(4-len(n)))+n
		#print(n)
			
	if(int(n)!=4):			
		while(len(n)>=4):
			if (int(n[len(n)-2:len(n)])>0) and (int(n[len(n)-2:len(n)])<20):
				x+=int(m1[int(n[len(n)-2:len(n)])]+m3[len(n)-2])
				#print(x, '1')
			if (int(n[len(n)-2:len(n)])>=20):
				x+=int(m2[int(n[len(n)-2])] +m1[int(n[len(n)-1])] +m3[len(n)-2])
				#print(x, '2')
			if (int(n[len(n)-3])!=0 and len(n)>=3):
				x+=m1[int(n[len(n)-3])]+m3[len(n)-1]
				#print(x,'3')
			if (int(n[len(n)-4])!=0 and len(n)>=4):
				x+=m1[int(n[len(n)-4])]+m3[len(n)]
				#print(x,'4')
				n=str(len(n)-1)
			print(z, 'is', x, ' and')
			n=str(x)
			magic4(n)
								
x='NULL'
while(x!="exit"):		
	x = input('\nenter a number to play 4 is the magic number or type "exit" to quit \n')		
	magic4(x)

	

