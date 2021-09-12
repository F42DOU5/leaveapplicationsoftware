print('Onudevs Leave Application System')

employeename = input('User Name:')
employeeid = input('ID:')

if employeename == 'Fardous' and employeeid == '1004':
	print('log in successfull')
	print('What type of leave you need')
	leavestype = ['Annual Leave', 'Sick Leave', 'Casual Leave']
	print(leaves)
	leavetype = input()
	days= input('How many days')
	date= input('Date')
	print('Thanks for your application. HR will conform you through mail') 
else:
	print(' Your user Name or Id is Invalid')

