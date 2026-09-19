namelist = ["ali" , "reza", "amir", "sara"]
it = iter(namelist)

try: 
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("ERROR : StopIteration ")