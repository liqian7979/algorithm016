学习笔记

#### 递归代码模板
```
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
    
    # process logic in current level
    process(level, data, ...)

    # drill down
    self.recursion(level + 1, p1, ...)
    
    # reverse the current level status if needed
```

#### 分治代码模板
```
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return
    
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = self.devide_conquer(subproblems[0], p1, ...)
    subresult2 = self.devide_conquer(subproblems[1], p1, ...)
    subresult3 = self.devide_conquer(subproblems[2], p2, ...)
    ...

    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)

    # revert the current level states
```

#### 动态规划 Dynamic Programming
##### 1. 关键点
    * 动态规划和递归或者分治没有根本上的区别（关键看有无最优的子结构）
    * 共性：找到重复子问题
    * 差异性：最优子结构、中途可以淘汰次优解
    * 最优子结构：opt[n] = best_of(opt[n-1], opt[n-2], ...)
    * 储存中间状态：opt[i]
    * 递推公式（美其名曰：状态转移方程或者DP方程）
          Fib: opt[n] = opt[n-1] + opt[n-2]
          二维路径: opt[i][j] = opt[i+1][j] + opt[i][j+1] (且判断a[i][j]是否为空地)

##### 2. 实战例题
* Fibonacci数列
```
# 递归 时间复杂度O(2^n)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# 递归 + 记忆化搜索
# memo = [0] * (n+1)
def fib(n, memo):
    if n < 2:
        return n
    if memo[n] == 0:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# for循环  自底向上
def fib(n):
    a = [0 for _ in range(n+1)]
    a[0], a[1] = 0, 1
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]
```
* 最长公共子序列
```
* s1 = "abazdc", s2 = "bacbad"
* if s1[-1] != s2[-1]: LCS[s1, s2] = max(LCS[s1-1, s2], LCS[s1, s2-1])
    LCS[s1, s2] = max(LCS[s1-1, s2], LCS[s1, s2-1], LCS[s1-1, s2-1])
* if s1[-1] == s2[-1]: LCS[s1, s2] = LCS[s1-1, s2-1] + 1
    LCS[s1, s2] = max(LCS[s1-1, s2], LCS[s1, s2-1], LCS[s1-1, s2-1], LCS[s1-1, s2-1] + 1)
* DP方程:
    if s1[-1] != s2[-1]: LCS[s1, s2] = max(LCS[s1-1, s2], LCS[s1, s2-1])
    if s1[-1] == s2[-1]: LCS[s1, s2] = LCS[s1-1, s2-1] + 1
```
* 爬楼梯
```
DP方程：F(n-1) + F(n-2)
思考：1.每次可上1个、2个或3个的情况（easy）
     2.相邻两步的步伐不能相同的情况（medium）
```

* 三角形最小路径和
```
"""
1.brute-force，递归，n层：left or right， 时间复杂度：2^n  自顶向下
2.DP  自底向上
    a.重复性（分治）problem(i, j) = min(sub(i+1, j), sub(i+1, j+1)) + a[i, j]
    b.定义状态数组: f[i, j]
    c.DP方程:f[i, j] = min(f[i+1, j], f[i+1, j+1]) + a[i, j]
"""
def minimum_total(self, triangle):
    dp = triangle
    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
    return dp[0][0]

# 只使用 O(n) 的额外空间
def minimum_total1(self, triangle):
    dp = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
    return dp[0]
```

##### 3.动态规划小结
    * 打破自己的思维惯性，形成机器思维
    * 理解复杂逻辑的关键
    * 也是职业进阶的要点要领


mit动态规划