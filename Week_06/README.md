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
