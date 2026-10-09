# ============================================================
# CONCURRENCY AND PERFORMANCE OPTIMISATION
# Scenario: Mental Health Monitoring Application
#
# This program simulates wearable data arriving from several
# users and compares:
#   1. Sequential processing
#   2. Concurrent processing using threads
# ============================================================


# ------------------------------------------------------------
# IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import time
# Used to:
# - simulate waiting for incoming sensor data
# - measure execution time

import random
# Used to generate example wearable sensor values

import threading
# Used to create and manage multiple threads


# ------------------------------------------------------------
# FUNCTION 1: PROCESS DATA FOR ONE USER
# ------------------------------------------------------------

def process_user_data(user_id):

    """
    Simulates receiving and processing wearable data
    for one user.

    Each user generates 100 records containing:
    - user ID
    - timestamp
    - heart rate
    - steps
    - sleep duration
    """

    # Create an empty list to store this user's records
    data_points = []

    # Generate 100 simulated wearable readings
    for _ in range(100):

        # Create one wearable-data record
        entry = {

            # Identify which user generated the reading
            "user": user_id,

            # Record the current time
            "timestamp": time.time(),

            # Generate a simulated heart rate
            # between 60 and 160 beats per minute
            "heart_rate": random.randint(60, 160),

            # Generate a simulated number of steps
            "steps": random.randint(0, 20),

            # Generate a simulated sleep-duration value
            "sleep_duration": random.uniform(0.0, 1.0)
        }

        # Add the new record to the user's list
        data_points.append(entry)

        # Simulate waiting for data to arrive from
        # an external wearable device
        #
        # This makes the example I/O-bound.
        time.sleep(0.01)

    # Return all records generated for this user
    return data_points


# ------------------------------------------------------------
# FUNCTION 2: SEQUENTIAL PROCESSING
# ------------------------------------------------------------

def sequential_processing(num_users):

    """
    Processes users one after another.

    The next user's data is not processed until the
    previous user's processing has finished.
    """

    # Start measuring execution time
    start_time = time.perf_counter()

    # Store the results for all users
    results = []

    # Process each user sequentially
    for user in range(num_users):

        # Process one user's data
        user_data = process_user_data(user)

        # Store the result
        results.append(user_data)

    # Stop measuring execution time
    end_time = time.perf_counter()

    # Calculate total execution time
    elapsed_time = end_time - start_time

    # Display the result
    print(
        f"Sequential Time: "
        f"{elapsed_time:.3f} seconds"
    )

    # Return both the results and execution time
    return results, elapsed_time


# ------------------------------------------------------------
# FUNCTION 3: CONCURRENT PROCESSING USING THREADS
# ------------------------------------------------------------

def threaded_processing(num_users):

    """
    Processes several users concurrently using threads.

    Each user is assigned a separate thread.
    """

    # Start measuring execution time
    start_time = time.perf_counter()

    # Store all Thread objects
    threads = []

    # Store results produced by the threads
    results = []

    # Create a lock to protect the shared results list
    lock = threading.Lock()


    # --------------------------------------------------------
    # INNER FUNCTION
    # --------------------------------------------------------

    def worker(user_id):

        """
        Processes one user's data inside a thread.
        """

        # Process the wearable data for this user
        user_data = process_user_data(user_id)

        # Several threads may access 'results'.
        # The lock ensures that only one thread updates
        # the shared list at a time.
        with lock:

            results.append(user_data)


    # --------------------------------------------------------
    # CREATE AND START THREADS
    # --------------------------------------------------------

    for user in range(num_users):

        # Create a new thread
        #
        # target = function the thread will execute
        # args   = values passed to that function
        thread = threading.Thread(
            target=worker,
            args=(user,)
        )

        # Store the Thread object
        threads.append(thread)

        # Start execution of the thread
        thread.start()


    # --------------------------------------------------------
    # WAIT FOR ALL THREADS TO FINISH
    # --------------------------------------------------------

    for thread in threads:

        # join() pauses the main program until this
        # thread has completed.
        #
        # This ensures that execution time is not measured
        # before the threads have finished.
        thread.join()


    # Stop measuring time only after all threads finish
    end_time = time.perf_counter()

    # Calculate execution time
    elapsed_time = end_time - start_time

    # Display the result
    print(
        f"Threaded Time: "
        f"{elapsed_time:.3f} seconds"
    )

    # Return the processed data and execution time
    return results, elapsed_time


# ------------------------------------------------------------
# RUN THE PERFORMANCE TEST
# ------------------------------------------------------------

# Number of users sending wearable data
num_users = 5


print("\n-------------------------------------")
print("SEQUENTIAL PROCESSING")
print("-------------------------------------")

# Run the sequential version
sequential_results, sequential_time = (
    sequential_processing(num_users)
)


print("\n-------------------------------------")
print("CONCURRENT PROCESSING")
print("-------------------------------------")

# Run the threaded version
threaded_results, threaded_time = (
    threaded_processing(num_users)
)


# ------------------------------------------------------------
# COMPARE PERFORMANCE
# ------------------------------------------------------------

print("\n-------------------------------------")
print("PERFORMANCE COMPARISON")
print("-------------------------------------")

# Display both execution times
print(
    f"Sequential Time : "
    f"{sequential_time:.3f} seconds"
)

print(
    f"Concurrent Time : "
    f"{threaded_time:.3f} seconds"
)


# Calculate the difference between the two approaches
difference = sequential_time - threaded_time

print(
    f"Time Difference : "
    f"{difference:.3f} seconds"
)


# ------------------------------------------------------------
# IDENTIFY WHICH APPROACH WAS FASTER
# ------------------------------------------------------------

if threaded_time < sequential_time:

    print(
        "For this run, the concurrent approach "
        "completed faster."
    )

elif sequential_time < threaded_time:

    print(
        "For this run, the sequential approach "
        "completed faster."
    )

else:

    print(
        "Both approaches took approximately "
        "the same amount of time."
    )
