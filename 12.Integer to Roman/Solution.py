class Solution:
    def intToRoman(self, num: int) -> str:

        r = 'IVXLCDM'
        res = ''
        count = 0

        while(num):

            temp = num % 10
            
            if(temp == 4):
                res = r[count * 2] + r[count * 2 + 1] + res
            elif(temp == 9):
                res = r[count * 2] + r[count * 2 + 2] + res
            elif(temp < 4):
                res = r[count * 2] * temp + res
            else:
                res = r[count * 2 + 1] + r[count * 2] * (temp - 5) + res

            num = num // 10
            count += 1

        return res