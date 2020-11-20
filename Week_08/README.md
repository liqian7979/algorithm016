学习笔记
## 位运算
### 位运算符
##### 1.为什么需要位运算
    机器里的数字表示方式和存储格式就是 二进制。
    十进制 <——> 二进制：如何转换
   [如何从十进制转换为二进制](https://zh.wikihow.com/%E4%BB%8E%E5%8D%81%E8%BF%9B%E5%88%B6%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E8%BF%9B%E5%88%B6)

##### 2.位运算符
在计算机中：  
| 含义 | 运算符 | 示例 |
| :-----: | :-----: | :-----: |
| 左移 | << | 0011=>0110 |
| 右移 | >> | 0110=>0011 |
| 按位或 | &#124; | 0011 &#124; 1011 => 1011 |
| 按位与 | & | 0011 & 1011 => 0011 |
| 按位取反 | ~ | 0011 => 1100 |
| 按位异或（相同为零不同为一） | ^ | 0011 ^ 1011 => 1000 |

* __XOR - 异或__  
    异或：相同为0，不同为1。也可用"不进位加法"来理解。  
    异或操作的一些特点：  
    - x ^ 0 = x  
    - x ^ 1s = ~x     //注意1s = ~0(全1)  
    - x ^ (~x) = 1s  
    - x ^ x = 0  
    - c = a ^ b => a ^ c = b, b ^ c = a     //交换两个数  
    - a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c     //associative  

* __指定位置的位运算__  
    - 将 x 最右边的 n 位清零： x & (\~0 << n)  
    - 获取 x 的第 n 位值（0或者1）： (x >> n) & 1  
    - 获取 x 的第 n 位的幂值： x & (1 << n)  
    - 仅将第 n 位置为1： x | (1 << n)  
    - 仅将第 n 位置为0： x & (\~(1 << n))  
    - 将 x 最高位至第 n 位（含）清零： x & ((1 << n) - 1)  

* __实战位运算要点__  
    - 判断奇偶：  
        x % 2 == 1 ——> (x & 1) == 1  
        x % 2 == 0 ——> (x & 1) == 0  
    - x >> 1 ——> x / 2  
      即：x = x / 2; ——> x = x >> 1;  
         mid = (left + right) / 2; ——> mid = (left + right) >> 1;  
    - x = x & (x - 1)清零最低位的1  
    - x & -x => 得到最低位的1  
    - x & ~x => 0  

##### 4.实战题目
* 191.位1的个数
```
# 1. for loop: 0 --> 32
# 2. %2, //2
# 3. &1, x = x >> 1; (32)
# 4. while (x > 0) {count ++; x = x & (x-1)}
```

* 231.2的幂
```
# 整数的二进制表示形式里面有且仅有一个二进制位是1.
def isPowerOfTwo(n):
    return n != 0 and (n & (n - 1)) == 0
```

* 190.颠倒二进制位
```
# 1.int --> "010101" string --> reverse --> int  巨慢无比
# 2.int --> 位运算
```

* N皇后II
```

```

* 338.比特位计数
```
# DP + 位运算
```

### 算数移位与逻辑移位

### 位运算的应用

## 布隆过滤器和LRU缓存
### 布隆过滤器的实现及应用
##### 1.布隆过滤器 Bloom Filter
* Bloom Filter vs Hash Table  
    一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中。
    优点是空间效率和查询时间都远远超过一般的算法。
    缺点是有一定的误识别率和删除困难。

* 案例  
    - 比特币网络
    - 分布式系统(Map-Reduce) —— Hadoop、search engine
    - Redis缓存
    - 垃圾邮件、评论等的过滤

* Python实现
```

```

### LRU Cache的实现、应用和题解
##### 1.Cache缓存
   [Understanding the Meltdown exploit](https://www.sqlpassion.at/archive/2018/01/06/understanding-the-meltdown-exploit-in-my-own-simple-words/)

##### 2.LRU Cache
    两个要素：大小、替换策略
    Hash Table + Double LinkedList
    O(1)查询
    O(1)修改、更新
    替换策略：LFU-least frequently used、LRU-least recently used
   [替换算法总揽](https://en.wikipedia.org/wiki/Cache_replacement_policies)

##### 3.实战题目
* LRU缓存机制
```
class LRUCache(object): 
    def __init__(self, capacity): 
        self.dic = collections.OrderedDict() 
        self.remain = capacity

    def get(self, key): 
        if key not in self.dic: 
            return -1 
        v = self.dic.pop(key) 
        self.dic[key] = v   # key as the newest one 
        return v 

    def put(self, key, value): 
        if key in self.dic: 
            self.dic.pop(key) 
        else: 
            if self.remain > 0: 
                self.remain -= 1 
            else:   # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value
```


## 排序算法  
    1.比较类排序：  
        通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此也被称为非线性时间比较类排序。
    2.非比较类排序：  
        不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序。
        缺点：一般只能用于整型的数据排序，同时需要额外的辅助内存空间。

##### 初级排序 - O(n^2)  
    1.选择排序（Selection Sort）  
        每次找最小值，然后放到待排序数组的起始位置。  
    2.插入排序（Insertion Sort）  
        从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。  
    3.冒泡排序（Bubble Sort）  
        嵌套循环，每次查看相邻的元素，如果逆序，则交换。  

##### 高级排序 - O(n*log(n))
* 快速排序（Quick Sort）  
    数组取标杆 pivot，将小元素放 pivot 左边，大元素放右侧，然后依次对左边和右边的子数组继续快排；以达到整个序列有序。

* 归并排序（Merge Sort）- 分治  
    1.把长度为n的输入序列分成两个长度为n/2的子序列；  
    2.对这两个子序列分别采用归并排序；  
    3.将两个排序好的子序列合并成一个最终的排序序列。

* 归并 vs 快排  
    归并和快排具有相似性，但步骤顺序相反；  
    归并：先排序左右子数组，然后合并两个有序子数组；  
    快排：先调配出左右子数组，然后对于左右子数组进行排序。

* 堆排序（Heap Sort）- 堆插入O(log(n))，取最大/小值O(1)  
    1.数组元素依次建立小顶堆；  
    2.依次取堆顶元素，并删除。






















