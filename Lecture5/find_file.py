import sys
import os
import re

if len(sys.argv) >= 3:
    if os.path.exists(sys.argv[1]):
        print("Directory not found!")
    else:
        search_dir = sys.argv[1]
        file_regex = sys.argv[2]
        pattern = re.compile(file_regex)
        found_files = []

        for dirpath, dirnames, filenames in os.walk(search_dir):
            for filename in filenames:
                if pattern.match(filename):
                    found_files.append(os.path.join(dirpath, filename))

        if len(found_files):
            print(found_files, end='\n')
        else:
            print("File not found")
else:
    print("You should run with dir name and file name as parameters.")

