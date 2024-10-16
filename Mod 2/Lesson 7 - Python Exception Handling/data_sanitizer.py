values = ["1", "string", "32.0", "boof", "3", "5"]
parsed_ints = []
for value in values:
    try:
        parsed_ints.append(int(value))
    except ValueError:
        print(f"{value} is not able to be converted to an int.")
print(parsed_ints)