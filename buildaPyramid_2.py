height = int(raw_input("What is the height of the pyramid? "))
line = 1
stars = "*"

while line < (height + 1):
    gap = " " * (height - line)
    print gap + stars
    stars = stars + ("*" * 2)
    line += 1
