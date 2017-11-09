Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> y = 'localpath C:\code\cnkiCrawl'
>>> y = 'Hello Kitty Hello Hello Kitty Kitty Hello Kitty'
>>> re.findall('(Hello)',y)
['Hello', 'Hello', 'Hello', 'Hello']
>>> re.findall('Hello',y)
['Hello', 'Hello', 'Hello', 'Hello']
>>> re.findall('(Hello){2}',y)
[]
>>> re.findall('(Hello ){2}',y)
['Hello ']
>>> re.findall('(:?hello ){2}',y)
[]
>>> re.findall('(:?Hello ){2}(Kitty)',y)
[('Hello ', 'Kitty')]
>>> re.findall('(:?Hello ){2}',y)
['Hello ']
>>> 
