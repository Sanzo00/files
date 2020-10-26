# coding=utf-8
import os, sys

path = "dir/"
dir = os.listdir("./")

for file in dir:
    if ".mp4" not in file:
        continue
    pos = file.find('.mp4')
    old_name = path + file
    new_name = path + file[:pos] + '.mkv'
    os.rename(old_name, new_name)
