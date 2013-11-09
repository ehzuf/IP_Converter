# written by ZheFu on 11th, October, 2013

# IP = "192.168.1.1"
IP = raw_input("input IP: ")
binIP = ''.join([bin(int(x)+256)[3:] for x in IP.split('.')])

# NetMask = "255.255.255.0"
flag = raw_input("netmask(n) or CIDR (c): ")
if flag == 'n':
	NetMask = raw_input("input netmask: ")
	prefix = 0
	binNetMask = ''.join([bin(int(x)+256)[3:] for x in NetMask.split('.')])
	for x in range(0, 31):
		if binNetMask[x] == '1':
			prefix += 1
elif flag == 'c':
	prefix = int(raw_input("input CIDR: "))
else:
	print "wrong input."

zero = '00000000000000000000000000000000'
one = '11111111111111111111111111111111'

binMinIP = binIP[:prefix] + zero[prefix:]
binMaxIP = binIP[:prefix] + one[prefix:]

print '.'.join([str(int(binMinIP[x:(x+8)],2)) for x in range(0, 32, 8)]) + ' - '\
 + '.'.join([str(int(binMaxIP[x:(x+8)],2)) for x in range(0, 32, 8)])