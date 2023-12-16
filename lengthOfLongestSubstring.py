# 使用滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,lenth= -1,0
        dic={}
        for j in range(len(s)):
            if s[j] in dic:
                i=max(dic[s[j]],i)
            dic[s[j]]=j
            lenth = max(j-i,lenth)
        return lenth
