row=1
while row<=9:
	col=1
	while col<=row:
		print('%s*%s=%s' %(row,col,row*col),end='\t')
		col+=1
	print('')
	row+=1