# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    sentence.lower()
    vowels = ("a", "e", "i", "o", "u")
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    
    return count 


print(get_count("aeiou"))
print(get_count("y"))
print(get_count("bcdfghjklmnpqrstvwxz y"))
print(get_count(""))
print(get_count("abracadabra"))
