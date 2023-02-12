import os
import shutil

from_dir="C:/Users/Recriation/Downloads"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for Move_file in list_of_files:
    name,ext=os.path.splitext(Move_file)
    print(ext)
