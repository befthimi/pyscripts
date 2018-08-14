'''
This script normalises the serial number for APs in the list such that it includes the training '00000'
'''
#Initialise the new file to write the full seial number
newfile = open("normalisedList.csv", "w")

def normaliseSerialNumber(NonNormalisedSerialNo):
    """
    Normalise the Extreme AP Serial numbers by appending '00000'.
    """
    print("Non normalised Serial Number: ", NonNormalisedSerialNo)
    serial_prefix = NonNormalisedSerialNo[:5]
    if (len(NonNormalisedSerialNo) >= 16) and (serial_prefix == '1736Y'):
        print("No change to serial number required")
        NormalisedSerialNo = NonNormalisedSerialNo
    else:
        NormalisedSerialNo = NonNormalisedSerialNo + '00000'
        print("Normalised Serial Number: ", NormalisedSerialNo)
    return NormalisedSerialNo

with open('Book1v3.csv') as f:
    for current_line in f:
        split_line = current_line.split(",")
        split_line[0] = normaliseSerialNumber(split_line[0])
        print(split_line[0], ' ', split_line[1])
        tempText = ','.join(split_line)
        newfile.write(tempText)
#close all files when done
f.close()
newfile.close()
