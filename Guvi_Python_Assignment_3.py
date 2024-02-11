def check(x):
    if x%2==0:
        print("Number is even")
    else:
        print("Number is odd")

num = int(input("Enter a number : "))
check(num)

 #----------------------------------------------------------

def check(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
n2 = int(input("Enter a number : "))
if check(n2):
    print("Prime")
else:
    print("Not prime")


#----------------------------------------------------------------

terms = int(input("How many terms do you need in the fibonacci series : "))
n1,n2 = 0,1
count = 0

if terms<0:
    print("Invalid Input")
elif terms == 1:
    print("Fibonacci Series upto ", terms, "term is ", n1)
else:
    print("Fibonacci Series is : ")
    while count<terms:
        print(n1)
        next_term = n1 + n2
        n1 = n2
        n2 = next_term
        count +=1



    





            
