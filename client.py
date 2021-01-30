import time
import json
from Server import machines


group_list = {}
LogStash = {}

def add_process(group_list,process,time_value, message, time):
   result =  check_data(process)
   if result is True:
       replace_process(process,time_value,group_list, time)

   elif result is False:

      group_list[process] = time_value
      LogStash[process] = message
      log = open("logstash.json", 'a')
      json.dump(LogStash, log)
      log.write(",\n")

      print(group_list)
      fh = open("processes.json", 'a')
      json.dump(group_list, fh)
      fh.write(",\n")


def check_data(process):
    with open('processes.json') as file:
        content = file.read()
        print(type(process))
        if process in content:
            return True
        else:
            return False

def delete_process(process, time):
    with open("processes.json", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        message = 'Removing the process from the Group List at' + ' ' + time
        LogStash[process] = message
        log = open("logstash.json", 'a')
        json.dump(LogStash, log)
        log.write(",\n")
        for line in new_f:
            if process not in line:
                f.write(line)
        f.truncate()



def replace_process(process, time_value, group_list, time):

    with open("processes.json", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if process not in line:
                f.write(line)
        f.truncate()

    group_list[process] = time_value
    message = 'ReEntering the group list at' + ' ' + time
    LogStash[process] = message
    log = open("logstash.json", 'a')
    json.dump(LogStash, log)
    log.write(",\n")
    sh = open("processes.json", 'a')
    json.dump(group_list, sh)
    sh.write(",\n")


choice = int(input("Press 1 to add machines and Press 2 to remove(leave) machines"))
if choice == 1:
   input= int(input("enter the machine name"))
   value = machines.get(input)
   time = repr(time.time())
   input_1 = repr(input)
   process = 'm' + input_1
   time_value = time + ' ' + value
   message = 'Entering the Group List at' + ' ' + time
   add_process(group_list,process,time_value, message, time)

elif choice == 2:
    input = int(input("enter the machine name you wish to remove"))
    input_1 = repr(input)
    process = 'm' + input_1
    time = repr(time.time())
    delete_process(process, time)

