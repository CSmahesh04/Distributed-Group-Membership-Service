import json



def print_logs():
    with open("logstash.json", "r") as f:
     new_f = f.readlines()
     f.seek(0)
     for line in new_f:
        print(line)




print_logs()