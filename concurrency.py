import time
import random
import threading

# ---------------------------------------
# FUNCTION: Simulate a single user stream
# ---------------------------------------
def process_user_data(user_id):
    """Simulates receiving and processing fitness data for one user."""
    data_points = []

    # Simulate the user generating 100 data entries
    for _ in range(100):
        entry = {
            "user": user_id,
            "timestamp": time.time(),
            "heart_rate": random.randint(60, 160),
            "steps": random.randint(0, 20),
            "sleep_duration": random.uniform(0.0, 1.0)
        }
        data_points.append(entry)

        # Simulate processing time
        time.sleep(0.01)

    return data_points


# ---------------------------------------
# BASELINE: Sequential Processing
# ---------------------------------------
def sequential_processing(num_users):
    start_time = time.time()

    results = []
    for user in range(num_users):
        results.append(process_user_data(user))

    end_time = time.time()
    print(f"Sequential Time: {end_time - start_time:.3f} seconds")
    return results


# ---------------------------------------
# MULTITHREADING: Concurrent Processing
# ---------------------------------------
def threaded_processing(num_users):
    start_time = time.time()

    threads = []
    results = []

    # Wrapper to store thread results
    def wrapper(user_id):
        results.append(process_user_data(user_id))

    # Create threads
    for user in range(num_users):
        t = threading.Thread(target=wrapper, args=(user,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    end_time = time.time()
    print(f"Threaded Time: {end_time - start_time:.3f} seconds")
    return results


# ---------------------------------------
# RUN BOTH APPROACHES
# ---------------------------------------
num_users = 5  # simulate 5 users sending data

print("\n--- Activity 3: Concurrency Performance Comparison ---")
seq_results = sequential_processing(num_users)
thr_results = threaded_processing(num_users)
