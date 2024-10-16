## step 1 : first go to input folder and read the file data in to lisyformat

fvar = open(r'D:\SANTHOSH\Python_Projects\vodafoneBilling\input\9986019198.txt', 'r')
data = fvar.readlines()
fvar.close()

del data[0]
# print(data)

# step 2 : go through each and every line split based on # and extract each data

isdduration = 0
custid = ''
stdcallduration = 0
stdcount = 0
isdcount = 0
freecount = 0
freecallduration = 0

for x in data:
    x = x.strip('\n')
    temp = x.split('#')
    print(temp[3])
    custid = temp[0]
    calltype = temp[-1]

    if(calltype == "std"):
        stdcount += 1
        stdcallduration += int(temp[3])

    elif(calltype == "isd"):
        isdcount += 1
        isdduration += int(temp[3])

    elif (calltype == "free"):
        freecount += 1
        freecallduration = 0


print("std calls = ", stdcount , stdcallduration)
print("isd calls = ", isdcount , isdduration)
print("free calls = ", freecount , freecallduration)


# # finding the total bill amount

stdtotalmins = stdcallduration / 60
stdtotalmins = round(stdtotalmins,2)

print("total std call duration is ", stdcallduration , " and total mins consumed is ", stdtotalmins)

# find out the amount per call its 2 rs for std call

stdtotalmount = stdtotalmins*2
taxamt = stdtotalmount*0.1
stdfinalbill = stdtotalmount + taxamt
print("std bill for " , custid , " is " , stdfinalbill , " rupees" )


isdtotalmins = isdduration / 60
isdtotalmins = round(isdtotalmins,2)

print("total isd call duration is ", isdduration , " and total mins consumed is ", isdtotalmins)

# find out the amount per call its 2 rs for std call

isdtotalmount = isdtotalmins*7.5
taxamt = isdtotalmount*0.1
isdfinalbill = isdtotalmount + taxamt
print("isd bill for " , custid , " is " , isdfinalbill , " rupees" )


totalmobilebill = stdfinalbill + isdfinalbill
print("Total Mobile bill - ", round(totalmobilebill,2))



