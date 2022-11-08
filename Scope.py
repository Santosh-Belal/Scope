x=89#it was Changed to 98.

def Santosh ():

    x=10#It is Local value

    def Belal():

        

        global x

        x=98

    print("Hello Im Santosh Belal", x)#Value of x will syll 10

    Belal()

    print("Hello im Participating in 30Days Challenges",x)

    

Santosh()

print(x)a = 10#Global

def my_func(n):

    #a=5#Local #If i comment this and print a it will print 10

    b=12#Local#Now i have permission to print  and Change Global a

    global a

    a = a +100

    print(a,b)#Output is 5,12 cause it is inside Function

    print(n, "How are you ?")

my_func("Santosh")

print(a)
