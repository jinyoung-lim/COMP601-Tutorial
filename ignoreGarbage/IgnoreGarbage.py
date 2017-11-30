""" File: IgnoreGarbage.py
Author: JJ Lim
Date: Nov 29 2017

A class dedicated to solve "Ignore The Garbage" problem from Open Kattis (https://open.kattis.com/problems/ignore).
"""
def main():
    kList = readFile("sample.in")
    for k in kList:
        norm = kToNormNum(k)
        upDown = normToUpDown(norm)
        print(upDown)

def normToUpDown(norm):
    norm = str(norm)
    upDown = ""
    for digit in norm:
        if digit == '6':
            digit = '9'
        elif digit == '9':
            digit = '6'
        upDown += digit
    return upDown

def kToNormNum(k):
    k = int(k)
    tensAndMore = k // 7
    ones = k % 7

    if ones == 3:
        ones = 5
    elif ones == 4:
        ones = 6
    elif ones == 5:
        ones = 8
    elif ones == 6:
        ones = 9
    elif ones == 7:
        ones = (tensAndMore + 1) * 10

    return (tensAndMore * 10 + ones)



def readFile(file):
    with open(file) as f:
        kAsStrList = []
        for line in f:
            kAsStrList.append(line.rstrip("\n"))
    return kAsStrList


if __name__ == "__main__":
    main()