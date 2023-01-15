#number of total cars
cars = 100
#number of seats in a cars
space_in_a_car = 4.0 #a floating number is a real number, and contains a decimal point
#number of drivers in a car
drivers = 30
#number of people not driving in a car
passengers = 90
#the cars not occupied by drivers out of the 100 total cars
cars_not_driven = cars - drivers
#for a car to drive it must need a driver so the number of cars driven is equivalent to drivers
cars_driven = drivers
#given a number of drivers of cars with a max space of 4 per car we have a total number
carpool_capacity = cars_driven * space_in_a_car
#the total number of passengers divided by the number of cars gives us the average number of passengers per car
average_passengers_per_car = passengers / cars_driven

puts "There are #{cars} cars available."
puts "There are only #{drivers} drivers available."
puts "There will be #{cars_not_driven} empty cars today."
puts "We can transport #{carpool_capacity} people today."
puts "We have #{passengers} passengers to carpool today."
puts "We need to put about #{average_passengers_per_car} in each car."
