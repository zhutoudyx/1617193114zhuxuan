Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = {'abc':456}
>>> dict1
{'abc': 456}
>>> dicr1['abc']

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dicr1['abc']
NameError: name 'dicr1' is not defined
>>> dict1['abc']
456
>>> dick1['ddd']

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dick1['ddd']
NameError: name 'dick1' is not defined
>>> dict1['abc']
456
>>> dict1['abc']=678
>>> dict1['abc']
678
>>> del dict1['abc']
>>> dict1
{}
>>> users = {
	'A':{
	'first':'yu',
	'last':'lei','
	
SyntaxError: EOL while scanning string literal
>>> users = {
	'A':{
	'first':'yu',
	'last':'lei',
	'location':'hs',
	},
	'B':{
	'first':'liu',
	'last':'wei',
	'location':'hs',
	},
}
>>> for username,userinfo in items():
	print("userid:" + username)
	print("userinfo:" + userinfo)
userid: A
SyntaxError: invalid syntax
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
userid£ºB
userinfo:{'last': 'wei', 'location': 'hs', 'first': 'liu'}
SyntaxError: invalid syntax
>>> 
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
SyntaxError: invalid syntax
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))
userid: A
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> for username, userinfo in users.items():
	print("userid£º" + username)
	print("userinfo:" + str(userinfo))

	
userid£ºA
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
userid£ºB
userinfo:{'last': 'wei', 'location': 'hs', 'first': 'liu'}
>>> dict = {'Name': 'Zara', 'Age': 7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>>  print "Key : %s" % dict.keys()
 
  File "<pyshell#42>", line 2
    print "Key : %s" % dict.keys()
    ^
IndentationError: unexpected indent
>>> 
KeyboardInterrupt
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dick.keys():
	print key

	

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    for key in dick.keys():
NameError: name 'dick' is not defined
>>> 
>>> for key in dict.keys():
	print key

	
Age
Name
>>> for key in dict.keys():
	print dict[key]

	
7
Zara
>>> 
