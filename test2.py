Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = { 'abc': 456 }
>>> dict1
{'abc': 456}
>>> dict1['abc']
456
>>> dick1['ddd']

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dick1['ddd']
NameError: name 'dick1' is not defined
>>> dict1['ddd']

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dict1['ddd']
KeyError: 'ddd'
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
    'last':'lei',
    'location':'hs',
    },
    'B':{
    'first':'liu',
    'last':'wei',
    'location':'hs',    
    },
}
>>> for username, userinfo in users.items():
	print("userid��" + username)
	print("userinfo:" + userinfo)

	
userid��A

Traceback (most recent call last):
  File "<pyshell#14>", line 3, in <module>
    print("userinfo:" + userinfo)
TypeError: cannot concatenate 'str' and 'dict' objects
>>> for username, userinfo in users.items():
	print("userid��" + username)
	print("userinfo:" + str(userinfo))

	
userid��A
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
userid��B
userinfo:{'last': 'wei', 'location': 'hs', 'first': 'liu'}
>>> dict = {'Name': 'Zara', 'Age': 7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dick.keys():
	print key

	

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for key in dick.keys():
NameError: name 'dick' is not defined
>>> for key in dict.keys():
	print key

	
Age
Name
>>> for key in dict.keys():
	print dict[key]

	
7
Zara
>>> 
