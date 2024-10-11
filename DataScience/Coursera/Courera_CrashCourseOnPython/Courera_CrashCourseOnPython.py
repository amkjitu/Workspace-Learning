#print("how are jitu?")
'''
#Sum of divisors
def sum_divisors(n):
    sum = 0
    divisor=1
    while(divisor<n):
    # Return the sum of all divisors of n, not including n
        if(n%divisor==0):
            sum+=divisor
        divisor+=1          
    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
#print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
#print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
'''
'''
def prime_fector(n):
       fector = 2;
       while(fector<=n):
                   if(n%fector==0):
                       print(fector)
                       n=n/fector
                   else:
                       fector+=1;

prime_fector(100)
'''

'''
def digits(number):
    count=0
    if(number == 0):
        return 1
    while(number>0):
        number=int(number/10)
        count+=1
        print(number)
    return count

print(digits(1000))
'''

'''
#unsolved
def counter(start, stop):
	x = start
	if ___:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if ___:
				return_string += ","
			___
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"
'''


'''
#unsolved
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for ___:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if ___:
			new_string = ___
			reverse_string = ___
	# Compare the strings
	if ___:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
'''

'''
##unsolved
#The permissions of a file in a Linux system are split into three sets of three permissions: 
#read, write, and execute for the owner, group, and others. 
#Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, 
#and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#For example: 
#640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
#Fill in the blanks to make the code convert a permission in octal format into a string format.
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for ___ in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if ___ >= value:
                result += ___
                ___ -= value
            else:
                ___
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
'''

'''
for x in range(10):
    for y in range(x):
        print(y,end = ' ')

for x in range(1, 10, 3):
    print(x)
'''
'''
#count letters in a word(ignoring white space)
def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result and letter != " ":
            result[letter] = 1
        elif(letter != " "):
           result[letter] +=1
    return result

print(count_letter("jitu is jitu"))
'''

'''
#count words in a texts(ignoring ,.?.\'' etc)
def count_word(text):
    words = text.split()
    final_words = [w for w in words if w.isalpha()]
    for index, x in enumerate(final_words):
        final_words[index] = x.lower()
    final_words.sort()
    #print(final_words)
    word_count = {}
    for word in final_words:
        new_word=""
        for letter in word:
            if letter >= 'A' and letter <= 'z':
                new_word+=letter
                #print(new_word+" "+letter)
        #final_words.append(new_word)
        if new_word not in word_count:
            #print(new_word)
            word_count[new_word]=1
        else:
             #print(new_word)
             word_count[new_word]+=1
        
    return word_count
    #return words

w = count_word("Hello there! How are you ? Hope all of you are very fine")

for key, item in w.items():
    print("{} {}".format(key, item))
'''

'''
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for x,y in wardrobe.items():
	for value in y:
		print("{} {}".format(value,x))
#for example: "red shirt", "blue shirt", "white  shirt".
'''

'''
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
w = wardrobe.update(new_items)
print(w)
'''

def highlight_word(sentence, word):
   new_senten = ""
   if (word in sentence):
      index = sentence.find(word)
      l =  len(word)
      n = sentence[index:index+l].upper()
      new_senten = sentence[:index] + n + sentence[index+l:]
   return new_senten	

	#return(if (sentence.find(word)) sentence[] )

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))