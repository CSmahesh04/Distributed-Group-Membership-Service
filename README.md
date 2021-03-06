<h1 align='center'>DISTRIBUTED GROP MEMBERSHIP SYSTEM</h1> 

I have built a distributed service which maintains, at each machine, a list of machines that are connected to it. This mimics a real life distributed system where machines 
connected to each have a way to recognize when another machine has failed and to disseminate this information to the remaining machines in the connection.
We are able to do the following operations to update/change the membership list:

1. A machine joins the group.
2. A machine voluntarily leaves the group.
3. A machine crashes from the group (Assuming the machine does not recover for a long time).


## System Design Requirements 
<details>
<a name="Design Requirements"></a>
<summary>Show/Hide</summary>
<br>
 
Within a group of machines, when a machine joins or rejoins, there must be a timestamp, IP address and name of the machine. Failure of a machine must be reflected in at least one
membership list within 10 seconds and it must be no longer than 10 seconds, no matter what the network latencies might be. Any change/update to a list must be disseminated 
to all other lists within 15 seconds.

The system must be able to scale to large numbers of machines. For the purpose of this project I have chosen a lower bound of at least 5 machines active at any given time. Only a 
classic <strong>ping-ACK</strong> style of failure detection should be used (<strong>MUST</strong> implement SWIM-style dissemination), hearbeating is not allowed.
A minimum number of pings must be used to reduce traffic load, so no random pinging or ping-to-all.

There will be at most 3 machine failures consecutively throughout the system. There should be no leader or central machine/node, as its failure needs to be detected as well. 
Logs have to be created at each machine, recording when a machine has joined, left or crashed from the network. The logs can include as much information as you want, but primarily
must include:
1. Each time a change is made to the local membership list (join, leave or failure).
2. Each time a failure is detected or communicated from one machine to another.
</details>

## Implementation
<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
<br>
 
I have designed and built this project using the principles of Microservices, which includes various loosely coupled modules which interact with each other to produce the expected result. A Microservices architecture gives us the option to easily add or remove modules without making drastic changes to the overall code base. This gives us the option of scalability if we choose to do so.

To implement the SWIM-style failure dissemination system I heavily utilized a dynamic data structure (Hash-maps) which scales easily without any collisions. This lets us add many machines to the system without having to worry about scalability. The time complexity of looking up an element is a constant in a hash-map, which allows for quick lookups and value retrieval. The time complexity of adding a new machine is linear and hence the worst time case is **O(N)**. This will scale very well with the addition of new machines.

The hash-maps were used to store key-value pairs for each of the machines and their respective members in the list. The SWIM algorithm was implemented where a machine P<sub>i</sub>
pings a machine P<sub>j</sub> in its membership list. Upon waiting for an ACK for 5 seconds, it requests the other members in its list to ping P<sub>j</sub>. Machine P<sub>i</sub> 
waits another 10 seconds for ACKs from any of the members in the list and upon not receiving even a single ACK it declares P<sub>j</sub> as crashed, logs the IP address and
timestamp in the log and then pings to every other member in its list. Now every member sends this information to every other member in their list. This is how information is 
disseminated in the system.
</details>

## File Descriptions
<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
<br>
 
* **_server.py_**: This file consists of the list of all available machines and their respective IP
addresses in the system.

* **_client.py_**: This file takes care of all the machines wanting to join and leave the system.

* **_processes.json_**: This JSON file consists of the machines which have been created and
deleted. This JSON file is used to maintain data persistency.

* **_logstash.json_**: This file maintains a record of when a process joins at a particular time and
when a process leaves at a particular time and also at re-joining along with timestamps
for any event.

* **_members.py_**: This file holds the membership lists of all the machines, including the
statuses of the machines.

* **_membershiplist.json_**: This file contains the membership lists of each individual machine
and we use this file to maintain data persistency.

* **_membershiplists.txt_**: This txt file contains the logs of the membership list.

* **_serverlog.py_**: This file is used to print the server logs.

* **_crashprocess.py_**: This file is used to crash machines in the system with a maximum of 3
machines at a time.
 
* **_crashprocesses.json_**: This process contains all the crashed machines separately. Again, we
use JSON files to maintain data persistency.

* **_SWIM_protocol.py_**: This is used to implement the SWIM protocol to check for crashed
machines.

* **_SWIM.py_**: Is used to remove the crashed processes from the membership lists.
</details>

## Instructions
<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
<br>
 
1. The first file to be run is the **_client.py_** file. Input as many machines as you'd like by pressing option 1. The machines can be anything from m1 to m_integer (i.e: m1,m2,3, etc). Pressing option 2 gives you the choice to remove a machine. Only machines which have already been added are available to you.

2. The next program to be run is **_members.py_**. You will see that the membership list is created for each of the processes which are active. Each process will have a Membership List which has at least 3 other processes selected at random.

3. The next program that should be run is **_crash_process.py_**. Here you can list all the processes that you want to crash (Do not exceed 3 at a time). This changes these processes to "crashed".

4. Next to be run is **_SWIM.py_**. This program eliminates the crashed processes from the main list. Just running the program is enough, no need to give any inputs.

5. Next run **_SWIM_protocol.py_**, this is the actual implementation of the SWIM algorithm, where active processes are pinged and their membership lists are updated regularly and from that is determined which processes are active and respond to the ping requests and which processes have crashed and don't respond any longer.
</details>
