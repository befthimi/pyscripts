'''
This script merges the AP data from two files.
The first column matches the serial number of the devices.
The second column, of the "newData" file is appended to the 'AP_Data' file.
'''
#Initialise the list of Access Points
All_My_APs = []
newData_List = []

#open existing files for read
File_with_newData = open("APs_controllers.csv")
File_with_AP_Data = open("HS_AP_List.csv")
#open new file with write
NewFile = open("newAPList.csv", "w")

#create list of existing data
for current_line in File_with_AP_Data:
    split_line = current_line.split(",")
#    print(split_line[0])
    All_My_APs.append(split_line)
print ("Seperator --------------")
#create list of new data to merge
for current_line in File_with_newData:
    split_line = current_line.split(",")
#    print(split_line[0])
    newData_List.append(split_line)

#merge new data by checking that serial numbers match first
for f, b in zip(All_My_APs, newData_List):
#    print(f[0], b[0])
    if f[0] != b[0]:
        print("we are foobar'ed")
        print (f[0], ' ', b[0])
    else:
        f[-1] = f[-1].strip()
        f.append(b[1])
        print f
        NewFile.write(','.join(f))

#close all files when done
File_with_newData.close()
File_with_AP_Data.close()
NewFile.close()
