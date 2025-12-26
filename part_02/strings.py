#this program is practicing string splits and string stuff

text= "ABCD EFGH"
print(text[1:4])
print(text[1:-6])

print(text[:])
print(text[1:-1])
print(text[::2])
print(text[::-1])

#Strings are imutable in python but ...
#Can i do something?

name="Jadi"
name = 'J'+name[1:]
print(name)

print((name+' ')*3)