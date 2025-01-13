li = [1,2,3,4]

li.append(5)
print(li)

li.insert(2, 0)
print(li)


li_dlc = [6,7,8]
li.extend(li_dlc)
print(li)

li += li_dlc
print(li)

print("Deleted element: ", li.pop(5)) # -1
print(li)

li.remove(0)
print(li)



