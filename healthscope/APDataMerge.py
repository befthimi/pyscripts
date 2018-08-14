'''
This script merges the AP data from two files such that...
'''
#Initialise the list of Access Points
All_My_APs = []

#Initialise the new list of Access Points
newfile = open("myNewAPlist.csv", "w")

#def snmp_get(whichrouter, which_oid):
#    """
#    Get snmp result based on which router and OID
#    """
#    snmp_data = snmp_helper.snmp_get_oid_v3(whichrouter, snmp_user, oid=which_oid)
#    snmp_result = int(snmp_helper.snmp_extract(snmp_data))
#    return snmp_result

with open('All_APs_v3.csv') as f:
    for current_line in f:
        split_line = current_line.split(",")
        All_My_APs.append(split_line)
        print len(All_My_APs)
        print split_line[0], ' ', split_line[1], ' ', split_line[2], ' ', split_line[3]
        tempList = [split_line[0], split_line[1], split_line[2]], split_line[3]
        tempText = ','.join(tempList)
        tempText += '\n'
        newfile.write(tempText) 

#close all files when done
f.close()
newfile.close()

