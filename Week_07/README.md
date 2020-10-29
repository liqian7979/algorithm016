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