#program with menu to perform various operations
print('1.prime number','2. square number','3.cube number','4.factorial','5.palindrome number','6.neon number','7.fibonacci series',
'8.armstrong number','9.disarium number','10.harshad number',sep='\n')
print('\n')
var1=int(input('choose one of the operations displayed below:'))
var2=int(input('enter a number of your choice:'))
print('\n')
if var1==1:
    print('FINDING IF A NUMBER IS PRIME NUMBER')
    if var2==0:
        print(var2,"is a prime number")
    elif var2>1:
        for i in range(2,var2):   
            if (var2%i)==0:
                print(var2,"is not a prime number")
                break
        else:
            print(var2,"is a prime number")
    else:
        print(var2,"is not a prime number")

elif var1==2:
    print('FINDING IF A NUMBER IS A SQUARE NUMBER')
    re=var2**0.5
    re=re//1
    if ((re**2)==var2):
        print(var2,"is a square number")
    else:
        print(var2,"is not a square number")
    
elif var1==3:
    print('FINDING IF A NUMBER IS A CUBE NUMBER')
    re=var2**(1/3)
    re=re//1
    if ((re**3)==var2):
        print(var2,"is a cube number")
    else:
        print(var2,"is not a cube number")
    
elif var1==4:
    print('FINDING THE FACTORIAL OF THE GIVEN NUMBER')
    if var2<2:
        print("factorial of",var2,"is 1")
    else:
        n=1
        for i in range(2,var2+1):
            n=n*i
        print("factorial of",var2,"is",n)

elif var1==5:
    print('FIND IF THE NUMBER IS A PALINDROME NUMBER')
    w=str(var2)
    l=len(w)
    sunn=0
    st=''
    while var2>0:
        rem=var2%10
        var2=var2//10
        o=str(rem)
        st+=o
    if w==st:
        print(w,'is a palindrome')
    else:
        print(w,'is not a palindrome')
    
    
    

elif var1==6:
    print('FINDING IF THE NUMBER IS A NEON NUMBER')
    sq=var2**2
    summ=0
    while sq>0:
        rem=sq%10
        summ=summ+rem
        sq=sq//10
    if var2==summ:
        print(var2,'is a neon number')
    else:
        print(var2,'is not a neon number')

elif var1==7:
    print('PRINTING FIBONACCI SERIES TILL THE GIVEN NUMBER:')
    if var2==1:
        print('fibonacci series upto',var2,'terms :',0)
    else:
        n1=0
        n2=1
        c=0
        while c<var2:
            print(n1,end=":")
            n=n1+n2
            n1=n2  
            n2=n
            c+=1
        
        
elif var1==8:
    print('FINDING IF A NUMBER IS AN ARMSTRONG NUMBER')
    summ=0
    we=var2
    while var2>0:
        rem=var2%10
        cu=rem**3
        summ=summ+cu
        var2=var2//10
    if summ==we:
        print(we,'is an armstrong number')
    else:
        print(we,'is not an armstrong number')
    

elif var1==9:
    print('FINDING IF THE NUMBER IS A DISARIUM NUMBER')
    we=var2
    w=str(var2)
    le=len(w)
    summ=0
    while var2>0:
        rem=var2%10
        sq=rem**le
        summ=summ+sq
        le-=1
        var2=var2//10
    if we==summ:
        print(we,'is a disarium number')
    else:
        print(we,'is not a diarium number')

elif var1==10:
    print('FINDING IF THE NUMBER IS A HARSHAD NUMBER')
    rem=sum=0
    n=var2
    while (var2>0):
        rem=var2%10
        sum=sum+rem
        var2=var2//10
    if (n%sum==0):
        print(str(n)+" is a harshad number ")
    else:
        print(str(n)+" is not a harshad number ")

else:
    print('INVALID OPTION! PLEASE ENTER NUMBERS 1-10')
    
    
        
    
    
    
    
    
    
        
    
    
    
    
    


            
            
