import turtle
import gmpy2
from gmpy2 import mpq

# /////////////// CHOOSE STUFF HERE //////////////

number = mpq(1, 117)  # mpq(numerator, denominator)
draw_this_much_digits = 300  # how many lines (digits) to draw
unit = 20  # how long are the lines

base = 10  # for now, only base10 works

# /////////////// DA PROGRAM /////////////////////

# numbers
gmpy2.get_context().precision = 20000
b = gmpy2.mpfr(number)

# turtle
bob = turtle.Turtle()
bob.speed(10)

# drawing
print("drawing: ", b)
for x in range(draw_this_much_digits):
    # current digit
    n = b // 1
    # TURTLE drawing
    bob.left(int(n*360/base))
    bob.forward(unit)
    # prepare for next digit
    b = (b-n) * 10

bob.hideturtle()
turtle.done()
