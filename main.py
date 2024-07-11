from scheduling_algorithms import fcfs, sjf, round_robin
from utils import print_schedule, calculate_average_times

def main():
    print("Select a CPU scheduling algorithm:")
    print("1. First Come First Serve (FCFS)")
    print("2. Shortest Job First (SJF)")
    print("3. Round Robin (RR)")

    choice = int(input("Enter your choice: "))

    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival time for process {pid}: "))
        burst_time = int(input(f"Enter burst time for process {pid}: "))
        processes.append((pid, arrival_time, burst_time))

    if choice == 1:
        schedule = fcfs(processes)
    elif choice == 2:
        schedule = sjf(processes)
    elif choice == 3:
        time_quantum = int(input("Enter the time quantum for Round Robin: "))
        schedule = round_robin(processes, time_quantum)
    else:
        print("Invalid choice!")
        return

    print_schedule(schedule)

    avg_turnaround_time, avg_waiting_time = calculate_average_times(schedule)
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")

if __name__ == "__main__":
    main()
