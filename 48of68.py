'''
Jamie W Bryant
January 26, 2017
'''
       
#####List 1       
def insertion(list1):
   for index in range(1,len(list1)):

     currentvalue = list1[index]
     position = index

     while position>0 and list1[position-1]>currentvalue:
         list1[position]=list1[position-1]
         position = position-1
     list1[position]=currentvalue

list1 = [67, 45, 2, 13, 1, 998]
insertion(list1)
print(list1)

########List 2

def insertion2(list2):
   for index in range(1,len(list2)):

     currentvalue = list2[index]
     position = index

     while position>0 and list2[position-1]>currentvalue:
         list2[position]=list2[position-1]
         position = position-1

     list2[position]=currentvalue
     


list2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]

insertion2(list2)
print(list2)
