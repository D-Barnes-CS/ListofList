import random
#random data i created
#*
'''
D Barnes
Revision: 9/25/23
'''

#P1
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


#P2
old_list = [78, 56, 8, 12, 90, 21, 71, 98, 101, 1245, 1600]
new_list = []
for i in range(len(old_list)):
    try:
        new_list.append(old_list[i-1] + old_list[i+1])
    except IndexError:
        if(old_list[i-1]):
            new_list.append(old_list[i-1] + old_list[i])
            print("this is indexing to the last digit in the list instead of checking if its the last digit"
                  " fix later.")
        else:
            new_list.append(old_list[i] + old_list[i+1])
            print("bye")

print(new_list)

user_data = "John Q Public 541-233-7612"
num = ""
name = ""
for ch in user_data:
    if (ch.isdigit() or ch == '-'):
        num += ch
    else:
        name += ch

print(num)
print(name)

print("I once was a \"child\"  who was stuck in 1st grade.")
print("But i knew D\'s brain would allow him to pass on the first try.")
print('''
He's just a poor boy from a poor family                         d           d
Spare him his life from this monstrosity     preserving white space
''')
print("This is multiple"
      " lines but on a "
      "singular line")

'''
D Barnes
Revision: 9/27/2023
'''