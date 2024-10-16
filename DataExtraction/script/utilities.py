import os
import re

def getallpaths(currpath):
    inputpath = currpath.replace('script', 'input')
    outputpath = currpath.replace('script', 'output')
    logpath = currpath.replace('script', 'log')
    return inputpath,outputpath, logpath

def getfilenames(inputpath):
    filenames = os.listdir(inputpath)
    return filenames

def extractallData(filenames):

    outputdata = {}

    for x in filenames:
        try:
            print(outputdata[x])
        except KeyError as err:
            outputdata[x] = []

        fvar = open(x,'r')
        data = fvar.read()
        fvar.close()

        dates = re.findall('[0-9]{2}[^A-Za-z0-9][0-9]{2}[^A-Za-z0-9][0-9]{4}', data)
        email = re.findall('[A-Za-z0-9]{1,}@gmail.com', data)
        ips = re.findall('[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}', data)

        outputdata[x].extend(dates)
        outputdata[x].extend(email)
        outputdata[x].extend(ips)

    return outputdata



def appedLog():
    pass

