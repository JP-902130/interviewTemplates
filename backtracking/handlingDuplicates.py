'''
Method 1: For subset problem, we still need to proceed 0/1 knapsack. The difference is we make two choices: 1st choice is the same as the standard: choose and move to i+1, then pop it to clean up. But if we do not choose the current element, we need cannot choose nums[i] once again. So we need to jump the pointer to the next distince element.
Method 2: Using hashmap. Creating a hashmap map the element to the number of occurence only if the order does not matter. In this case, the duplicate problem is solved. 47. Permutations II is an example

'''
