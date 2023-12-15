import os

parent_dir_path = str(os.path.dirname(os.path.realpath(__file__)))
root_path = parent_dir_path.replace("/src/utils", "")
print(root_path)