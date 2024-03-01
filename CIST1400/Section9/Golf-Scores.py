strokes = int(input())
par = int(input())


if not (3 >= par <= 5):
    res= "Error"
if not (1 <= strokes <= 10):
    res = "Error"

if par - strokes == 2:
    res = ('Eagle')
elif par - strokes == 1:
    res = ('Birdie')
elif par == strokes:
    res = ('Par')
elif par - strokes == -1:
    res = ('Bogey')

print(f"Par {par} in {strokes} strokes is {res}")