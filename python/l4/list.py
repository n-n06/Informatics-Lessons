li = [400,24,34,-5]
a = 2
b = 3
c = 4

li = [b,c,a] #b = 3
print(li)

# index from 0 
print(li[1])


# index from 0 to 11 
li2 = [1,6,8,30,20,11,13,45,17,3,2,4] #len(l2) = 12

# index from 0 to 4
li3 = [1,2,3,4,5] # len(li3) =  5

# index from 0 to 1
li4 = [5,6] # len(li4) = 2

print(li2[-3])


'''
Indexing
1. start from 0
2. go to len(li) - 1
3. can be < 0 => count elements from the back
4. change byindex
5. slice




'''

li5 = [1,2,3,4,5,10249]
# last elemtns in li5 - incorrect, change last elemnts in li5,  make it 6
li5[-1] = 6
print(li5)

