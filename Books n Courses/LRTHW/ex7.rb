#print statement
puts "Mary had a little lamb."
#print statement with string variable
puts "Its fleece was white as %s." % 'snow'
#print statement
puts "And everywhere that Mary went."

puts "." * 10 # what'd that do? <-- this multiplication operater can be applied to strings to repeat themselves. This expression creates a row of dots

#end1 through end12 assigns each letter of cheeseburger to individual variables.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# notice how are using print instead of puts here. Change it to puts
# and see what happens.
puts end1+end2+end3+end4+end5+end6
print end7+end8+end9+end10+end11+end12 #using print does not add a new line while print does add a new line

#this just is polite use of the terminal, try removing it
puts #<-- with this removed the terminal command prompt starts with burger followed by my terminal identity rather than only my terminal identity. A puts at the end of a program gives us a fresh line for our terminal identity. 
