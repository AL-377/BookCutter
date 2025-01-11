import os

print(os.getcwd())

def longestPalindrome(s: str) -> str:
    # 边界条件判断
    if not s or len(s) < 2:
        return s
    
    # 初始化动态规划表
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0  # 记录最长回文子串的起始位置
    max_len = 1  # 记录最长回文子串的长度
    
    # 所有单个字符都是回文
    for i in range(n):
        dp[i][i] = True
    
    # 开始填充dp表
    for length in range(2, n + 1):  # 子串长度
        for i in range(n - length + 1):  # 起始位置
            j = i + length - 1  # 结束位置
            
            if length == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
            
            # 更新最长回文子串信息
            if dp[i][j] and length > max_len:
                start = i
                max_len = length
    
    return s[start:start + max_len]

# 测试代码
test_cases = [
    "babad",
    "cbbd",
    "a",
    "ac",
    "racecar"
]

for test in test_cases:
    print(f"输入: {test}")
    print(f"输出: {longestPalindrome(test)}\n")
