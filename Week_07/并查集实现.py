# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-11-2 下午4:40
# @File     : 并查集实现.py
# @Software : PyCharm


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
