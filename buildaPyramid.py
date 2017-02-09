height = int(raw_input("What is the height of the pyramid? "))

for i in range(height):
    if i == 0:
        stars = "*"
    else:
        stars = stars + ("*" * 2)
    gap = " " * (height - (i + 1))
    print gap + stars
