import sys
from random import choice

kurier_status = "w pracy"

def magazyn():
    print(choice())
    kurier_status = "magazyn"
def zatankuj():
    print(choice())
    kurier_status = "stacja"
def odbierz(co,ulica):
    print(choice() + "ulica")
    kurier_status = "w pracy"
def zawieź(co,ulica):
    print(choice() + "ulica")
    kurier_status = "w pracy"
def przerwa():
    print(choice())
    kurier_status = "przerwa"

while True:
    print(kurier_status)
    orderLine=sys.stdin.readline()
    orderList=eval(orderLine)
    for order in orderList:
        # print("rozkaz" + str(order))
        if order[0] == "MAGAZYN":
            magzyn()
        elif order[0] == "ZATANKUJ":
            zatankuj()
        elif order[0] == "ODBIERZ":
            odbierz(order[1],order[2])
        elif order[0] == "ZAWIEŹ":
            zawieź(order[1],order[2])
        elif order[0] == "PRZERWA":
            przerwa()
