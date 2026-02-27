def calculate_average_ping(response_times):
    total_time = 0
    valid_pings = 0
    
    for time in response_times:
        try:
            total_time += time
            valid_pings += 1
        except TypeError:
            continue
    
    if valid_pings > 0:
        average = total_time / valid_pings
        return average            
    else:
        return 0

if __name__ == "__main__":
    print("--- Server Ping Analyzer ---")

    network_logs = [45, 52, 48, "timeout", "except", 50, 49, 55]

    print("Calculating average response time...")
    final_average = calculate_average_ping(network_logs)

    print(f"The average server ping is: {final_average:.2f} ms")
