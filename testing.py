review = "this thing is great! loved it."

new = []
new += review.split(' ')
keywords = ["great", "love"]
for i in new:
    for j in range(len(keywords)):
        if keywords[j] in i:
            new[new.index(i)] = i.upper()

converted = " ".join(new)
print(converted)