#output is indented
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
#output splits string into 3 words
backslash_cat = "I'm \\ a \\ cat."

#output is a list of 4 indented strings
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Revisit: Not understanding use case for all escapes below,
# and application of escapes in %r and %s (%r shows raw while %s shows string representation)

# Escape What it does.
# \\ Backslash (\)
# \' Single- quote (')
# \" Double- quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r ASCII carriage return (CR)
# \t ASCII horizontal tab (TAB)
# \uxxxx Character with 16- bit hex value xxxx (Unicode only)
# \Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
# \v ASCII vertical tab (VT)
# \ooo Character with octal value oo
# \xhh Character with hex value hh