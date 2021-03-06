学习笔记
## 字典树和并查集
### 字典树 Trie
##### 1.复习树
    二叉树的一个高频题目：按层次打印一颗二叉树 BFS DFS
    二叉搜索树:中序遍历是升序序列
##### 2.字典树的基本结构
    字典树，即Trie树，又称单词查找树或键树，是一种树形结构。
    典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。
    优点：最大限度地减少无谓的字符串比较，查询效率比哈希表高。
    注意：Trie树不是二叉树，是多叉树。
##### 3.字典树的基本性质
    a.结点本身不存完整单词；
    b.从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的字符串；
    c.每个结点的所有子结点路径代表的字符都不相同。
    （结点可存储额外信息，例如单词出现的统计的频次）
##### 4.字典树的核心思想
    Trie树的核心思想是空间换时间。
    利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。
##### 5.Trie树的代码模板
```
class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```
##### 6.实战题目
* 单词搜索II
```
1. words遍历 --> board search    O(N*m*m*4^k)
2. trie
    a. all words --> Trie 构建起 prefix
    b. board, DFS
```

### 并查集 Disjoint Set
##### 1.适用场景
    组团、配对问题
    Group or not ?
##### 2.基本操作
    · markeSet(s): 建立一个新的并查集，其中包含s个单元素集合。
    · unionSet(x, y): 把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并。
    · find(x): 找到元素x所在的集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了。
##### 3.并查集的实现
    初始化: 每个元素拥有一个parent的数组指向自己；
    查询: 一直网上找元素的parent,直到找到所在集合的领头元素（parent指向自己的元素）；
    合并: 查询两个元素的所在集合的代表，将其中一个的parent指向另外一个即可，并将孤立集合的个数减一；
```
class UnionFind(object):
    def init(self, n):
        """初始化: 每个元素拥有一个parent的数组指向自己"""
        p = [i for i in range(n)]

    def union(self, p, i, j):
        """合并: 查询两个元素的所在集合的代表，将其中一个的parent指向另外一个即可"""
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2

    def parent(self, p, i):
        """查询: 一直网上找元素的parent,直到找到所在集合的领头元素（parent指向自己的元素）"""
        root = i
        while p[root] != root:
            root = p[root]
        # 路径压缩
        while p[i] != i:
            x = i
            i = p[i]
            p[x] = root
        return root
```
##### 4.实战题目
* 朋友圈
```
# 1. DFS, BFS  (类似 岛屿问题)
# 2. 并查集
def find_circle_num(self, M):
    if not M:
        return 0
    n = len(M)
    p = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                # 合并
                self._union(p, i, j)
    # 获取孤立集合数
    return len(set([self._parent(p, i) for i in range(n)]))
```

## 高级搜索
### 剪枝
##### 1.剪枝的实现和特性
* 初级搜索
    1.朴素搜索
    2.优化方式：不重复（fibonacci)、剪枝（生成括号问题）
    3.搜索方向：
        DFS：depth first search 深度优先搜索
        BFS：breadth first search 广度优先搜索
        双向搜索、启发式搜素（A*算法、优先级搜索）

* DFS代码-递归写法
```
visited = set()

def dfs(node, visited):
    # terminator
    if node in visited:
        # already visited
        return
    visited.add(node)
    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

* DFS代码-非递归写法
```
def dfs(tree):
    if tree.root is None:
        return []
    
    visited, stack = [], [tree.root]

    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
    
    # other processing work
    ...
```

* BFS代码
```
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```

* 回溯法
    回溯法采用试错的思想，它尝试分步的去解决一个问题。在分布解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。
    回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：
    · 找到一个可能存在的正确的答案
    · 在尝试了所有可能的分步方法后宣告该问题没有答案
    在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

##### 2.剪枝实战题目解析
    爬楼梯、括号生成、N皇后、有效的数独、解数独

### 启发式搜索 Heuristic Search (A*)
##### 1.A*代码模板
```
def AstarSearch(graph, start, end):
    pq = collections.priority_queue() # 优先级 —> 估价函数
    pq.append([start]) 
    visited.add(start)
    while pq: 
        node = pq.pop() # can we add more intelligence here ?
        visited.add(node)
        process(node) 
        nodes = generate_related_nodes(node) 
        unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
```

##### 2.估价函数
    启发式函数：h(n)，它用来评价哪些结点最有希望的是一个我们要找的结点，h(n)会返回一个非负实数，也可以认为是从结点n到目标结点路径的估计成本。
    启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居结点会导向一个目标。

##### 3.实战题目解析
* 1091.二进制矩阵中的最短路径
```
# BFS
def shortestPathBinaryMatrix(grid):
    # grid: List[List[int]]
    q, n = [(0, 0, 2)], len(grid)
    if grid[0][0] or grid[-1][-1]:
        return -1
    elif n <= 2:
        return n
    
    # BFS starts
    for i, j, d in q:
        # current node: i, j; distance = d
        for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), 
                     (i, j-1), (i, j+1),
                     (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                if x == y == n-1:
                    return d
                q += [(x, y, d+1)]
                grid[x][y] = 1
    return -1
```
```
# A*

```

* 773.滑动谜题
```
# DFS
# BFS - 更快找到最优解
# A*
def sliding_puzzle(self, board):
    """BFS"""
    # 将二维数组变换为一维字符串
    # 方向变换向量  0位于不同位置时对应的可交换的位置（在一维字符串中）
    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }
    # 存放位置移动过的字符串
    used = set()
    cnt = 0
    s = ''.join(str(c) for row in board for c in row)
    q = [s]
    # BFS starts
    while q:
        new = []
        for s in q:
            used.add(s)
            if s == '123450':
                return cnt
            arr = [c for c in s]
            # 开始移动0
            zero_index = s.index('0')
            for move in moves[zero_index]:
                new_arr = arr[:]
                new_arr[zero_index], new_arr[move] = new_arr[move], new_arr[zero_index]
                new_s = ''.join(new_arr)
                if new_s not in used:
                    new.append(new_s)
        cnt += 1
        q = new
    return -1
```

## 红黑树和AVL树
### AVL树
##### 1.发明者 G.M.Adelson-Velsky 和 Evgenil Landis
##### 2.Balance Factor(平衡因子)
    是它的左子树的高度减去它的右子树的高度（有时相反）。
    balance factor = {-1, 0, 1}
##### 3.通过旋转操作来进行平衡（四种）
    左旋
    右旋
    左右旋
    右左旋
##### 4.AVL总结
    平衡二叉树；
    每个结点存 balance factor = {-1, 0, 1};
    四种旋转操作；
    不足：结点需要存储额外信息、且调整次数频繁。

### 红黑树 Red-black Tree
##### 1.介绍
    红黑树是一种近似平衡的二叉搜索树（Binary Search Tree），它能够确保任何一个结点的左右子树的高度差小于两倍。
    具体来说，红黑树是满足如下条件的二叉搜索树：
    * 每个结点要么是红色，要么是黑色；
    * 根结点是黑色；
    * 每个叶结点（NIL结点，空结点）是黑色的；
    * 不能有相邻接的两个红色结点；
    * 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。
