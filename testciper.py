import cipher
#variable for encode function
#variable for decode function 
# Code out your tests here

choice = input("Would you like to decode or encode? Press 1 for decode, 2 for encode: ")
if int(choice) == 1:
    print("encoding")
    my_message =  input("What message would you like to encode? ")
    print(cipher.encode(my_message))
elif int(choice) == 2:
    #run function from cipher to encode
    print("wip")