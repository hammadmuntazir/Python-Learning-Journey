import time
print("Chai is here")
username ="Hammad"
print(username)

'''

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS D:\Hammad Muntazir\Python by Hammad\Chapter 7\iteration_tool> ls



Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        15/02/2025     20:01             71 chai.py


PS D:\Hammad Muntazir\Python by Hammad\Chapter 7\iteration_tool> python3
PS D:\Hammad Muntazir\Python by Hammad\Chapter 7\iteration_tool>
PS D:\Hammad Muntazir\Python by Hammad\Chapter 7\iteration_tool> f=open('chai')   
was included, verify that the path is correct and try again.
At line:1 char:1
+ f=open('chai')
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (f=open:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS D:\Hammad Muntazir\Python by Hammad\Chapter 7\iteration_tool> f=open('chai.py')
was included, verify that the path is correct and try again.
At line:1 char:1
+ f=open('chai.py')
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (f=open:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS D:\Hammad Muntazir\Python by Hammad\Chapter 7\iteration_tool> python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> f=open('chai.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'print("Chai is here")\n'
>>> f.readline()
'username ="Hammad"\n'
>>>
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f=open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("Chai is here")\n'
>>> f.__next__()
'username ="Hammad"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for line in open('chai.py'):           
...     print(line)
... 
import time

print("Chai is here")

username ="Hammad"

print(username)
>>> f=open('chai.py')
>>> while True:
... line=f.readline()
  File "<stdin>", line 2
    line=f.readline()
    ^
IndentationError: expected an indented block after 'while' statement on line 1
>>> f=open('chai.py')
>>> while True:
...       line=f.readline()
...       if not line:break
...       print(line,end='')
...
import time
print("Chai is here")
username ="Hammad"
print(username)>>>
>>> test="hammad"
>>> if not test:
...      print("Chai")
...
>>> test=""
>>> if not test:
...     print("chai")
...
chai
>>> myList[1,2,3,4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myList' is not defined
>>> myList=[1,2,34]
>>> iter(myList)
<list_iterator object at 0x0000017874C26290>
>>> myList=[1,2,3,4]
>>> I=iter(myList)
>>> I
<list_iterator object at 0x0000017874D927A0>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x0000017874D927A0>
>>> I.__next__()
2
>>>  I.__next__()
  File "<stdin>", line 1
    I.__next__()
IndentationError: unexpected indent
>>>
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> f =open('chai.py')
>>> iter(f) is f             
True
>>> iter(f) is f.__iter__()
True
>>> myNewList=[1,2,3]
>>>  iter(myNewList)] is myNewList
  File "<stdin>", line 1
    iter(myNewList)] is myNewList
IndentationError: unexpected indent
>>> myNewList=[1,2,3]
>>> iter(myNewList) is myNewList
False
>>> D ={"a":1,"b":2}
>>> for key in D.keys():
...     print(key)
...
a
b
>>> I=iter(D)(key)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_keyiterator' object is not callable
>>> I=iter(D)
>>> I
<dict_keyiterator object at 0x00000178749BDBC0>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> range(5)
range(0, 5)
>>> R =range(5)
>>> R
range(0, 5)
>>> iter(R)
<range_iterator object at 0x00000178748DAF10>
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> range(6)
range(0, 6)
>>> E=range(6)
>>> E
range(0, 6)
>>> f=iter(E)
>>> next(f)
0
>>>
>>>
>>>
>>>
>>>
>>>
>>> next(f)
1
>>> next(f)
2
>>> next(f)
3
>>> next(f)
4
>>> next(f)
5
>>> next(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

'''