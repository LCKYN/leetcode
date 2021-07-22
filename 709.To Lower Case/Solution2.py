class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = "".join([(chr(ord(i)+32)if 65 <= ord(i) <= (65+26) else i) for i in str])
        return res