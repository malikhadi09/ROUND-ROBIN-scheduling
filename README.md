# ROUND ROBIN:
Round Robin is a CPU scheduling algorithm where each process is assigned a fixed time slot in a cyclic way. It is basically the preemptive version of First come First Serve CPU Scheduling algorithm. 

Round Robin CPU Algorithm generally focuses on Time Sharing technique. 
The period of time for which a process or job is allowed to run in a pre-emptive method is called time quantum. 
Each process or job present in the ready queue is assigned the CPU for that time quantum, if the execution of the process is completed during that time then the process will end else the process will go back to the waiting table and wait for its next turn to complete the execution.
 
# Characteristics of Round Robin CPU Scheduling Algorithm:
It is simple, easy to implement, and starvation-free as all processes get fair share of CPU.
One of the most commonly used technique in CPU scheduling as a core.
It is preemptive as processes are assigned CPU only for a fixed slice of time at most.

# TASK 

You are required to implement Round Robin Scheduling Algorithm in this lab task.
Implement the functions for the following:
# findWaitingTime()
# findTurnAroundTime()
# findavgTime()
    averageWaitingTime()
    averageTurnAroundTime()
    
# Step to findWaitingTime()
1)Create an array rem_burstTime[] to keep track of the remaining burst time of processes. This array is initially a copy of burstTime[] (burst times array)

2)Create another array waitingTime[] to store waiting times of processes. Initialize this
array as 0.

3)Initialize time: time = 0

4) Keep traversing all the processes while they are not done. Do the following for i’th process if it is not done yet. 

5) If rem_burstTime[i] > quantum
 time = time + quantum
 rem_burstTime[i] -= quantum;

6) Else // Last cycle for this process
 time = time + rem_burstTime[i];
 waitingTime[i] = time – burstTime[i]
 rem_busrtTime[i] = 0; // This process is over

#OUTPUTS:
![image](https://user-images.githubusercontent.com/92660593/209430799-4c819dd9-15de-4deb-8d51-22f94397668f.png)
![image](https://user-images.githubusercontent.com/92660593/209430805-0ab847b4-6200-4294-9695-b664b46c851f.png)
