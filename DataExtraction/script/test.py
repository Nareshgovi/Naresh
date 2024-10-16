from utilities import *


# egtting the current path
currpath = os.getcwd()
inputpath,outputpath, logpath = getallpaths(currpath)

allinputfiles = getfilenames(inputpath)
print(allinputfiles)

newfilenames = []
for x in allinputfiles:
    temp = inputpath + "\\" + x
    newfilenames.append(temp)

# print(newfilenames)

finalres = extractallData(newfilenames)
# print(finalres)

for k,v in finalres.items():
    print(k , "====> ", v)