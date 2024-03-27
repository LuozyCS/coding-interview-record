'''


'''
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #  哈希
        # 找到一个就保存一下index
        # 怎么哈希, acwing好像有一个, 一个词存成一个哈希
        # 字符串哈希 841
        # 两种做法 排序和计数, 计数更快, 排序更直观
        # 但是不能用乘法之类的那种, 那种是有可能错的.

        
        # # 排序 dict
        
        # dictA = {}
        # for s in strs:
        #     s_ = "".join(sorted(s))
        #     if s_ not in dictA:
        #         dictA[s_] = [s]
        #     else:
        #         dictA[s_].append(s)

        # return list(dictA.values())
        # ------

        # # 排序defaultdict

        # # defaultdict是Python内建dict类的一个子类，第一个参数为default_factory属性提供初始值，默认为None。它覆盖一个方法并添加一个可写实例变量。
        # # collections.defaultdict()的其他功能与dict相同，但会为一个不存在的键提供默认值，从而避免KeyError异常。

        # mp = collections.defaultdict(list)

        # for s in strs:
        #     s_ = "".join(sorted(s))
        #     mp[s_].append(s)
        # return list(mp.values())

        # ------

        # 计数

        
        mp = collections.defaultdict(list) # 应该是默认value是list?
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1 # 有一个该字符就计数, 是符合题意的
                # 因为题意就是不同字符的排列组合成不同的词
            # mp[count].append(s) # unhashable type: 'list'
            # 因为字典的键，必须是不可变类型，所以用tuple 元组。
            mp[tuple(count)].append(s)
        return list(mp.values())

