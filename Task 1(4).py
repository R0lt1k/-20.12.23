import os
import shutil

os.mkdir("watch_me")

video_files = os.listdir("video")
for file in video_files:
    source = os.path.join("video", file)
    destination = os.path.join("watch_me", file)
    shutil.move(source, destination)

sub_files = os.listdir("sub")
for file in sub_files:
    source = os.path.join("sub", file)
    destination = os.path.join("watch_me", file)
    shutil.move(source, destination)
