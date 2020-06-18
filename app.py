name = input("put your name here ")
if len(name) < 3:
    print("name must be at least 3 character long!")
elif len(name) > 10:
    print("name can be maximum of 10 characters")
else:
    print("this name is okey ;)")