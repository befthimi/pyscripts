'''
This script merges the AP data from two files such that...
'''
#Initialise the list of Access Points
All_My_APs = []
APs_with_intf = []

File_with_intf = open("normalisedList.csv")
File_with_AP_Data = open("All_APs_v3.csv")
NewFile = open("newAPList.csv", "w")

#def normaliseSerialNumber(NonNormalisedSerialNo):
#    """
#    Normalise the Extreme AP Serial numbers by appending '00000'.
#    """
#    print("Non normalised Serial Number: ", NonNormalisedSerialNo)
#    serial_prefix = NonNormalisedSerialNo[:5]
#    if (len(NonNormalisedSerialNo) >= 16) and (serial_prefix == '1736Y'):
#        print("No change to serial number required")
#        NormalisedSerialNo = NonNormalisedSerialNo
#    else:
#        NormalisedSerialNo = NonNormalisedSerialNo + '00000'
#        print("Normalised Serial Number: ", NormalisedSerialNo)
#    return NormalisedSerialNo

for current_line in File_with_AP_Data:
    split_line = current_line.split(",")
#    print(split_line[0])
    All_My_APs.append(split_line)
print ("Seperator --------------")
for current_line in File_with_intf:
    split_line = current_line.split(",")
#    print(split_line[0])
    APs_with_intf.append(split_line)

for f, b in zip(All_My_APs, APs_with_intf):
#    print(f[0], b[0])
    if f[0] != b[0]:
        print("we are foobar'ed")
        print (f[0], ' ', b[0])
    else:
        f[-1] = f[-1].strip()
        f.append(b[1])
        print f
        NewFile.write(','.join(f))

#tempText = ','.join(split_line)
#newfile.write(tempText)
#close all files when done
File_with_intf.close()
File_with_AP_Data.close()
NewFile.close()
