import os

directory = "personal_info/"
outfile_name = "merged_personal_info.txt"

out_file = open(outfile_name, 'w')

files = os.listdir(directory)

for filename in files:
    if ".txt" not in filename:
        continue
    file = open(directory + filename)
    for line in file:
        out_file.write(line)
    out_file.write("\n\n")
    file.close()
out_file.close()
