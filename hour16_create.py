f = open("tmp.txt", "w+")
f.write("this is a new file")
f.close()
f = open("tmp.txt")
f.readlines()

import os
os.getcwd()