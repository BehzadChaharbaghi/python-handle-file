my_list = []

try:
    with open('text.txt' , 'rt') as tx:
        my_list.extend(tx.readlines())

    print(my_list)
    print(my_list[5])

except:
    print("Error...")

