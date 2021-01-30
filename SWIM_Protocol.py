from SWIM import membership_process
import time
import json
crash_list = []
process_crash_list = []
process_active_list = []
with open('crashed_processes.json') as fp:
    crashes = json.load(fp)

    print("printing crashes")
    print(crashes)


for key,values in membership_process.items():
     key_value = key
     for value in values:
         value_key = value
         print(key_value + " " + " process pinging the process" + " " + value_key)

         if crashes[value_key] == 'crashed' and value not in process_crash_list:
             time.sleep(10)
             print(value_key + " " + "process is not responding to the ping request")
             process_crash_list.append(value)
         elif crashes[value_key] == 'Active' and value not in process_active_list:
             time.sleep(2)
             print(value_key + " " + "is responding to the ping request")
             process_active_list.append(value)



for key, value in crashes.items():
    if crashes[key] == 'crashed' and key not in process_crash_list:
        time.sleep(10)
        print("Process" + "  " + key + "  " + "is not responding to the ping request")
        process_crash_list.append(key)


print(process_crash_list)
print(process_active_list)