## Our Goal

For each d in gcds:

    1. Find a, b in nums where gcd(a, b) == d
    2. Find Bézout coefficients s, t such that a*s + b*t = d
    3. Compute d + s + t, then chr(that number) to get the flag char

### Step 1: Find (a, b) for each d
For each d in gcds and for each unordered pair (a, b) from nums, check if gcd(a, b) == d.

Optimization:

Only consider pairs where both are divisible by d, and then check gcd(a, b) == d.

### Step 2: Compute Bézout Coefficients
Given two numbers a, b, use the Extended Euclidean Algorithm to find integers s, t such that a*s + b*t = gcd(a, b).