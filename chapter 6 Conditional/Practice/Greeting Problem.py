'''
Create a python program capable of greeting you with Good Morning ,Good Afternoon  and Good Evening .
Your program should use time module to get the current hour.Here is sample program and documentation link for you.
'''

#import time
'''import time python ki library ka part hai just like tkinter
iski waja sy hum bohat sy program krskty hai jin mn time functions  ka use hota hai,jesy tkinter ki waja sy GuI bana skty thy
ab is mn bohat sy function hai unhi mn aik localtime() hai jis sy program humy humara current time laptop wala bata skta hai
time.localtime()  =>jub hum kuch import krty hai jesy thinkter as tk() kia tha to haar cheeze jis mn vo use ho raha tha hum pahly tk. aur phir cheeze likty thy
but agr hum likh haar jaga time.  nai likhna chaty hum likh skty hain "from time import *"* mean everything to sary function apny ap mil jay gyein time ky aur humy haar jaga time . use krna nai pary ga
'''
#current_hour = time.localtime().tm_hour

from time import * #idr sub kuch ly lia hai time sy isliye time.nai kry gyein
current_hour = localtime().tm_hour
#.tm_hour sy hour ka pta lgy ga  baki hum minute aur second bi pta lgava skty hain insy=> tm_min, tm_sec
#current_hour = time.localtime().tm_hour
# yh sub idr tak already python mn kia hua hai start sy unho ny baki hum condition lga kr khud bana lain gye program
##current_minute = localtime().tm_min
#print(current_hour,":",current_minute,"") in 20 aur 21 ko use krky minute bi ly kr asakty hain
print(current_hour)
if 5 <= current_hour < 12:
    print("Good Morning!")
#agr 5am sy zaida aur 12 pm sy kum time hua to morning
elif 12 <= current_hour < 16:
    print("Good Afternoon!")
#agr 12 pm sy  zaida hua aur 17 mean 4pm tak afternoon dy ga
elif 16 <= current_hour < 21:
    print("Good Evening!")
#agr 4pm sy ly kr  8pm tak ka time hua  to evening day ga
else:
    print("Hello! It's late,Good Night")
#9pm ky baad good night dy ga  .5am sy pahly tak

