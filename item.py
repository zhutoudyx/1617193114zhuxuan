Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:/Users/lenovo32/Desktop/find.py =================
>>> import re
>>>  string="abcdefg  acbdgef  abcdgfe  cadbgfe"
>>> string
  File "<pyshell#1>", line 2
    string="abcdefg  acbdgef  abcdgfe  cadbgfe"
    ^
IndentationError: unexpected indent
>>> string
'abcdefg  acbdgef  abcdgfe  cadbgfe'
>>>  re.findall('\w', string)
 
  File "<pyshell#3>", line 2
    re.findall('\w', string)
    ^
IndentationError: unexpected indent
>>> re.findall('\w', string)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'c', 'b', 'd', 'g', 'e', 'f', 'a', 'b', 'c', 'd', 'g', 'f', 'e', 'c', 'a', 'd', 'b', 'g', 'f', 'e']
>>> re.findall('\w+', string)
['abcdefg', 'acbdgef', 'abcdgfe', 'cadbgfe']
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>>  y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adf.com'
 
  File "<pyshell#7>", line 2
    y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adf.com'
    ^
IndentationError: unexpected indent
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adf.com'
>>> test_list = ['first', 'seconde']
>>> test_list
>>> test_list = ['first', 'seconde']
>>> test_list = ['first', 'seconde']
>>> test_list
['first', 'seconde']
>>> test_list[0]
'first'
>>> test_list[1]
'seconde'
>>> for item in test_list:



print(item)
  File "<pyshell#20>", line 6
    print(item)
        ^
IndentationError: expected an indented block
>>> for item in test_list:
	print(item)

	
first
seconde
>>> 
