import csv
import logging
csvfile = open('addr.csv', 'r')
logging.basicConfig(level=logging.DEBUG)
rows=[]
def RequiredCsvData():
        csvreader = csv.reader(csvfile)
        for row in csvreader:
                rows.append(row)
        return(rows)
def addressess(addr):
        ipaddress=addr
        final_list=[]
        for each_list in RequiredCsvData():
                logging.debug(each_list)
                each_dict = {}
                if str(ipaddress) in each_list:
                        print("yes")
                        each_dict['Id'] = each_list[0]
                        each_dict['Object_name'] = each_list[1]
                        each_dict['IP_address'] = each_list[2]
                        each_dict['Owner_name'] = each_list[5]
                        final_list.append(each_dict)
        logging.debug(final_list)
        return(final_list)
def FinalData(addr,mask):
        ipaddress=addr
        subnetmask=mask
        final_list=[]
        for each_list in RequiredCsvData():
                logging.debug(each_list)
                each_dict = {}
                if str(ipaddress) in each_list or str(subnetmask) in each_list:
                        print("yes")
                        each_dict['Id'] = each_list[0]
                        each_dict['Object_name'] = each_list[1]
                        each_dict['IP_address'] = each_list[2]
                        each_dict['Owner_name'] = each_list[5]
                        final_list.append(each_dict)
        logging.debug(final_list)
        return(final_list)
