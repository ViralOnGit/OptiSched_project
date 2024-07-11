def fcfs(processes):
    processes.sort(key=lambda x: x[1])
    start_time = 0
    schedule = []

    for process in processes:
        pid, arrival_time, burst_time = process
        if start_time < arrival_time:
            start_time = arrival_time
        finish_time = start_time + burst_time
        turnaround_time = finish_time - arrival_time
        waiting_time = start_time - arrival_time
        schedule.append((pid, arrival_time, burst_time, start_time, finish_time, turnaround_time, waiting_time))
        start_time = finish_time

    return schedule



def sjf(processes):
    processes.sort(key=lambda x: (x[1], x[2]))
    start_time = 0
    schedule = []

    while processes:
        available_processes = [p for p in processes if p[1] <= start_time]
        if available_processes:
            next_process = min(available_processes, key=lambda x: x[2])
        else:
            next_process = min(processes, key=lambda x: x[1])
            start_time = next_process[1]
        processes.remove(next_process)
        pid, arrival_time, burst_time = next_process
        finish_time = start_time + burst_time
        turnaround_time = finish_time - arrival_time
        waiting_time = start_time - arrival_time
        schedule.append((pid, arrival_time, burst_time, start_time, finish_time, turnaround_time, waiting_time))
        start_time = finish_time

    return schedule


def round_robin(processes, time_quantum):
    from collections import deque

    processes.sort(key=lambda x: x[1])
    queue = deque(processes)
    time = 0
    schedule = []
    process_map = {p[0]: [p[1], p[2]] for p in processes}  # pid -> [arrival_time, remaining_burst_time]
    ready_queue = deque()
    process_start_times = {p[0]: 0 for p in processes}

    while queue or ready_queue:
        while queue and queue[0][1] <= time:
            ready_queue.append(queue.popleft())

        if ready_queue:
            pid, arrival_time, burst_time = ready_queue.popleft()
            remaining_burst_time = process_map[pid][1]
            exec_time = min(remaining_burst_time, time_quantum)
            process_map[pid][1] -= exec_time
            start_time = time
            time += exec_time
            finish_time = time

            if process_start_times[pid] == 0:
                process_start_times[pid] = start_time

            if process_map[pid][1] > 0:
                ready_queue.append((pid, arrival_time, burst_time))
            else:
                turnaround_time = finish_time - arrival_time
                waiting_time = turnaround_time - burst_time
                schedule.append((pid, arrival_time, burst_time, process_start_times[pid], finish_time, turnaround_time, waiting_time))
        else:
            time = queue[0][1]

    return schedule
