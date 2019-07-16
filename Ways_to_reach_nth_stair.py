import time

#recursion

recursion_start_time = time.time()

base_case = {0:0, 1:1, 2:2, 3:4}

def total_ways_recursion(n):
    if n in base_case:
        return base_case[n]
    return total_ways_recursion(n-1) + total_ways_recursion(n-2) + total_ways_recursion(n-3)

print("output with recursion", total_ways_recursion(30))

print("recursion time", time.time() - recursion_start_time)

# Dynamic programming

dp_start_time = time.time()
total_ways_dict = {0:0, 1:1, 2:2, 3:4}

def total_ways_dp(n):
    if n in total_ways_dict:
        return total_ways_dict[n]
    ways = total_ways_dp(n-1) + total_ways_dp(n-2) + total_ways_dp(n-3)
    total_ways_dict[n] = ways
    return total_ways_dict[n]


print("output with dp", total_ways_dp(30))

print("dp time", time.time() - dp_start_time)

