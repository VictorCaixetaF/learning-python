'''map exercises'''

nums = [4, 5, 6, 7, 8]

def square (x):
    return x * x
    
print(f'The original list: {nums}')
print()
result = map(square, nums)
print(f'The Square list: {list(result)}')
