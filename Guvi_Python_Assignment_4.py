
a = int(input("Enter number of names to be entered : "))
names = []
list = input("Enter names : ").split()

for i in range(0,a):
    n = input()
    names.append(n)

print("Capitalized names are : ")
for i in range(0,a):
    print(list[i].capitalize())

#------------------------------------------------------------------------
import mysql.connector

config = {
    'host': 'localhost',
    'user': 'user1',
    'password': 'passowrd123'
    'database': 'db',
}

cur = config.cursor()
cur.execute("CREATE TABLE t1(name VARCHAR(255), age INT)")

sql = "INSERT INTO t1 (name, age) VALUES (%s, %s)"
data = [("Sayli", " 21"), ("Nidhi", " 21")]
cur.execute(sql, data)

config.commit()

select_query = 'SELECT * FROM your_table'
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(f'Name: {row[0]}, Age: {row[1]}')


#------------------------------------------------------------------------------------

a = int(input("Enter number  : "))
rev_no = 0

while a != 0:
    digit = a % 10
    rev_no = rev_no * 10 + digit
    a =  a // 10

print("Reversed Number is : ", rev_no)


#--------------------------------------------------------------------------------

import inflect

f = open("number.txt","r")
a = f.read()
f.close()

p = inflect.engine()
k = p.number_to_words(a)

f = open("number.txt", "a")
f.write(" "+k)
f.close()

f = open("number.txt","r")
a = f.read()
print(a)
