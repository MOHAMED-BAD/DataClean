x=input('').split()
n, m=[int(i) for i in x]
k=0
for i in  range(1,n+1,1):
        for  j in range(1,m+1,1):
            if (i % 2 != 0):
                print("#",end='')
            else:
                if (i % 2 == 0 and i % 4 == 0):
                    k = 1;
                elif (i % 2 == 0):
                        k = m
                if (k != j):
                    print(".",end='')
                else:
                    print('#',end='')
        print()          
                    
