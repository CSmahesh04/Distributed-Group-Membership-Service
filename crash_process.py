from Members import process_status
import time
import json



def crash_process(process_status,process):
    for key in process_status.keys():
        key_value = repr(key)
        if process == key_value:
            process_status[key]  = 'crashed'











n  = int(input("Enter the number of processes you want to crash"))
count = 1
for i in range(n):
    n = (input("Enter the process name"))
    process = repr(n)
    var = None
    if count % 3 == 0 and count != 0:
        print(count)
        var = True
        if var == True:
            time.sleep(20)
            var = False

    crash_process(process_status,process)
    count+= 1




print(process_status)

with open('crashed_processes.json', 'w') as fp:
    json.dump(process_status, fp)



