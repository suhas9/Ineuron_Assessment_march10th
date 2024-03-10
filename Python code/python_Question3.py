def count_horses(stalls, distance):
    count = 1
    last_stall = stalls[0]
    for stall in stalls:
        if stall - last_stall >= distance:
            count += 1
            last_stall = stall
    return count

def largest_min_distance(stalls, k):
    stalls.sort()
    lower_bound = 0
    upper_bound = stalls[-1] - stalls[0]

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if count_horses(stalls, mid) >= k:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1
    return upper_bound

stalls = [1, 2, 4, 8, 9]
k = 3
result = largest_min_distance(stalls, k)
print("Largest minimum distance:", result)