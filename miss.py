#create a empty tuple
my_tuple = ()
print(my_tuple)

#tuple having integer 
my_tuple = (10,20,30)
print(my_tuple)

#tuple mix datatypes
my_tuple = ("taysir","age 12",5,"student")
print(my_tuple)

#nested tuple
my_tuple = ("taysir",[1,5,66], (1,2,3))
print(my_tuple)

#slicing tuple
print("Sliced : ",my_tuple[1:4])

#iteration in tuple

for letter in (my_tuple):
    print("Hello",letter)