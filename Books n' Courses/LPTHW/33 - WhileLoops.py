i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")
for num in numbers:
    print(num)

# FUNCTION VERSION
# def while_loop(start, end):
#     numbers = []
#     while start < end:
#         start += 1
#         numbers.append(start)
#     return numbers
#
# make_numbers = while_loop(5, 20)
# print(make_numbers)

