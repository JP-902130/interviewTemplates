Problem1: dfs(i), strictly from i or not strictly?

- Referring to "300. Longest Increasing Subsequence"
  - [10,9,2,5,3,7,101,18]
  - Does dfs(1) return the longest subsequence start "strictly" from the element 9, or the longest subsequence from arr[1:]?
  - We have to return the longest subsequence start "strictly from element 9. The reason is we need to use the dfs(1) to build up the result for dfs(0). If dfs(1) returns the longest Increasing subsequence from arr[1:], we have 0 knowledge of what the sequence should look like. Hence we cannot maintain the subsequence invariance.
