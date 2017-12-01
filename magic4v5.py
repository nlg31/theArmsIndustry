def magic4(x):
	n=str(x)
	m1=[4,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
	m2=[0,3,6,6,5,5,5,7,6,6]
	m3=[0,0,0,7,8,0,0,7,0,0,8]

	if int(n)==4:
		print ('and 4 is the magic number')	
		return 0
			
	elif int(n)<20:
		print(n,'is',m1[int(n)],'and')
		n=m1[int(n)]
		magic4(n)

	elif len(n)==2:
		if int(n[1])==0:
			print(n, 'is', m2[int(n[0])])
			n=m2[int(n[0])]			
		else:
			print(n,'is',m2[int(n[0])]+m1[int(n[1])],'and')
			n=m2[int(n[0])]+m1[int(n[1])]
		magic4(n)

	elif len(n)==3:
		if int(n[1:3])==00:
			print(n, 'is', m1[int(n[0])]+m3[len(n)])
			n=m1[int(n[0])]+m3[len(n)]
		elif int(n[1])==1:
			print(n,'is',m1[int(n[0])]+m1[int(n[1])]+m3[len(n)],'and')
			n=m1[int(n[0])]+m1[int(n[1])]+m3[len(n)]
		elif int(n[2])==0:
			print(n, 'is', m1[int(n[0])]+m3[len(n)]+m2[int(n[1])])
			n=m1[int(n[0])]+m3[len(n)]+m2[int(n[1])]
		else:
			print(n,'is',m1[int(n[0])]+m3[len(n)]+m2[int(n[1])]+m1[int(n[2])],'and')
			n=m1[int(n[0])]+m3[len(n)]+m2[int(n[1])]+m1[int(n[2])]
		magic4(n)
			
	elif len(n)==4:
		if int(n[1:4])==000:
			print(n, 'is', m1[int(n[0:1])]+m3[len(n)])
			n=m1[int(n[0:1])]+m3[len(n)]
		elif int(n[2:4])<20 and int(n[2:4])>00:
			print(n,'is',m1[int(n[0:1])]+m3[len(n)]+m1[int(n[1])]+m3[len(n)-1]+m1[int(n[2:4])],'and')
			n=m1[int(n[0:1])]+m1[int(n[2:4])]+m3[len(n)]
		elif int(n[2:4])==00:
			print(n, 'is', m1[int(n[0:1])]+m2[int(n[1:2])]+m3[len(n)]+m1[int(n[2:3])]+m3[len(n)-1])
			n=m1[int(n[0:1])]+m2[int(n[1:2])]+m3[len(n)]+m1[int(n[2:3])]+m3[len(n)-1]
		elif int(n[3])==0:
			print(n, 'is', m1[int(n[0])]+m3[len(n)]+m1[int(n[1])]+m3[len(n)-1]+m2[int(n[2])])
			n=m1[int(n[0])]+m3[len(n)]+m1[int(n[1])]+m3[len(n)-1]+m2[int(n[2])]
		else:
			print(n,'is',m1[int(n[0:1])]+m3[len(n)]+m1[int(n[1:2])]+m3[len(n)-1]+m2[int(n[2:3])]+m1[int(n[3])],'and')
			n=m1[int(n[0:1])]+m3[len(n)]+m1[int(n[1:2])]+m3[len(n)-1]+m2[int(n[2:3])]+m1[int(n[3:4])]
		magic4(n)
		
	elif len(n)>4:
			print('try a smaller number, no more than 4 digits')
				
	else:
			magic4(n)
			

x='NULL'
while(x!="exit"):		
	x = input('\nenter a number to play 4 is the magic number or type "exit" to quit \n')		
	magic4(x)

	


