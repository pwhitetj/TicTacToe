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
            block = 9
        else:
            block = int(m.group(1))
        print("%i %20s %30s" % (block, name, file))
        data += [(block, name, newfile, file)]

for (block, name, newfile, file) in data:

    print("cp \"%s\" %s" % (prefix+file, newfile))
    shutil.copy(prefix+file, "students/" + newfile)