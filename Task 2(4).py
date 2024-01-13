import os
files = os.listdir()
for file in files:
    if file.endswith(".jpg"):
        first_name, last_name = file.split("_")
        new_name = f"{last_name}_{first_name}"
        os.rename(file, new_name)
