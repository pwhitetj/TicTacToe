import os
import fnmatch
import re
import shutil
import pprint

prefix = "/Users/silver/Dropbox/2016-2017/AI/Submissions/TicTacToe/"
data = []
for file in os.listdir(prefix):
    if fnmatch.fnmatch(file, "*.py"):
        b = file.split()
        m = re.match("(.*)\s-\s(.*)",file)
        (name, newfile) = m.groups()
        newfile = newfile.lower()
        m = re.match(".*([1-9])_.*", m.group(2))
        if (m.__class__==None.__class__):
            block = 99
        else:
            block = int(m.group(1))
        data += [(block, name, newfile, file)]

outfile = open("students-index.txt","w")
for (block, name, newfile, file) in sorted(data):
    print("%i;%s;%s;%s" % (block, name, file, newfile), file=outfile)
    shutil.copy(prefix+file, "students/"+newfile)
outfile.close()