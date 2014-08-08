"""
Project Euler Problem #17
==========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

nums = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',\
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',\
        'eighteen', 'nineteen', 'twenty']
nums += [''] * 80
nums[30] = 'thirty'
nums[40] = 'forty'
nums[50] = 'fifty'
nums[60] = 'sixty'
nums[70] = 'seventy'
nums[80] = 'eighty'
nums[90] = 'ninety'

def numToWord(n):
    nstr = str(n)[::-1]

    result = ''

    i = len(nstr) - 1
    
    while i >= 0:
        current = int(nstr[i])
        if (current != 0):
            if i == 3:
                result += nums[current] + 'thousand'
            elif i == 2:
                result += nums[current] + 'hundred'
            elif i == 1:
                if len(nstr) > 2:
                    result += 'and'
                if (current == 1):
                    i -= 1
                    current = current * 10 + int(nstr[i])
                    result += nums[current]
                else:
                    result += nums[current * 10]
            else:
                if len(nstr) > 2 and int(nstr[i+1]) == 0:
                    result += 'and'
                result += nums[current]

        i -= 1

    #return result
    return len(result)

print sum([numToWord(i) for i in range(1, 1001)])
