#how to concat string in python

#format string 
name="Amir"
last_name="Azizi"
age=22
print("hello , my name is {} {} and i am  {} years old".format(name,last_name,age))

print("hello {1}, {0} is {2} years old ".format(name,last_name,age))

#verbose >>
print("hiiii {family}, {esm} is {sen} years old".format(family=last_name,esm=name,sen=age))

#precion and width >>
score_amir=150
score_ali= 120
score_salar=95
score_zahra=56
score_parsa=8
score_moein= 7.56
score_reza= 22.76
print(" got : {0:6.1f}".format(score_amir))
print(" got : {0:6.1f}".format(score_ali))
print(" got : {0:6.1f}".format(score_salar))
print(" got : {0:6.1f}".format(score_zahra))
print(" got : {0:6.1f}".format(score_parsa))
print(" got : {0:6.1f}".format(score_moein))
print(" got : {0:6.1f}".format(score_reza))

# f String method

print(f"hello my name is {name} {last_name} and i am {age} years old.")