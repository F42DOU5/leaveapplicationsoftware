print('Onudevs Leave Application System')

while True:	
	employeename = input('User Name:')
	employeeid = input('ID:')
	if employeename == 'Fardous' and employeeid == '1004':
		print('log in successfull')
		print('What type of leave you need')
		leavestype = ['Annual Leave', 'Sick Leave', 'Casual Leave']
		print(leavestype)
		leavetype = input('Leave:')
		days= input('How many days:')
		date= input('Date:')
		print('Thanks for your application. Soon HR will confirm you through mail') 
		break
	else:
		print(' Your user Name or Id is Invalid')
		continue

