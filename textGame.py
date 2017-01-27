import sys
from random import choice

kurier_status = "w pracy"

def magazyn():
    print(choice(odpMagazyn))
    return "magazyn"
def zatankuj():
    print(choice(odpZatankuj))
    return "stacja"
def odbierz(co,ulica):
    print(choice(odpOdbierz) + ulica)
    return "w pracy"
def zawieź(co,ulica):
    print(choice(odpZawieź) + ulica)
    return "w pracy"
def przerwa():
    print(choice(odpPrzerwa))
    return "przerwa"

odpMagazyn = ["OK, jade na magazyn.","Zjeżdżam na bazę.","Wracam do centrali."]
odpZatankuj = ["OK, jadę zatankować.", "Jadę nalać do baku."]
odpPrzerwa = ["OK, jadę sobie odpocząć.","Czas na przerwę !","Nareszczie odpoczynek."]
odpOdbierz = ["Jadę odebrać paczkę z ","Odbieram paczkę z ","Jadę po paczkę na "]
odpZawieź = ["Zawożę paczkę na ","Podrzucę paczkę na ", "Dostarczam paczkę na "]

while True:
    print("Status kuriera: " + kurier_status)
    orderLine=sys.stdin.readline()
    orderList=eval(orderLine)
    for order in orderList:
        # print("rozkaz" + str(order))
        if order[0] == "MAGAZYN":
            kurier_status = magzyn()
        elif order[0] == "ZATANKUJ":
            kurier_status = zatankuj()
        elif order[0] == "ODBIERZ":
            kurier_status = odbierz(order[1],order[2])
        elif order[0] == "ZAWIEŹ":
            kurier_status = zawieź(order[1],order[2])
        elif order[0] == "PRZERWA":
            kurier_status = przerwa()
