#dictionary will go here. 
#function will go here. 
import random
import string 
encode_code_words = {
    1 : "A",
    2 : "BE",
    3 : "FOR",
    4 : "JOKE",
    5 : "SUNNY",
    6 : "FUNNIE",
    7 : "BLUEJAY",
    8 : "SIBERIAN",
    9 : "JAZZINESS",
    10 : "PUZZINGLYM",
}

#create the dictionary for the code
alphabet_lower = list(string.ascii_lowercase)
num_list = list(range(1, 27))
encoding_list = dict(zip(alphabet_lower, num_list))
reverse_encoding_list={y:x for x,y in encoding_list.items()}
print(encoding_list)

# for letter in alphabet_lower:
    

#encode function is going to take a message and give out 1. code word and 2. encription of the original message
def encode(message):
    #this is the 
    final_encoded = "" 
    number = random.randint(1, 11)
    key_word = encode_code_words[number]
    message = message.lower()  
    #we have the key word set, and we know the number. 
    #run along each letter in message. 
    for char in range(0, len(message)):
        if message[char] in alphabet_lower:
            char_letter=message[char]
        # """9 
        # IT IS A LETTER:
        # Check which number it is. 
        # Add random number we chose above to it. 
        # Check to see if that is less than 27.
        # IF IT IS LESS THAN 27:
        #     make it the letter corresponding to the sum it has become. 
        # IF IT IS GREATER THAN 27
        #     make it the letter corresponding to sum - 26"""
            new_index=encoding_list[message[char]]+(number)
            if new_index<27:
                print("New index is under 27")
                final_encoded+=reverse_encoding_list[new_index]
            else:
                new_index=new_index-26
                final_encoded+=reverse_encoding_list[new_index]
        else:
            final_encoded+=message[char]
    return "Your key word is: " + key_word + " and your encoded message is: " + final_encoded 
"""
    aPpLe
    a = 0 each character. 
    p = 1
    p = 2 
    find the lowercase of the corresponding character. 
    build in a check to see if it's a letter 
        ^ by SEEING IF IT IS IN ENCODING LIST. 
    
    IT IS A LETTER:
        Check which number it is. 
        Add random number we chose above to it. 
        Check to see if that is less than 27.
        IF IT IS LESS THAN 27:
            make it the letter corresponding to the sum it has become. 
        IF IT IS GREATER THAN 27
            make it the letter corresponding to sum - 26
    
"""
        
    

#  def decode(message) :
#   ##printing the original decoded string  
#   #Take the final message + key (new_index)
#   #Check the number of the letter 
#   #print "The decoded string is : ", 

#   alphabet_lower[new_index] - final_encoded
#         if 
#     print str_enc.decode(', '') 

# #encode: 
# """ 
# ENCODE
# TAKE IN MESSAGE TO BE SCRAMBLED.
# SPIT OUT CODE WORD AND A SCRAMBLED. 
#     RANDOM
#     RANDOM.RANDINT(1, 11)
#     {1 : "A"
#     2 : "BE"
#     3 : "FOR
#     4 : 
#     }
# """



# # # Code out your function definitions here
# # ## The Goal

# # There are a couple of different ways to do this, but the goal is simple: create two functions, one called encode, the other called decode. Each method should take two arguments (the string you'd like to encode, and the offset of the cipher).

# # Try writing lines of code to test your file in the testcipher.py file:

# # ###### Code to test your encode method.

# # ```python
# # print(cipher.encode("Python is fun", 8)) # => prints out the string "Xgbpwv qa ncv"
# # ```
    


# # ###### Code to test your decode method.

# # ```pytho
# # print(cipher.decode("Xgbpwv qa ncv", 8)) # => prints out the string "Python is fun"
# # ```

# # ## Push Yourself!

# # Here are some questions you can ask yourself for when your code is finished - if the answer to any of them inspires you to add some functionality to your program, then go for it!

# # * Does your cipher handle upper and lowercase letters well?
# # * What does your cipher do with punctuation? Is that what you want?
# # * What does your cipher do if the user doesn't KNOW the offset? Can you think of a way to write a decode message that can work with the user to crack an unknown code?