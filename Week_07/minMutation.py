# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-11-13 上午10:03
# @File     : minMutation.py
# @Software : PyCharm
"""
433.最小基因变化
一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于"A", "C", "G", "T"中的任意一个。
假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
例如，基因序列由"AACCGGTT"变化至"AACCGGTA" 即发生了一次基因变化。
与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
现在给定3个参数—— start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。
如果无法实现目标变化，请返回-1。
注意:
    1.起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
    2.所有的目标基因序列必须是合法的。
    3.假定起始基因序列与目标基因序列是不一样的。
示例1:
    start: "AACCGGTT"
    end: "AACCGGTA"
    bank: ["AACCGGTA"]
    返回值: 1
示例2:
    start: "AACCGGTT"
    end: "AAACGGTA"
    bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    返回值: 2
示例3:
    start: "AAAAACCC"
    end:   "AACCCCCC"
    bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    返回值: 3
"""


class Solution(object):
    def min_mutation(self, start, end, bank):
        # 广度优先搜索
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            'A': 'CGT',
            'C': 'AGT',
            'G': 'CAT',
            'T': 'CGA'
        }
        queue = [(start, 0)]

        while queue:
            node, step = queue.pop(0)
            if node == end:
                return step
            for i, s in enumerate(node):
                for c in change_map[s]:
                    new = node[:i] + c + node[i+1:]
                    if new in bank:
                        queue.append((new, step+1))
                        bank.remove(new)
        return -1

    def min_mutation2(self, start, end, bank):
        # 双向广度优先搜索
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {
            'A': 'CGT',
            'C': 'AGT',
            'G': 'ACT',
            'T': 'ACG'
        }
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change_map[s]:
                        new = node[:i] + c + node[i+1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            if len(end_set) < len(start_set):
                # 每次选取数量较少的集合遍历
                start_set, end_set = end_set, start_set
        return -1


if __name__ == '__main__':
    start = 'AAAAACCC'
    end = 'AACCCCCC'
    bank = ['AAAACCCC', 'AAACCCCC', 'AACCCCCC']
    sol = Solution()
    # res = sol.min_mutation(start, end, bank)
    res = sol.min_mutation2(start, end, bank)
    print(res)
