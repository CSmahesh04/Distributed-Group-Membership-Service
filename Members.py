from Server import process_list
from random import randint
from collections import defaultdict
import json
number = 3
process_status = {}
active_processes = []
passive_processes = []
Membership_list= {}
membership_list_log = []

def create_process_list():
    for i in range(len(process_list)):
      n = repr(process_list[i])
      process = 'm' + n
      with open("processes.json") as file:
         content = file.read()
         if process in content:
             process_status[process] = 'Active'
             active_processes.append(process)
             passive_processes.append(process)








def Membership_List(active_processes, passive_processes, size):

     for i in range(0,size):
         Membership_list.setdefault(active_processes[i],[])
         list = []
         while len(list) < 3:
             n = randint(0, size-1)
             if passive_processes[n] not in list and active_processes[i] != passive_processes[n]:
                   list.append(passive_processes[n])
         Membership_list[active_processes[i]] = list
         #print(list)




def WriteMembership_list(Membership_list):
    with open("membershiplist.json", 'w') as fp:
        json.dump(Membership_list,fp)



def Membership_list_log(Membership_list, membership_list_log):
    with open("Membershiplist.json", "r") as fp:
        dicdump = json.loads(fp.read())
        for key,values in dicdump.items():
            for value in values:
                Message = 'Adding process' + ' ' + value + ' ' +  'to the membership list of' + ' ' + key
                membership_list_log.append(Message)



def Membership_list_log_write(membership_list_log):
    with open('Membershiplist.txt', 'w+') as fp:
        for item in membership_list_log:
            fp.write("%s\n" % item)





create_process_list()
print(process_status)
print(active_processes)
print(passive_processes)
size = len(active_processes)
Membership_List(active_processes,passive_processes,size)
print(Membership_list)
WriteMembership_list(Membership_list)
Membership_list_log(Membership_list,membership_list_log)
#print(membership_list_log)
Membership_list_log_write(membership_list_log)