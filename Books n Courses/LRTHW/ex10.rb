#first way to escape double and single quotes inside strings
"I am 6'2\" tall." #escape double-quote inside string
'I am 6\'2" tall.' #escape single-quote inside string

#second way of escaping double and single quotes inside strings
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = <<MY_HEREDOC
I'll do a list:
\t* Cat good
\t* Fishies
\t* Catnip\n\t* Grass
MY_HEREDOC

puts tabby_cat
puts persian_cat
puts backlash_cat
puts fat_cat
