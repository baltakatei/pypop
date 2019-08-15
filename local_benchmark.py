# The purpose of this script is to benchmark the resolution of local
# time measurement.

import time

# Set constants
lightspeed  = 299792458    # speed of light in meters per second
loop_count = 1000000

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

    
