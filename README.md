# Hamon-Technologies-Code-Challenge

# Explainations

1. A detailed explanation of the function's purpose and operation.

The function counts the frequency of each unique element in the input argument s(iterable) and returns a dictionary where the keys are the elements and the values are the number of times each element appears.
The function first initializes an empty dictionary for the result, then iterates through the input (O(n)) and for each element checks if it is present as key in the result dictionary (O(1)). If the element is present, it increments its value by else the element is set as key to the result dictionary and the value of 1 assigned to it .

2. Suggestions for improving the code in terms of efficiency, readability, or functionality.

    a. https://github.com/darkmewtwo/Hamon-Technologies-Code-Challenge/blob/main/count_elements_improvements.py#L5
    
        Highly readable and very efficient, it is very efficient because the Counter from collections module is used, Counter is specially optimized for the purpose of counting.

    b. https://github.com/darkmewtwo/Hamon-Technologies-Code-Challenge/blob/main/count_elements_improvements.py#L9

        Highly readable and not very efficient as the above, but it is beginner friendly code.

3.  A set of unit tests for this function.
https://github.com/darkmewtwo/Hamon-Technologies-Code-Challenge/blob/main/test_counter_function.py