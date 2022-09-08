#decler value for x variable
x = "There are #{10} types of people."
#declare string value for binary variable
binary = "binary"
#declare string value for do_not variable
do_not = "don't"
#declare string value of y variable
y = "Those who know #{binary} and those who #{do_not}."

#print x variable contents
puts x
#print y variable contents
puts y

#print x with a premise
puts "I said #{x}."
#print y with a premise with a little string interpolation to inject the y value
puts "I also said: '#{y}'."

#give a binary value to the hilarious variable
hilarious = false
#declare string value to joke_evaluation variable
joke_evaluation = "Isn't that joke so funny?! #{hilarious}"

#print joke_evaluation variable contents
puts joke_evaluation

#declare string value of w variable
w = "This is the left side of..."
#declare string value of e variable
e = "a string with a right side."

#print a combination of string values, or concatenation
puts w + e
