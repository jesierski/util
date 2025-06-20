from pathlib import Path
import os

# Assign directory
directory = "<here is your desired directory>"
print("***********************")
os.remove("totalcontents.txt")


# Iterate over files in directory
def files_content_walk(start_path="."):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if not file.endswith(
                (".xml", ".java", ".txt")
            ):  # modify extensions at wish
                print("This file does not have a valid extension.")
            else:
                # add content of file found to file with total contents
                print(os.path.join(root, file))
                with open("totalcontents.txt", "a", encoding="utf-8") as f:
                    contents = Path(os.path.join(root, file)).read_text(encoding="utf-8")
                    f.write(contents)
                    f.write("\n")


# Specify the directory you want to start from
files_content_walk(directory)
