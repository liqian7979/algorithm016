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
* 1143.最长公共子序列  
```
if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

* 最长公共子串  
```
if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = 0
```

* 5.最长回文子串  
    1.暴力  嵌套循环，枚举 i，j（起点和终点），判断该子串是否是回文串  O(n^3)  
    2.枚举中心，向两边扩张  O(n^2)  
    3.动态规划  
        定义P(i, j) i, j为子串的起点和终点:  
                P(i, j) = true, s[i, j]是回文串  
                P(i, j) = false, s[i, l]不是回文串  
        P(i, j) = (P(i+1, j-1) && s[i] == s[j])  

* 10.正则表达式匹配  

* 115.不同的子序列  
    1.暴力递归  
    2.动态规划  
    ```
        dp[i][j]代表T前i字符串可以由s前j字符串组成的最多个数。
        所以动态方程：
            当S[j] == T[i], dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            当S[j] != T[i], dp[i][j] = dp[i][j-1]
    ```


### 字符串匹配算法
* 暴力法  O(M*N)  
   [字符串匹配暴力法代码示例](https://shimo.im/docs/8G0aJqNL86wWrPUE)

* Rabin-Karp  
    算法思想：  
        1.假设子串的长度为M(pat)，目标字符串的长度为N(txt)  
        2.计算子串的 hash 值 hash_pat  
        3.计算目标字符串 txt 中每个长度为 M 的子串的 hash 值（共需要计算 N-M+1 次）  
        4.比较 hash 值：如果 hash 值不同，字符串必然不匹配；如果 hash 值相同，还需要使用朴素算法再次判断  

   [Rabin-Karp代码示例](https://shimo.im/docs/1wnsM7eaZ6Ab9j9M)

* KMP  
    [KMP字符串匹配算法视频](https://www.bilibili.com/video/av11866460?from=search&seid=17425875345653862171)  
    [字符串匹配的KMP算法](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)


[Boyer-Moore算法](https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
[Sunday算法](https://blog.csdn.net/u012505432/article/details/52210975)

