import os
import re

cwd = os.getcwd()

for filename in os.listdir(cwd):
    if not filename.endswith(".mp3"):
        continue

    new_filename = re.sub(r'[^\x00-\x7F]', '_', filename)
    print(f"'{filename}' -> '{new_filename}'")
    os.rename(filename, new_filename)

