print('Onudevs Leave Application System')

while True:	
	employeenameDatabase = ['Fardous','Ratia','Sayanta','Rafayet','Choyon','Riffat','Wahid','Rituparna']
	employeeidDatabase = ['1004','1008','1009','1010','1011','1013','1014','1015' ]	

	employeename = input('User Name:')
	employeeid = input('ID:')

	
	if employeename in employeenameDatabase and employeeid in employeeidDatabase:
		print('log in successfull')
		print('What type of leave you need')
		leavesType = ['Annual Leave', 'Sick Leave', 'Casual Leave']		
		print(leavesType)
		leavetype = input('Leave Type:')
		if leavetype == '':
			print('Please fill up your leave type.')
		else:
			days = input('How many days:')
			print('Date:dd.mm.yy to dd.mm.yy')
			date = input('Date:')
			print('Thanks for your application. Soon HR will confirm you through mail.') 
			break
			
	else:
		print(' Your user Name or Id is Invalid.')
		

