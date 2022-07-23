STAGE = "first"

line = f"This is stage {STAGE}\n"

with open("one.txt", "w") as f:
    f.write(line)
