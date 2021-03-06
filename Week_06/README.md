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

* 最大子序列和
```
"""
1. 暴力：n^2 (可优化：以正数开头，以正数结尾）
2. DP:
    a. 分治（子问题） max_sum(i) = Max(max_sum(i-1), 0) + a[i]
    b. 状态数组定义: f[i] (包含第i个元素并以其结尾的最大子序列和）
    c. DP方程: f[i] = Max(f[i-1], 0) + a[i]
"""
```

* 乘积最大子数组
```
"""
思考:
    1.DP问题:
        a.分治（子问题）: 需考虑负负得正的情况，保留当前位置的最大值和最小值
                        max_product[i] = Max(max_product[i-1] * a[i], min_product[i-1] * a[i], a[i])
                        min_product[i] = Min(max_product[i-1] * a[i], min_product[i-1] * a[i], a[i])
        b.状态数组定义 max_dp, min_dp
        c.DP方程 
            max_dp[i] = Max(max_dp[i-1] * a[i], min_dp[i-1] * a[i], a[i])
            min_dp[i] = Max(max_dp[i-1] * a[i], min_dp[i-1] * a[i], a[i])
"""

def max_product2(self, nums):
    # 利用两个变量维护i-1时刻的状态，res维护最大乘积
    max_dp = min_dp = res = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_dp, min_dp = min_dp, max_dp
        max_dp = max(max_dp * nums[i], nums[i])
        min_dp = min(min_dp * nums[i], nums[i])
        res = max(max_dp, res)
    return res
```

* 零钱兑换
```
"""
    1. 暴力：递归：指数
    2. BFS
    3. DP
        a. subproblems
        b. DP array: f(n) = min{f(n-k), for k in [1, 2, 5]} + 1
        c. DP 方程
"""
```

* 打家劫舍
```
"""
a[i][0,1]: 0,...,i 能偷到的最大值 (,)
0: 不偷第i个房间时； 1: 偷第i个房间时
DP方程:
    a[0][0] = 0
    a[0][1] = nums[0]
    a[i][0] = max(a[i-1][0], a[i-1][1])
    a[i][1] = a[i-1][0] + nums[i]

简化：
    a[i]: 0,...,i 能偷到的最大值， 第i个房子可偷或者不偷
    DP方程:
        a[i] = max(a[i-1], nums[i] + a[i-2])
        a[0] = nums[0]
        a[1] = max(nums[0], nums[1])
"""
"""
再次简化：
    不用dp数组，利用两个中间变量
"""
def rob(nums):
    pre = 0
    now = 0
    for num in nums:
        pre, now = now, max(pre + num, now)
    return now
```

* 打家劫舍II （房子围成一个圈，第一个和最后一个相邻）
```
"""
分两部分：
    1.不偷第一个房间nums[1:]，利用打家劫舍问题的方法得到一个最大金额res1;
    2.不偷最后一个房间nums[:n-1]，利用打家劫舍问题的方法得到一个最大金额res2;
    3.最后取两者的最大值 max(res1, res2)
"""
```

##### 3.动态规划小结
    * 打破自己的思维惯性，形成机器思维
    * 理解复杂逻辑的关键
    * 也是职业进阶的要点要领


mit动态规划