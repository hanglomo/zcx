list1=[24563,9675,87654,976,76783,8745698,765,987345]
list=[]
print(list)
if list1[0]<list1[1]:
   print(list1)
else:
   list1[0],list1[1]=list1[1],list1[0]

if list1[1]<list1[2]:
   print(list1)
else:
   list1[1],list1[2]=list1[2],list1[1]

if list1[2]<list1[3]:
   print(list1)
else:
   list1[2],list1[3]=list1[3],list1[2]

if list1[3]<list1[4]:
   print(list1)
else:
   list1[4],list1[3]=list1[3],list1[4]

if list1[4]<list1[5]:
   print(list1)
else:
   list1[5],list1[4]=list1[4],list1[5]   

if list1[5]<list1[6]:
   print(list1)
else:
   list1[6],list1[5]=list1[5],list1[6]

if list1[6]<list1[7]:
   print(list1)
else:
   list1[6],list1[7]=list1[7],list1[6]

print(list1) 
