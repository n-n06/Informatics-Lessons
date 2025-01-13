import math

li = [1,4,9,16,-1,9,49,25,4,81] #len(li)=10

for i in range(len(li)):  #
    #i = 0,1,2,3,4,5,6,7,8,9 
    if li[i] < 0:
        break
    else:
        print(math.sqrt(li[i]))
