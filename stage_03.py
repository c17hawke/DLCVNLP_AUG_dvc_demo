STAGE = "three"

line = f"This is stage {STAGE}\n"

with open("one.txt", "r") as f:
    content1 = f.read()

print(f"line from prev stage: {content1}")

with open("two.txt", "r") as f:
    content2 = f.read()

print(f"line from prev stage: {content2}")


with open("three.txt", "w") as f:
    f.write(f"{line}, \n{content1}, \n{content2}")
