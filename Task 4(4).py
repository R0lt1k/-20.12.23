with open("input.txt", "r") as f:
    lines = f.readlines()

edited_lines = lines[:-1]

with open("output.txt", "w") as f:
    f.writelines(edited_lines)
