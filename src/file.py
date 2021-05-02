my_list = []

try:
    with open('text.txt' , 'rt') as tx:
        my_list.extend(tx.readlines())

    print(my_list)
    print(my_list[5])

except:
    print("Error...")
    
########
try:
    with open('text2.txt' , 'w') as tx:
        tx.write("new test => text2")

    filesname = ['text.txt' , 'text2.txt' ]

    with open('text3.txt' , 'w') as output:
        for names in filesname:
            with open(names) as intext:
                output.write(intext.read())
            output.write('\n')
except:
    print("Error...")

############
import os

if os.path.exists("text3.txt"):
    os.remove("text3.txt")