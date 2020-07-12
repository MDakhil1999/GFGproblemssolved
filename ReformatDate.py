# Leetcode 1507

# https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        print(date)
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        s = ""
        s += date[-4:]
        s += "-"
        if len(date) == 13:
            mon = date[5:8]
            print(mon)
            indi = month.index(mon) + 1
            print(indi)
        else:
            mon = date[4:7]
            print(mon)
            indi = month.index(mon) + 1
            print(indi)
        mont = ""
        if indi < 10:
            mont += "0"
        mont += str(indi)
        s += mont
        s += "-"
        if len(date) == 13:
            s += date[:2]
        else:
            s += "0"
            s += date[0]
        
        return s
        
