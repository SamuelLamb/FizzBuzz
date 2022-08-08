# FizzBuzz challenge

# Step 1 is to print all integers from 1 to 100.
# Any mutliples of 3 are replaced with the word "Fizz".
# Any multiples of 5 are replaced/appended with the word "Buzz".
# Any multiples of both 3 and 5 become "FizzBuzz", as multiples of 5 will append "Buzz" to "Fizz".

# Step 2 adds more rules depending on if numbers are multiples.
# Any multiples of 7 are replaced/appended with the word "Bang".
# Any multiples of 11 replace the entire string with the word "Bong".
# Any multiples of 13 insert the word "Fezz" into the string either:
#                                                         Immediately before a word beginning with "B" (This includes the word "Bong").
#                                                         At the end of the string if there are no words beginning with "B".
# Any multiples of 17 reverse the order of the words above in the string (i.e. Instead of returning "FizzBuzz", 3 x 5 x 17 = 255 would become "BuzzFizz").
