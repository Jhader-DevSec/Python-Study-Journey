import os
import platform


def retry_connection(original_function):
    def wrapper(*args, **kwargs):
        print("\nTrying to connect...")

        
        for attempt in range(3):
            try:
                result = original_function(*args, **kwargs)
                return result

            except Exception as e:
                print(f"[WARNING] Attempt {attempt + 1} failed. Reason: {e}. Retrying...")

        print("[CRITICAL ERROR] Max retries reached. Connection aborted.")
        return None
            
    return wrapper

# ==========================================
#  THE PROTECTED FUNCTIONS
# ==========================================
@retry_connection
def perform_ping(host):
    system_op = '-n' if platform.system().lower() == 'windows' else '-c'
    
    command = f"ping {system_op} 1 {host}"
    status = os.system(command)
    
    if status == 0:
        print(f"\n[SUCCESS] {host} is online!")
    else:
        raise Exception("Host is unreachable")

@retry_connection
def connect_to_database(local_data):
    # Forcing a ZeroDivisionError to test the fault tolerance
    point = 1 / 0 

# ==========================================
#  TEST SPACE
# ==========================================
if __name__ == "__main__":
    
    print("--------- 1. Trying to ping a server ---------")
    target_host = "8.8.8.8" 
    perform_ping(target_host)

    print("\n--------- 2. Objective is to fail ---------")
    path = "/fake/path/data"
    connect_to_database(path)