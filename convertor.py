"""
for a give folder, convert recursively all the file names and folders names from PascalCase to snake_case
"""

import os
import re

def convertor(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            new_name = re.sub(r'([a-z])([A-Z])', r'\1_\2', file).lower()
            os.rename(os.path.join(root, file), os.path.join(root, new_name))
        for dir in dirs:
            new_name = re.sub(r'([a-z])([A-Z])', r'\1_\2', dir).lower()
            os.rename(os.path.join(root, dir), os.path.join(root, new_name))


if __name__ == '__main__':
    convertor('./data/templates')