# The purpose of this script is to benchmark the resolution of local
# time measurement.

import time

lightspeed = 299792458

#time.time()
print("Testing time.time(). Spatial resolution (meters):")
for counter in range(1,10):
    time_1     = time.time()
    time_2     = time.time()
    distance   = lightspeed*(abs(time_1-time_2))
    print(distance)

#time.time_ns()
print("Testing time.time_ns(). Spatial resolution (meters):")
for counter in range(1,10):
    time_1     = time.time_ns()
    time_2     = time.time_ns()
    distance   = lightspeed*(abs(time_1-time_2))/1000000000
    print(distance)      


    
