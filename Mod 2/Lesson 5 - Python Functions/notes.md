built in functions
print()
\n = new line
\t = tab
\\ = backslash
+
print("apple", "babn", "cher", sep= "-", end="...yum")
returns apple-babn-cher...yum
print(f"value of pi is {pi:.2f}")
returns value of pi is 3.14
, add spaces unlike +
concatenation + is more expensive but faster unless you do a lot

input() always returns a string
convert with str() bool() int() or float()
bool("anything") returns true
bool("") returns false
type() returns type of variable
len() returns length of str or items in list
isinstance(item, type) checks if something is what it claims

abs() finding absolute value
round() rounds numbers to nearest whole
sum() totals it up
min() and max() bring smallest and largest
pow() when numbers to bulk
divmod() fair division and whats left
sqrt() root of a number
ceil() floor() handle decimals, ensure numbers fall where we want
exp() and log() for expo growth or log patterns
sin() cos() tan() trig operations
radians() degrees() convert degrees and radians

functions
def dog(treat=chicken)
treat can be defined otherwise it will default to chicken
def dog(*treats)
    for treat in treats
        print(treat)
can pass a variable number of args to dog'

**kwargs
def make sandwich(**ingredients):
    for item, quantity in ingredients.items():
        print(f"adding {quantity} of {item} to sandwich)
make_sandwich(tomatoes="3 slices", lettuce = "2 leaves", mayo = "1 spread")
returns
Adding 3 slices of tomato to the sandwich etc.

def get details():
    return name, age
var1, var2 = get_details()
print(var1, var2)

counter =0
def func():
    global counter # this uses the above var

pdb = gps for code to debug
import pdb; pdb.set_trace()