print "Hello Python"

#g = input("please enter a num: ")

#print g

P = pow(4,3)
print P

ABSOLUTE=abs(-18)
print ABSOLUTE

import math
print math.floor(16.7)
SQRT= math.sqrt
print SQRT(81)

num = str(15)
print "helo " + num

num = repr(15)
print "helo " + num

# repr and str does the same thing

#G = raw_input("enter strng: ")
#print G


arr = ['11','21','31']
print arr[0]
print arr[1]
print arr[2]

stri = "Manish"[4]
print stri


# SEQUENCE

seqf =  ["man", "tan", "ban", "wan", "san", "jan"]
print seqf[3]
print seqf[-3]

seq =  ["0", "1", "2", "3", "4", "5", "6", "7"]

print seq[0:7:2]

print "manish "*4

print [21]*5
print 21*5

#chapter 11
name="manish"
print 'r' in name

# chapter 12

nums=[1,3,14,6,2]
print min(nums)
print max(nums)
print len(nums)
print list('manish')

print "old string " + str(nums)
nums[3]=26
print "new string " + str(nums)

print "old string-del " + str(nums)
del nums[3]
print "new string-del " + str(nums)


stri="manish"
print list(stri)
print list(stri[1])

# chapter 13

example=list("sweta ghosh")
print "old" + str(example)

example[6:]=list("pandey")

print "new" + str(example)



#Python has five standard data types −

#    Numbers
#    String
#    List
#    Tuple
#    Dictionary

# The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] )
# and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) 
# and cannot be updated. Tuples can be thought of as read-only lists.

# Python's dictionaries are kind of hash table type consist of key-value pairs.
# Dictionaries are enclosed by curly braces ({ }) and values can be assigned
# and accessed using square braces ([]). 

example=[1,2,3]
example[1:1]=[4,4,4]
print example

#14

mac=[11,22,33]
print mac
mac.append(44)
print mac


app=["my", "name", "is", "manish", "manish"]
print app.count("manish")


two=["Pandey", "from", "Dehradun"]

app.extend(two)

print app



#chapter 15
#index, reverse, insert, pop, remove, sort, sorted

#chapetr 17 string: 

STR="Hi. My name is %s. I am from %s"
var1=("Manish", "Dehradun")
print STR %var1

# find, 
SD="Hi My name is Manish"
print SD.find("name")

#join
SA="my name is GID"
JOIN="-"
print JOIN.join(SA)

print SA.lower()
print SA.upper()

print SA.replace("GID", "GOD")

#19 DICTIONARY

family={'dad':'Harish', 'Mom':'Deepa','Bro':'Saket', 'Sis':'Himani'}
print family

print family['dad']
print family['Sis']

print family.has_key('dad')

newf=family.copy()
print newf

newf.clear()

print newf


#20 if else
var= raw_input("please enter a string: ")

if var=="manish":
	print "My name is " + var
elif var=="pandey":
	print "My Surname is " + var
else:
	print "I Don't know what it is.."
	
	

#25loop

b=1
while b<=5:
	print b
	b=b+1
	
g1=['allo','khalo','pilo']

for food in g1:
	print "i want " + food
	


#while 1:
#	name = raw_input("Enter a name: ")
#	if name =="quit":
#		break
#		

#func

def new_func():
	return "hello"

print new_func()

	
def func1(x):
	return x+10

print func1(4)
