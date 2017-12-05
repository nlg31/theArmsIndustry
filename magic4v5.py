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
	if int(n)==4:
		print ('4 is the magic number')	
		return 0
	if(len(n)<3):
		n=str('0'*(3-len(n)))+n
		#print(n)
		
	if(int(n)!=4):			
		while(int(n)!=0):
			#ones and tens
			if (len(n)%3==0):
				if int(n[1:3])<20 and int(n[1:3])>0:
					x+=int(m1[int(n[1:3])])
					#print(x, "3_1")
				if (int(n[1:3])>=20):
					x+=int(m2[int(n[1])] +m1[int(n[2])])
					#print(x, "3_2")
				if int(n[0])!=0:
					x+=m1[int(n[0])]+m3[len(n)]
					#print(x,"3_3")
				if(n[3:]!=''):
					n=n[3:]
				else:
					n=str(x)
					print(z, 'is', x, ' and')
					break;
			#thousands
			if ((len(n)-1)%3==0):
				if (int(n[2:4])>0) and (int(n[2:4])<20):
					x+=int(m1[int(n[2:4])]+m3[len(n)-1]) +m3[len(n)-2]
					#print(x, "4_1")
				if (int(n[2:4])>=20):
					x+=int(m2[int(n[2])] +m1[int(n[3])] +m3[len(n)-2])
					#print(x, "4_2")
				if int(n[1])!=0:
					x+=m1[int(n[1])]+m3[len(n)-1]
					#print(x,"4_3")
				if int(n[0])!=0:
					x+=m1[int(n[0])]+m3[len(n)]
					#print(x, "4_4")
				if(n[4:]!=''):
					n=n[4:]
				else:
					n=str(x)
					print(z, 'is', x, ' and')
					break;
			#hundreds
			if((len(n)-2)%3==0):
				if (int(n[3:5])>0) and (int(n[3:5])<20):
					x+=int(m1[int(n[3:5])]+m3[len(n)-3])
					#print(x, "5_1")
				if (int(n[3:5])>=20):
					x+=int(m2[int(n[3])] +m1[int(n[4])] +m3[len(n)-3])
					#print(x, "5_2")
				if int(n[2])!=0:
					x+=m1[int(n[2])]+m3[len(n)-2]
					#print(x,"5_3")
				if (int(n[0:2])>0) and (int(n[0:2])<20):
					x+=int(m1[int(n[0:2])]+m3[len(n)-1])
					#print(x, "5_4")
				if (int(n[0:2])>=20):
					x+=int(m2[int(n[0])] +m1[int(n[1])] +m3[len(n)])
					#print(x, "5_5")
				if(n[5:]!=''):
					n=n[5:]
				else:
					n=str(x)
					print(z, 'is', x, 'and')
					break;
		magic4(n)
								
x='NULL'
while(x!="exit"):		
	x = input('\nenter a number to play 4 is the magic number or type "exit" to quit \n')		
	magic4(x)

	

