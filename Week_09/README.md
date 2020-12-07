学习笔记
## 高级动态规划
### 递归、分治、回溯、动态规划复习

### 常见的DP题目和状态方程

### 高阶动态规划题目详解
* 爬楼梯问题改进  
    - 1,2,3  
    - x1, x2,..., xm步  
    - 前后不能走相同的步伐  
    - 746.使用最小花费爬楼梯  

* 编辑距离  
    1.BFS, two-ended BFS  
    2.DP  

```
# dp[i][j]: word1.substr(0, i) 与 word2.substr(0, j)之间的编辑距离
if w1[i] == w2[j]:
    edit_dist(i, j) = edit_dist(i-1, j-1)  # 分治
else:
    # w1[i] != w2[j]
    edit_dist(i, j) = MIN(edit_dist(i-1, j-1) + 1, edit_dist(i-1, j) + 1, edit_dist(i, j-1) + 1)
```

## 字符串算法
### 字符串基础知识和引申题目
* 387.字符串中的第一个唯一字符  
    1.暴力求解：i 枚举所有字符， j 枚举 i 后面的所有字符    O(n^2)  
    2.map (hashmap O(1), treemap O(logN))    O(N) or O(NlogN)  
    3.hash table  

* 8.字符串转换整数  
    


### 高级字符串算法


### 字符串匹配算法

