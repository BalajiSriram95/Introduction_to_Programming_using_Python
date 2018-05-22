# How to Write to a File
log_book = open('log_entry.txt', 'w') # 'w' for write
                                      # 'r' for read
                                      # 'a' for append
log_book.write('first log')
log_book.write('second log')
log_book.close()

# Writing a Newline to a File
log_book = open('log_entry.txt', 'w')
log_book.write('first log\n')
log_book.write('second log\n')
log_book.write('thrid log\n')
log_book.close()


# Writing Out Each Order
def write_log_book(order_entries):
    file = open('log_entry.txt', 'w')
    for order in order_entries:
        file.write(order + '\n')
    file.close()

def main():
    fruitsandprices = {'Banana - 1kg': 20, 'Cherry - 300gs': 30, 'Grape - 1kg': 40, 'Watermelon - 2kg': 50}
    write_log_book(fruitsandprices)

# If need to separate Writing Out both item and Price for total purchase in shop with out overwrite
def write_log_book(order_entries):
    file = open('C:\\Users\\balajisriram\\.PyCharmCE2018.1\\config\\scratches\\log_entry.txt', 'a')
    total = 0
    for item, price in order_entries.items():
        file.write(item + ' ' + format(price, '.2f') + '\n')
        total += price
    file.write('total = ' + format(total, '.2f') + '\n\n')
    file.close()

def main():
    fruitsandprices = {'Banana - 1kg': 20, 'Cherry - 300gs': 30, 'Grape - 1kg': 40, 'Watermelon - 2kg': 50}
    write_log_book(fruitsandprices)

main()
# We Don’t Want to Overwrite Our File
# then 'w' to 'a'
def main():
    vegetablesandprices = {'Beetroot - 1kg': 20, 'Tomato - 1kg': 30, 'Carrot - 1kg': 40, 'Potato - 2kg': 50}
    write_log_book(vegetablesandprices)

main()


# Reading the Entire Contents of a File
shopping_items = open('C:\\Users\\balajisriram\\.PyCharmCE2018.1\\config\\scratches\\log_entry.txt', 'r')
print(shopping_items.read())
shopping_items.close()

# Reading an Individual Line From a File
def read_log_entry():
    shopping_items = open('C:\\Users\\balajisriram\\.PyCharmCE2018.1\\config\\scratches\\log_entry.txt', 'r')
    print(shopping_items.readline())
    shopping_items.close()

read_log_entry()


# We can read all of the lines individually in a loop, which will be convenient to add each item to a list.
def read_log_entry():
    shopping_items = open('C:\\Users\\balajisriram\\.PyCharmCE2018.1\\config\\scratches\\log_entry.txt', 'r')
    for item in shopping_items:
        print(item)
    shopping_items.close()

read_log_entry()



