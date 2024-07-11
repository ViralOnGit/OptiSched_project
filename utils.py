def print_schedule(schedule):
    print("PID\tArrival\tBurst\tStart\tFinish\tTurnaround\tWaiting")
    for entry in schedule:
        print(f"{entry[0]}\t{entry[1]}\t{entry[2]}\t{entry[3]}\t{entry[4]}\t{entry[5]}\t{entry[6]}")

def calculate_average_times(schedule):
    total_turnaround_time = sum(entry[5] for entry in schedule)
    total_waiting_time = sum(entry[6] for entry in schedule)
    num_processes = len(schedule)

    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes

    return avg_turnaround_time, avg_waiting_time
