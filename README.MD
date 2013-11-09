#IP_Converter

These are two simple python programs, one for converting `prefix` (say 1.2.3.4/255.255.255.128 or 1.2.3.4/28) to `range` (such as 1.2.3.100-1.2.3.200), and another converting `range` to `prefix`.

---
####`prefix2range.py` --- convert prefix to range

The algorithm to convert prefix to range is quite simple. First change the mask to binary number (such as 111…11100...00), then keep the bits of the IP unchanged when the corresponding bits of mask are ‘1’. When the bits of mask are ‘0’, change the corresponding bits to ‘0’ to get the lower bound of IP and change corresponding bits to ‘1’ to get the upper bound of IP. 

![image](http://github.com/fooozhe/IP_Converter/screenshots/prefix2range.png)

---
####`range2prefix2.py` --- convert range to prefix

This algorithm is much more complex than that above. First, convert two IPs to binary number. Define the flag as the first different bit between the two IPs, IP1r1 as the furthest right bit of IP1.


It must be noted that the source code doesn’t contain any extra parts to handle the invalid input, such as wrong IP format (300.2.3) or wrong IP range (1.2.3.5 – 1.2.3.4). It will cause nothing but errors.

![image](http://github.com/fooozhe/IP_Converter/screenshots/range2prefix.png)Since the algorithm is implemented using recursion, the worst case is that the algorithm scans each bit of IP from right to left unless IP1r1 <= flag (31 times) and then scans from left to right (31 times). So the recursion function may be called 62 times in the worst case. Each recursion has three 32-bit variables, which results in that the memory consumption is at least 4B * 3 * 62 =744B. And the biggest number of policy is 62.