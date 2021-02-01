#!/usr/bin/python

# Convert .crd to SIMH ASCII

import sys

co = """
] 11-0
@ 4-8
* 11-4-8
| 0-2-8
! 11-2-8
} 0-7-8
" 12-7-8

. 12-3-8
) 12-4-8
+ 12
$ 11-3-8
* 11-4-8
- 11
/ 0-1
, 0-3-8
( 0-4-8
= 3-8
A 12-1
B 12-2
C 12-3
D 12-4
E 12-5
F 12-6
G 12-7
H 12-8
I 12-9
J 11-1
K 11-2
L 11-3
M 11-4
N 11-5
O 11-6
P 11-7
Q 11-8
R 11-9
S 0-2
T 0-3
U 0-4
V 0-5
W 0-6
X 0-7
Y 0-8
Z 0-9
0 0
0 12-0
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
"""

# bit value of each row of holes
crd = (
(0, 0x80),
(0, 0x40),
(0, 0x20),
(0, 0x10),
(0, 8),
(0, 4),
(0, 2),
(0, 1),
(0x80, 0),
(0x40, 0),
(0x20, 0),
(0x10, 0),
)

# number of each row on card
holes = 12, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

tab = []

for l in co.split("\n"):
    x = l.strip()
    if x == "": continue
    char, h = x.split()
    hh = h.split("-")
    n1, n2 = 0, 0
    for y in hh:
        for q, z in enumerate(holes):
            if z == int(y):
                n1 += crd[q][0]
                n2 += crd[q][1]
    tab.append((char, n1, n2))
        
        
f = open(sys.argv[1], "rb")

n = 0
line = ""

while True:
    r = " "
    try:
        ch = ord(f.read(1))
        ch1 = ord(f.read(1))
    except:
        print("\r")
        sys.exit()
    n += 1
    if n > 80:
        n = 1
        print(line.rstrip() + "\r")
        line = ""
    for t in tab:
        if ch == t[1] and ch1 == t[2]:
            r = t[0]
    line += r
     
