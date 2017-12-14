#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhang Zeyue"
__pkuid__  = "1700011816"
__email__  = "2607718149@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
 
    lines=lines.lower()
    tilto=lines.split()
    tys=[]
    tql={}
    for aw in tilto:
        xj=''
        for i in aw:
            if ord(i)==32 or ord(i)==39 or 97<=ord(i)<=122:
                xj+=i
            
        
        tys.append(xj)
            
    for j in tys:
        tql[j]=tql.get(j,0)+1
    
    
    dl=[(a,b) for (b,a) in list(tql.items())]
    dl.sort(reverse=True)
    for k in range(0,topn):
        print(dl[k][1],'\t',dl[k][0])
        
    pass


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        print(sys.argv)
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)