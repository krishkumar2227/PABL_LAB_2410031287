#10.You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
def can_jump(arr):
    max_reach = 0
    
    for i in range(len(arr)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + arr[i])
    
    return True


# Example
arr = [2, 3, 1, 1, 4]
print("Can reach end:", can_jump(arr))