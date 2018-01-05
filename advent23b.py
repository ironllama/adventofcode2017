# Advent of Code 2017
# Day 23 - Part II
# mushmine - Python


'''
To optimize, I couldn't really see any discernable repeating patterns. So, I cheated and looked online to see how others had solved this problem. As it turns out, I'm glad I did, because the approach was something that was somewhat obvious, but it has been so long since I've done any assembly, that I didn't consider that the puzzle input can actually be translated into source.

Examples:
set b 79 -> b = 79
jnz a 2  -> if a != 0: GOTO SOMEPLACE (usually a loop block or function)
sub d -1 -> d += 1
mul g e  -> g *= e

So, my input translates into:
b = 79
c = b
if a != 0: GOTO A
GOTO B
A: b *= 100
b += 100000
c = b
c += 17000
B: f = 1
d = 2
E: e = 2
D: g = d
g *= e
g -= b
if g != 0: goto C
f = 0
C: e += 1
g = e
g -= b
if g != 0: goto D
d += 1
g = d
g -= b
if g != 0: goto E
if f != 0: goto F
h += 1
F: g = b
g -= c
if g != 0: goto G
goto H
G: b += 17
goto B
H:

If we take out some of the GOTO's by properly blocking some of the operations, we get:
b = 79
c = b
if a != 0:
    b *= 100
    b += 100000
    c = b
    c += 17000
while(true):
    f = 1
    for d in range(2, b):
        for e in range (2, b):
            g = d
            g *= e
            g -= b
            if g != 0: continue
            f = 0
    if f == 0:
        h += 1
    g = b
    g -= c
    if g != 0:
        b += 17
    else:
        break;


Then we compress some of the assignments (g is being reused to do computation) and add some variables to make it a bit easier to read:
b = 79
c = b
if a != 0:
    b = (b * 100) + 100000
    c = b + 17000
while(true):
    f = 1
    for d in range(2, b):
        for e in range (2, b):
            if (d * e) == b:
                f = 0;

    if f == 0:
        h += 1
    if b != c:
        b += 17
    else:
        break;


Looks like b is increased by 17 per loop and a is always going to be 1 in Part II, so we get:
b = (79 * 100) + 100000
c = b + 17000
while(true):
    f = 1
    for d in range(2, b, 17):
        for e in range (2, b, 17):
            if (d * e) == b:
                f = 0;

    if f == 0: h += 1
    if b == c: break


Which makes it pretty clear that we are looking for the number of non-prime numbers(h) between 107900(b) and 124900(c), using loop variables (d and e), and a boolean flag(f), with one reused register just for storing computation(g). So, we write a program do that.
'''

non_primes = 0
for d in range(107900, 124901, 17):
    for e in range(2, d):
        # print("CHECKING: d", d, "e", e)
        if d % e == 0:
            non_primes += 1
            break

print("END VALUE OF H:", non_primes)