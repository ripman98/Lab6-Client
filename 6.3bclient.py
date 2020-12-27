import socket
import sys

ClientSocket = socket.socket()
host = '192.168.1.6'
port = 4848

print('Checking Connection.....')

try:
	ClientSocket.connect((host,port))
	print('Server Connected')

except socket.error as e:
	print(str(e))

while True:
	print('\n Welcome to python math calculator')
	print('Enter the number 1 for Logarithmic Expression')
	print('Enter the number 2 for Square Root')
	print('Enter the number 3 for Exponential Expression')
	print('Enter the number 4 to Exit')

	code = input('Enter the code word: ')
	ClientSocket.send(code.encode())

	num = input('\n Enter Number: ')
	ClientSocket.send(num.encode())
	total = ClientSocket.recv(2048)

	if code == '1':
		print('Answer for LOG calculation: '+str(total.decode()))

	if code == '2':
		print('Answer for ROOT calculation: '+str(total.decode()))

	if code == '3':
		print('Answer for EXPO calculation: '+str(total.decode()))

	if code == '4':
		Client.clode()
		sys.exit()
