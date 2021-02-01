#!/usr/bin/python

# Disassemble 1620 punch cards
# Output is opcode mnemonic + 5-digit P and Q addresses

import sys

c = """21 A
11 AM
22 S
12 SM
23 M
13 MM
28 LD
18 LDM
29 D
19 DM
25 TD
15 TDM
26 TF
16 TFM
31 TR
72 TNS
73 TNF
24 C
14 CM
49 B
44 BNF
45 BNR
43 BD
46 BI
47 BNI
27 BT
17 BTM
42 BB
36 RN
38 WN
35 DN
37 RA
39 WA
34 K
32 SF
33 CF
71 MF
48 H
41 NOP"""
cmd = {}
for l in c.split("\n"):
    x,y = l.split(" ")
    cmd[x] = y.strip()
for l in open(sys.argv[1]):
    for n in 0, 12, 24, 36, 48, 60, 72:
        print(cmd.get(l[n:n+2], "**") + " " + l[n+2:n+7] + " " + l[n+7:n+12] + " ", end="")
    print()
    
