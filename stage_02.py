STAGE = "two"

line = f"This is stage {STAGE}\n"

with open("one.txt", "r") as f:
    content = f.read()

print(f"line from prev stage: {content}")

with open("two.txt", "w") as f:
    f.write(line)
