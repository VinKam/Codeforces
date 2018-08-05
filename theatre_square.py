import math

dimensions = input()

n,m,a = dimensions.split()

n,m,a = int(n),int(m),int(a)

max = max(n,m)
min = (n+m)-max

if(a>=max):
    print(1)
else:
    count = math.floor(max/a)
    if(max%a != 0):
        count += 1
    if(max != min):
        if(a >= min):
            print(count)
        else:
            count2 = math.floor(min/a)
            if(min%a != 0):
                count2 += 1
            print(count*count2)
    else:
        print(count*count)
