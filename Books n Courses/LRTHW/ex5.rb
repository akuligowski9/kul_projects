name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
book = "LRTHW"
kilos = weight*0.453592
centi = height*2.54

puts "Let's talk about %s." % name
puts "He's %d inches tall, or %d centimeters." % [height, centi]
puts "He's %d pounds heavy, or %d kilograms" % [weight, kilos]
puts "Actually that's not too heavy."
puts "He's got %s eyes and %s hair." % [eyes, hair]
puts "His teeth are usually %s depending on the coffee." % teeth
puts "When he isn't drinking coffee he's probably writing %s." % book

# this line is tricky, try to get it exactly right
puts "If I add %d, %d, and %d I get %d." % [age, height, weight, age + height + weight]
