import random
#random data i created
orderDate = ["09/27/2023", "08/30/2023", "06/06/2023", "02/04/2023", "10/22/2023"]
l_name = ["Barnes", "Blue", "Logan", "Ramsey", "Myers"]
product = ["Xbox", "PS5", "Nintendo", "Glasses", "Water"]
stock = [150, 687, 12, 65, 98, 78, 25, 35, 99, 100, 14, 2, 0, 86, 17, 502, 16, 48, 500, 26, 27]
cost = [6.99, 5.99, 19.99, 7.99, 512.99, 687.95, 1999.99, 385.99, 10.00, 4.00]
store = [orderDate, l_name, product, stock, cost]
orders = []
x = 0
#looping to enter all of the above data into a list(randomly put together) and then putting all of that into a list
while (x < 20):
    temp_list = []
    for lst in store:
        temp_list.append(random.choice(lst))
    orders.append(temp_list)
    x += 1

#getting the total of each order
for lst in orders:
    num = lst[3]*lst[4]
    lst.append("%.2f" % num)

print("Date\tName\tProduct\tStock\tCost\tTotal")
for lst in orders:
    print(*lst)
