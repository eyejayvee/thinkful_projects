# imported sys to allow the use of argv
import sys

# add a coounter variable for the loop
i = 0

# check whether an upper limit argument was added at runtime
try:
  # the argument would be a index 1, index 0 is the name of the python program
  upper_limit = sys.argv[1]
except IndexError:
  # allow the user to enter an upper limit if one was not passed in as an argument
  upper_limit = raw_input("Enter an upper numeric limit for the Fizz Buzz game: ")

# loop while the counter is less than the upper limit provided
# make sure to convert the argument to an integer
while i < int(upper_limit):
  # increment the counter
  i += 1
  if i % 3 == 0 and i % 5 == 0:
    # divisible by 3 and 5
    print "fizz buzz"
  elif i % 3 == 0:
    # only divisible by 3
    print "fizz"
  elif i % 5 == 0:
    # only divisible by 5
    print "buzz"
  else:
    # not divisible by 3 and/or 5
    print i