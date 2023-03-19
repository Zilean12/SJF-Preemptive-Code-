from tabulate import tabulate

# SJF Preemptive Scheduling in Python using Tabulate

def sjf_preemptive(processes):
    # Sort the processes by arrival time and burst time
    processes.sort(key=lambda x: (x[0], x[1]))
    
    n = len(processes)
    burst_times = [processes[i][1] for i in range(n)]
    remaining_times = burst_times.copy()
    waiting_times = [0] * n
    response_times = [-1] * n
    completion_times = [0] * n
    turn_around_times = [0] * n
    relative_delays = [0] * n
    
    time = 0
    completed = 0
    queue = []
    current_time = 0
    min_time = float('inf')
    min_index = None
    flag = False
    
    while completed != n:
        # Check for arriving processes
        for i in range(n):
            if processes[i][0] == time:
                queue.append(i)
                flag = True
                
        # Select the process with the shortest remaining time
        if not queue:
            time += 1
            continue
        
        for i in queue:
            if remaining_times[i] < min_time:
                min_time = remaining_times[i]
                min_index = i
        
        if flag:
            response_times[min_index] = time - processes[min_index][0]
            flag = False
        
        # Reduce remaining time for selected process
        remaining_times[min_index] -= 1
        
        # If process is completed
        if remaining_times[min_index] == 0:
            completion_times[min_index] = time + 1
            turn_around_times[min_index] = completion_times[min_index] - processes[min_index][0]
            waiting_times[min_index] = turn_around_times[min_index] - burst_times[min_index]
            relative_delays[min_index] = waiting_times[min_index] / burst_times[min_index]
            completed += 1
            
            # Remove process from queue
            queue.remove(min_index)
            
            # Reset min_time and min_index
            min_time = float('inf')
            min_index = None
        
        time += 1
        
    # Calculate average values
    avg_tat = sum(turn_around_times) / n
    avg_wt = sum(waiting_times) / n
    avg_rt = sum(response_times) / n
    avg_rd = sum(relative_delays) / n
    
    # Create a table with the results
    headers = ["Process", "Burst Time", "Arrival Time", "Waiting Time", "Response Time", "Turnaround Time", "Relative Delay"]
    results = [[i+1, burst_times[i], processes[i][0], waiting_times[i], response_times[i], turn_around_times[i], f"{relative_delays[i]:.2f}"] for i in range(n)]
    results.append(["Average", "-", "-", f"{avg_wt:.2f}", f"{avg_rt:.2f}", f"{avg_tat:.2f}", f"{avg_rd:.2f}"])
    table = tabulate(results, headers=headers, tablefmt="fancy_grid")
    
    # Print the table
    print(table)
    
# Define the list of processes with their arrival times and burst times
processes = [(0, 3), (1, 1), (5, 2), (4, 4)]

# Call the sjf_preemptive function with the list of processes
sjf_preemptive(processes)
