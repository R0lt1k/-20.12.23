import os
import shutil
os.mkdir("list")
with open("list.tsv", "r") as f:
    file_names = f.read().splitlines()

for file_name in file_names:
    source = os.path.join(".", file_name)
    destination = os.path.join("list", file_name)
    shutil.move(source, destination)
