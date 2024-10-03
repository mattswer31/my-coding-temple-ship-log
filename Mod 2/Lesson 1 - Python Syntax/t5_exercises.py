#1. forgotten quote, pretty sure this is fine as is
print("hello, World!")

#2. mismatched socks: identify logic error
num = 7
if num % 2 == 0: #semi colon was forgotten here
    print("odd") #odd and even should be swapped
else:
    print("even")

#3. logic error, code should greet red only
color = "pink"
if "red" in color:
    print("hello red")
else:
    print("your not red!")

#should be if "red" == color:
#otherwise any word with red in it would trigger hello red