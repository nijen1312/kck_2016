import sys

odpMagazyn = ["OK, jade na magazyn.","Zjeżdżam na bazę.","Wracam do centrali."]
odpZatankuj = ["OK, jadę zatankować.", "Jadę nalać do baku."]
odpPrzerwa = ["OK, jadę sobie odpocząć.","Czas na przerwę !","Nareszczie odpoczynek."]
odpOdbierz = ["Jadę odebrać paczkę z ","Odbieram paczkę z ","Jadę po paczkę na "]
odpZawieź = ["Zawożę paczkę na ","Podrzucę paczkę na ", "Dostarczam paczkę na "]

while True:
    orderLine=sys.stdin.readline()
    orderList=eval(orderLine)
    for order in orderList:
        # print("rozkaz" + str(order))
