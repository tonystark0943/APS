def longest_common_substring(A, B):
    dp = [[0 for j in range(len(B))] for i in range(len(A))]
    for i in range(len(B)):
        if A[0] == B[i]:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    for i in range(len(A)):
        if B[0] == A[i]:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
    max_len = 0
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
            max_len = max(max_len, dp[i][j])
    return max_len

if __name__ == '__main__':
    print(longest_common_substring('nature', 'nurture'))