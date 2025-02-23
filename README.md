# ZeroDivisionError despite apparent check
This example showcases a subtle error in Python where a `ZeroDivisionError` occurs even though there is a check for a zero divisor. The issue is related to the order of operations and conditional checks.

## Bug Description
The provided `function_with_uncommon_error` aims to prevent division by zero. However, it incorrectly handles the case where the denominator (`a`) is zero only when the numerator (`b`) is not zero. If b is zero, the condition `a == 0` is evaluated first and the function returns 0 before the potential division error occurs.