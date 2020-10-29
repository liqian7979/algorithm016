# @Author   : debian-liqian
# @Email    : liqian@infinities.com.cn
# @Time     : 20-10-29 下午3:55
# @File     : Trie.py
# @Software : PyCharm
"""
208. 实现Trie (前缀树)
实现一个Trie (前缀树)，包含 insert, search 和 startsWith 这三个操作。
示例:
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // 返回 true
    trie.search("app");     // 返回 false
    trie.startsWith("app"); // 返回 true
    trie.insert("app");
    trie.search("app");     // 返回 true
说明:
    · 你可以假设所有的输入都是由小写字母 a-z 构成的
    · 保证所有输入均为非空字符串
"""


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


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    sea1 = trie.search('apple')
    print(sea1)
    sea2 = trie.search('app')
    print(sea2)
    stw = trie.startsWith('app')
    print(stw)
    trie.insert('app')
    sea3 = trie.search('app')
    print(sea3)
    sea4 = trie.search('apple')
    print(sea4)