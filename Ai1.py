A=int(input("Enter a number: "))
B=int(input("Enter a next number: "))

for i in range(A,B):
    if i%2==0:
        
        print( i,end="\t\t")
    else:
        
        print( i,end="\n")
    