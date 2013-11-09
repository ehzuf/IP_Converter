# written by ZheFu on 11th, October, 2013

# IP1 = "1.2.3.127"
IP1 = raw_input("input IP1: ")
binIP1 = ''.join([bin(int(x)+256)[3:] for x in IP1.split('.')])

# IP2 = "1.2.3.248"
IP2 = raw_input("input IP2: ")
binIP2 = ''.join([bin(int(x)+256)[3:] for x in IP2.split('.')])

zero = '00000000000000000000000000000000'
one = '11111111111111111111111111111111'

print "The CIDR of " + IP1 + " - " + IP2 + " is:"
print

count = 0

def convert(binIP1, binIP2):
	global count
	count += 1
	if binIP1 == binIP2:
		print '.'.join([str(int(binIP2[x:(x+8)],2)) for x in range(0, 32, 8)]) + '/' + str(32)
		return

	flag = 0
	for i in range(0, 32):
		if binIP1[i] != binIP2[i]:
			flag = i
			break

	for i in range (31, -1, -1):
		if binIP1[i] == '1':
			if i <= flag:
				for j in range (flag, 32):
					tempbinIP1 = str(bin(int(binIP1,2) + int(one[j:],2) + 4294967296)[3:])
					if int(tempbinIP1,2) <= int(binIP2,2):
						print '.'.join([str(int(binIP1[x:(x+8)],2)) for x in range(0, 32, 8)]) + '/' + str(j)
						tempbinIP1 = str(bin(int(binIP1,2) + int(one[j:],2) + 1 + 4294967296)[3:])
						if int(tempbinIP1,2) <= int(binIP2,2):
							convert(tempbinIP1, binIP2)
						break
			else:
				print '.'.join([str(int(binIP1[x:(x+8)],2)) for x in range(0, 32, 8)]) + '/' + str(i+1)
				tempbinIP1 = str(bin(int(binIP1,2) + int(binIP1[i:],2) + 4294967296)[3:])
				if int(tempbinIP1,2) <= int(binIP2,2):
					convert(tempbinIP1, binIP2)
				break
			break

convert(binIP1, binIP2)
print count