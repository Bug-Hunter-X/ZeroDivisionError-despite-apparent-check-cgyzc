def function_with_uncommon_error_fixed(a, b):
    if a == 0:
        if b == 0:
            return 0 # Return 0 for both a and b being 0.
        else:
            return float('inf') # or raise a custom exception, or return None - depending on your requirements.
    return b / a

result = function_with_uncommon_error_fixed(0, 10)
print(result) # Output: inf

result = function_with_uncommon_error_fixed(10, 0)
print(result) # Output: 0.0

result = function_with_uncommon_error_fixed(0,0)
print(result) # Output: 0