import json
crashed_process = {}
processes =[]
string = 'crashed'

with open('crashed_processes.json') as fp:
          crashed_process = json.load(fp)

with open("membershiplist.json") as fs:
        membership_process = json.load(fs)


print(crashed_process)
print(membership_process)

for key,value in crashed_process.items():
        if value == string:
            processes.append(key)


n = len(processes)

for i in range(n):
    del membership_process[processes[i]]


print(membership_process)

