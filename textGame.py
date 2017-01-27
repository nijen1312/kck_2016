import sys

while True:
    orderLine=sys.stdin.readline()
    orderList=eval(orderLine)
    for order in orderList:
        print("rozkaz" + str(order))
