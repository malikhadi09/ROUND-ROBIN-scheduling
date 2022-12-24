def findWaitingTime(process,no_process, bt,
                    wt, Time_Quantum):
    rem_bursttime = [0] * no_process

    for i in range(no_process):
        rem_bursttime[i] = bt[i]
    time = 0

    while (1):
        done = True


        for i in range(no_process):


            if (rem_bursttime[i] > 0):
                done = False

                if (rem_bursttime[i] > Time_Quantum):


                    time += Time_Quantum


                    rem_bursttime[i] -= Time_Quantum


                else:


                    time = time + rem_bursttime[i]


                    wt[i] = time - bt[i]


                    rem_bursttime[i] = 0


        if (done == True):
            break



def findTurnAroundTime(process,no_process, bt, wt, tat):

    for i in range(no_process):
        tat[i] = bt[i] + wt[i]





def findavgTime(process,no_process, bt, Time_Quantum):
    wt = [0] * no_process
    tat = [0] * no_process


    findWaitingTime(process,no_process, bt,
                    wt, Time_Quantum)


    findTurnAroundTime(process,no_process, bt,
                       wt, tat)


    print("Processes_ID    Burst Time     Waiting",
          "Time    Turn Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(no_process):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i], "\t\t\t\t", wt[i], "\t\t\t\t", tat[i])

    print("AVERAGE WAITING TIME AND AVERAGE TURN AROUND TIME: ")
    print("__________________________________________________")
    print("\n")
    print("\nAverage waiting time = %.5f " % (total_wt / no_process))
    print("Average turn around time = %.5f " % (total_tat / no_process))

print("ROUND ROBIN SCEDULING: ")
print("______________________")
print("\n")
no_process = 0
no_process = int(input("Please, Enter no of process:"))
Time_Quantum = int(input("Please, Enter the value of Time Quantum:"))
process = []
Time_quantum=[]
burst_time = []
for i in range(no_process):
    Process = int(input("Please, Enter Process id:"))
    process.append(Process)
    BT = int(input("Please,Enter the Burst Time: "))
    burst_time.append(BT)

findavgTime(process,no_process, burst_time, Time_Quantum)