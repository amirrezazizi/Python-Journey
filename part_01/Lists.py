# here , we meet List (array in C family) in python.

my_list=[2,6,3,8,1]
names=['amir','ali','reza','parsa','ashkan']
print(len(my_list))
print(my_list+names)
print(my_list*2)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)


#methods for List
print("\n")

my_list.append(10)
my_list.append(1)
my_list.append(1)
print(my_list)
print(my_list.count(1))

names.clear()
print(names)
names.append("ali")
names.append("hamed")
names.append(10)
print(names)
num=names.pop()
print(num)
print(names.pop(0))
print(names)

fav=['hamed','dog',20,'ice','red']
fav.remove('dog')
fav.remove('hamed')
print(fav)
fav.insert(0,10)
print(fav)


