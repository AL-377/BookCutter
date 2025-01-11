import os
import re



print(os.getcwd())

def longestPalindrome(s: str) -> str:
    """
    寻找字符串中最长的回文子串
    
    算法思路：使用动态规划方法
    - dp[i][j] 表示子串 s[i:j+1] 是否为回文串
    - 状态转移方程：dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
    
    参数:
        s: str - 输入字符串
    
    返回:
        str - 最长回文子串
    """
    # 边界条件判断：空串或长度为1的字符串直接返回
    if not s or len(s) < 2:
        return s
    
    # 初始化动态规划表
    n = len(s)
    dp = [[False] * n for _ in range(n)]  # 创建n*n的二维数组，初始值都是False
    start = 0   # 记录最长回文子串的起始位置
    max_len = 1 # 记录最长回文子串的长度
    
    # 初始化：所有单个字符都是回文
    for i in range(n):
        dp[i][i] = True
    
    # 开始填充dp表
    for length in range(2, n + 1):  # 遍历所有可能的子串长度
        for i in range(n - length + 1):  # 遍历所有可能的起始位置
            j = i + length - 1  # 计算结束位置
            
            # 处理长度为2的子串
            if length == 2:
                dp[i][j] = (s[i] == s[j])
            # 处理长度大于2的子串
            else:
                # 当前子串是回文的条件：
                # 1. 首尾字符相同 (s[i] == s[j])
                # 2. 去掉首尾后的子串也是回文 (dp[i+1][j-1])
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
            
            # 如果当前子串是回文，且长度大于当前记录的最大长度，则更新记录
            if dp[i][j] and length > max_len:
                start = i
                max_len = length
    
    # 返回最长回文子串
    return s[start:start + max_len]

# 测试用例
test_cases = [
    "babad",    # 期望输出: "bab" 或 "aba"
    "cbbd",     # 期望输出: "bb"
    "a",        # 期望输出: "a"
    "ac",       # 期望输出: "a" 或 "c"
    "racecar"   # 期望输出: "racecar"
]

# 执行测试
for test in test_cases:
    print(f"输入: {test}")
    print(f"输出: {longestPalindrome(test)}\n")
