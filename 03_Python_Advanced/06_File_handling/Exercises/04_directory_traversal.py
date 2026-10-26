import os

files_collections = {}

for root, dirs, files in os.walk("."):
    if root.count(os.sep) <= 1:
        for file in files:
            if file == "report.txt":
                continue
            name, ext = os.path.splitext(file)
            if ext == "":
                continue
            if ext not in files_collections:
                files_collections[ext] = [name]
            else:
                files_collections[ext].append(name)

files_collections = dict(sorted(files_collections.items(), key=lambda x: x[0]))
for extension, files in files_collections.items():
    files_collections[extension] = sorted(files)

with open("report.txt", "w") as report_file:
    for extension, files in files_collections.items():
        report_file.write(extension + "\n")
        for file in files:
            report_file.write(f"- - - {file+extension}\n")