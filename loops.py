# Loop in Python

# while

b=5
while b>=1:
	print b
	b -=1

s="*"
a=1
while a<=5:
	print " " + s
	a +=1

for letter in 'PYTHON':
	print letter
print "-------"

#for number in range(start, stop, steps)
for num in range(5):
	print(num)
print "------"

for num in range(10,20):
	print(num)
print "------"

for num in range(10,20, 2):
	print(num)
print "------"


my_list=['A1','A2','A3','A4','A5']

my_list_len=len(my_list)
print my_list_len

for i in range(0,my_list_len):
	print my_list[i]


for i in range(5, 0, -1):
	if i == 1:
		print "{0} This is".format(i)
	else:
		print "this is nothing"



'''
for i in range(9, 0, -1):
        if i == 1:
                print('1 bottle of beer on the wall, 1 bottle of beer!')
                print('So take it down, pass it around, no more bottles of beer on the wall!')
        elif i == 2:
                print('2 more bottles of beer on the wall, 2 more bottles of beer!')
                print('So take one down, pass it around, 1 more bottle of beer on the wall!')
        else:
                print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
                print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))
'''

'''
for num in range(10,20):
	for i in range(2,num):
		if num%i == 0:
			j=num/i
			print '%d equals %d * %d' % (num,i,j)
			break
	else:
		print num, 'is a prime number'
'''

# Once the loop execution comptele then it exeute else
for num in range(2,10):
	if num%2 ==0:
		print num
else:
	print "nothing"


#  it exeute else when if condition fails
for num in range(2,10):
	if num%2 ==0:
		print num
	else:
		print "nothing"


for num in range(10,20):
	for i in range(2,num):
		if num%i == 0:
			print num, i
			break
	else:
		print num, 'is a prime number'


# break continue
#continue # skip to the next value in "series"

for i in [1, 2, 3, 4, 5, 6]:
	if i == 3:
		print i
		#break
		continue
	else:
		print "else" + str(i)


# even odd in python

choice = raw_input("Enter a number: ")
if int(choice)%2 == 0:
	print "The number {0} is EVEN".format(choice)
else:
	print "The number %s is ODD" %(choice)
# 	print "The number %d is ODD" %(int(choice))


row = input("Enter row number: ")
for i in range(1,row):
	for j in range(1,i):
		print "* ",
#	else:
	print "\n"


row = input("Enter row number: ")
for i in range(1,row):
	for j in range(1,i):
		print "%s " %(j),
#	else:
	print "\n"


row = input("Enter row number: ")
for i in range(row, 1, -1):
	for j in range(1, i):
		print "* ",
	print "\n"



