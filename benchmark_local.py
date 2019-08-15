# The purpose of this script is to benchmark the resolution of local
# time measurement.

import time

# Set constants
lightspeed  = 299792458    # speed of light in meters per second
loop_count = 400000

print("")

# ==Benchmark time.time() for multiple rounds==

print("Testing time.time() for multiple rounds.")

# Initialize lists with zeros.
time_1_list       = [0]*loop_count
time_2_list       = [0]*loop_count
time_delta        = [0]*loop_count
time_delta_average = [0]*loop_count

# measure delays in nanoseconds
for counter in range(1,loop_count):
    time_1_list[counter] = time.time_ns()
    time_2_list[counter] = time.time_ns()

# calculate round trip times in nanoseconds
for counter in range(1,loop_count):
    time_delta[counter] = (time_2_list[counter] - time_1_list[counter])

# calculate average round trip time in nanoseconds
sum = 0
for counter in range(1,loop_count):
    sum = sum + time_delta[counter]
    time_delta_average = sum/len(time_delta)

# print average round trip time in nanoseconds
print("time.time() temporal resolution (nanoseconds):")
print(time_delta_average)
    
# print  upper bound for distance in meters
print("time.time() spatial resolution (meters):")
distance = lightspeed*(time_delta_average)/1000000000
print(distance)
print("")
    
# ==Benchmark time.time_ns() for multiple rounds==

print("Testing time.time_ns() for multiple rounds.")

# Initialize lists with zeros.
time_1_list       = [0]*loop_count
time_2_list       = [0]*loop_count
time_delta        = [0]*loop_count
time_delta_average = [0]*loop_count

# measure delays in nanoseconds
for counter in range(1,loop_count):
    time_1_list[counter] = time.time_ns()
    time_2_list[counter] = time.time_ns()

# calculate round trip times in nanoseconds
for counter in range(1,loop_count):
    time_delta[counter] = (time_2_list[counter] - time_1_list[counter])

# calculate average round trip time in nanoseconds
sum = 0
for counter in range(1,loop_count):
    sum = sum + time_delta[counter]
    time_delta_average = sum/len(time_delta)

# print average round trip time in nanoseconds
print("time.time_ns() temporal resolution (nanoseconds):")
print(time_delta_average)
    
# print  upper bound for distance in meters
print("time.time_ns() spatial resolution (meters):")
distance = lightspeed*(time_delta_average)/1000000000
print(distance)
print("")


# ==Benchmark time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID) for multiple rounds==

print("Testing time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID) for multiple rounds.")

# Initialize lists with zeros.
time_1_list       = [0]*loop_count
time_2_list       = [0]*loop_count
time_delta        = [0]*loop_count
time_delta_average = [0]*loop_count

# measure delays in nanoseconds
for counter in range(1,loop_count):
    time_1_list[counter] = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)
    time_2_list[counter] = time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID)

# calculate round trip times in nanoseconds
for counter in range(1,loop_count):
    time_delta[counter] = (time_2_list[counter] - time_1_list[counter])

# calculate average round trip time in nanoseconds
sum = 0
for counter in range(1,loop_count):
    sum = sum + time_delta[counter]
    time_delta_average = sum/len(time_delta)

# print average round trip time in nanoseconds
print("time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID) temporal resolution (nanoseconds):")
print(time_delta_average)
    
# print  upper bound for distance in meters
print("time.clock_gettime_ns(time.CLOCK_PROCESS_CPUTIME_ID) spatial resolution (meters):")
distance = lightspeed*(time_delta_average)/1000000000
print(distance)
print("")

    
# ==Benchmark time.monotonic_ns() for multiple rounds==

print("Testing time.monotonic_ns() for multiple rounds.")

# Initialize lists with zeros.
time_1_list       = [0]*loop_count
time_2_list       = [0]*loop_count
time_delta        = [0]*loop_count
time_delta_average = [0]*loop_count

# measure delays in nanoseconds
for counter in range(1,loop_count):
    time_1_list[counter] = time.monotonic_ns()
    time_2_list[counter] = time.monotonic_ns()

# calculate round trip times in nanoseconds
for counter in range(1,loop_count):
    time_delta[counter] = (time_2_list[counter] - time_1_list[counter])

# calculate average round trip time in nanoseconds
sum = 0
for counter in range(1,loop_count):
    sum = sum + time_delta[counter]
    time_delta_average = sum/len(time_delta)

# print average round trip time in nanoseconds
print("time.monotonic_ns() temporal resolution (nanoseconds):")
print(time_delta_average)
    
# print  upper bound for distance in meters
print("time.monotonic_ns() spatial resolution (meters):")
distance = lightspeed*(time_delta_average)/1000000000
print(distance)
print("")


# ==Benchmark time.perf_counter_ns() for multiple rounds==

print("Testing time.perf_counter_ns() for multiple rounds.")

# Initialize lists with zeros.
time_1_list       = [0]*loop_count
time_2_list       = [0]*loop_count
time_delta        = [0]*loop_count
time_delta_average = [0]*loop_count

# measure delays in nanoseconds
for counter in range(1,loop_count):
    time_1_list[counter] = time.perf_counter_ns()
    time_2_list[counter] = time.perf_counter_ns()

# calculate round trip times in nanoseconds
for counter in range(1,loop_count):
    time_delta[counter] = (time_2_list[counter] - time_1_list[counter])

# calculate average round trip time in nanoseconds
sum = 0
for counter in range(1,loop_count):
    sum = sum + time_delta[counter]
    time_delta_average = sum/len(time_delta)

# print average round trip time in nanoseconds
print("time.perf_counter_ns() temporal resolution (nanoseconds):")
print(time_delta_average)
    
# print  upper bound for distance in meters
print("time.perf_counter_ns() spatial resolution (meters):")
distance = lightspeed*(time_delta_average)/1000000000
print(distance)
print("")


# ==Benchmark time.process_time_ns() for multiple rounds==

print("Testing time.process_time_ns() for multiple rounds.")

# Initialize lists with zeros.
time_1_list       = [0]*loop_count
time_2_list       = [0]*loop_count
time_delta        = [0]*loop_count
time_delta_average = [0]*loop_count

# measure delays in nanoseconds
for counter in range(1,loop_count):
    time_1_list[counter] = time.process_time_ns()
    time_2_list[counter] = time.process_time_ns()

# calculate round trip times in nanoseconds
for counter in range(1,loop_count):
    time_delta[counter] = (time_2_list[counter] - time_1_list[counter])

# calculate average round trip time in nanoseconds
sum = 0
for counter in range(1,loop_count):
    sum = sum + time_delta[counter]
    time_delta_average = sum/len(time_delta)

# print average round trip time in nanoseconds
print("time.process_time_ns() temporal resolution (nanoseconds):")
print(time_delta_average)
    
# print  upper bound for distance in meters
print("time.process_time_ns() spatial resolution (meters):")
distance = lightspeed*(time_delta_average)/1000000000
print(distance)
print("")


# ==Benchmark time.thread_time_ns() for multiple rounds==

print("Testing time.thread_time_ns() for multiple rounds.")

# Initialize lists with zeros.
time_1_list       = [0]*loop_count
time_2_list       = [0]*loop_count
time_delta        = [0]*loop_count
time_delta_average = [0]*loop_count

# measure delays in nanoseconds
for counter in range(1,loop_count):
    time_1_list[counter] = time.thread_time_ns()
    time_2_list[counter] = time.thread_time_ns()

# calculate round trip times in nanoseconds
for counter in range(1,loop_count):
    time_delta[counter] = (time_2_list[counter] - time_1_list[counter])

# calculate average round trip time in nanoseconds
sum = 0
for counter in range(1,loop_count):
    sum = sum + time_delta[counter]
    time_delta_average = sum/len(time_delta)

# print average round trip time in nanoseconds
print("time.thread_time_ns() temporal resolution (nanoseconds):")
print(time_delta_average)
    
# print  upper bound for distance in meters
print("time.thread_time_ns() spatial resolution (meters):")
distance = lightspeed*(time_delta_average)/1000000000
print(distance)
print("")
