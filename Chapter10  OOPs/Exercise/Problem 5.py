'''
   Problem5
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.

'''
from random import randint

class Train:
    def book(self,traino):
        self.traiNo=traino
        print(f"Tick is book in train no :{trainNo} from{fro} to {to}")

    def getStatus(self,fro,to):
        print(f"Train no:{self.trainNo}is running on time")

    def getFare(self,trainNo,fro,to):#from is reserved so we cannot use it
        print(f"Ticket fare in train no:{trainNo}from{fro}to{to} is{randint(222,555)}")
