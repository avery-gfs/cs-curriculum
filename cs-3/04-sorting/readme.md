# Sorting

## Warm Up

Sort these emojis

```
🦀 🥦 🫖 🐼 🧲 🐼 🏀 🫖 🪭 💩 🍄 ⚽ 🥑 🥦 🦘 🫖
```

[Comparitor](https://avery-gfs.github.io/cs-curriculum/apps/emoji-comparison.html)

[Virtual cards](https://avery-gfs.github.io/cs-curriculum/apps/click-drag.html?q=🦀,🥦,🫖,🐼,🧲,🐼,🏀,🫖,🪭,💩,🍄,⚽,🥑,🥦,🦘,🫖)

...

Why use emojis?

...

```
[8, 7, 12, 4, 10, 4, 3, 12, 11, 5, 2, 1, 6, 7, 9, 12]
```

Sorting numbers is too intuitive! We're interested in **comparison sorting**,
where we don't have any intuition about what values are "large" or "small", and
we can only rely on direct comparisions between items.

## Lexicographic Comparison

```py
ord("A")
ord("a")
ord("🥑")
```

```
65
97
129361
```

## Bubble Sort

- Compare values that are next to each other, and swap them if they're out of
  order.

- Do this for every pair of adjacent values in the list (a single pass).

- This builds up a sorted sublist at the end of the list. After each pass this
  sorted sublist grows.

- Keep doing passes until the entire list is sorted.

---

```
5 3 2 5 1 4 1
^ ^
```

---

```
3 5 2 5 1 4 1
^ ^
```

---

```
3 5 2 5 1 4 1
  ^ ^
```

---

```
3 2 5 5 1 4 1
  ^ ^
```

---

```
3 2 5 5 1 4 1
    ^ ^
```

---

```
3 2 5 5 1 4 1
      ^ ^
```

---

```
3 2 5 1 5 4 1
      ^ ^
```

---

```
3 2 5 1 5 4 1
        ^ ^
```

---

```
3 2 5 1 4 5 1
        ^ ^
```

---

```
3 2 5 1 4 5 1
          ^ ^
```

---

```
3 2 5 1 4 1 5
          ^ ^
```

---

```
3 2 5 1 4 1 5
^ ^
```

---

```
2 3 5 1 4 1 5
^ ^
```

---

```
2 3 5 1 4 1 5
  ^ ^
```

---

```
2 3 5 1 4 1 5
    ^ ^
```

---

```
2 3 1 5 4 1 5
    ^ ^
```

---

```
2 3 1 5 4 1 5
      ^ ^
```

---

```
2 3 1 4 5 1 5
      ^ ^
```

---

```
2 3 1 4 5 1 5
        ^ ^
```

---

```
2 3 1 4 1 5 5
        ^ ^
```

---

```
2 3 1 4 1 5 5
^ ^
```

---

```
2 3 1 4 1 5 5
  ^ ^
```

---

```
2 1 3 4 1 5 5
  ^ ^
```

---

```
2 1 3 4 1 5 5
    ^ ^
```

---

```
2 1 3 4 1 5 5
      ^ ^
```

---

```
2 1 3 1 4 5 5
      ^ ^
```

---

```
2 1 3 1 4 5 5
^ ^
```

---

```
1 2 3 1 4 5 5
^ ^
```

---

```
1 2 3 1 4 5 5
  ^ ^
```

---

```
1 2 3 1 4 5 5
    ^ ^
```

---

```
1 2 1 3 4 5 5
    ^ ^
```

---

```
1 2 1 3 4 5 5
^ ^
```

---

```
1 2 1 3 4 5 5
  ^ ^
```

---

```
1 1 2 3 4 5 5
  ^ ^
```

---

```
1 1 2 3 4 5 5
^ ^
```

## Correctness

How do we know this works?

Invariant: a property of a system that is perserved, even as the state of the
system changes.

...

> After the $n^{th}$ pass, the last $n$ items in the list are the largest $n$
> values, in sorted order.

Therefore, for a list with length $l$ the list will be sorted after $l$ passes.

## Complexity

For a list with `10` distinct values, how many comparisons do we need?

...

$$
9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
$$

...

For a list with $n$ distinct values, how many comparisons do we need?

...

$$
(n - 1) + (n - 2) + ... + 2 + 1 = \frac{n^2 - n}{2}
$$

---

Big O notation (asymptotic notation)

$$
\frac{n^2 - n}{2} = O(n^2)
$$

- "Quadratic growth"
- "Quadratic complexity"
- "Quadratic algorithm"

<img height="500" src="/assets/quadratic.png"/>

---

If bubble sorting a list of `10,000` items took 2 seconds, how long would we
expect it to take to sort a list of `50,000`?

...

```
10,000 items x 5 = 50,000 items
```

...

```
2 seconds x 5² = 50 seconds
```

---

<img height="700" src="/assets/asymptotics.png"/>

Quadratic complexity is a bummer

---

Examples of algorithms for these categories?

- 😇 $O(1)$
- 😉 $O(log(n))$
- 🙂 $O(n)$
- 🤔 $O(n \cdot log(n))$
- 😨 $O(n^2)$
- 💀 $O(2^n)$

## Problem: Implement Bubble Sort

```py
def bubbleSort(items):
    # ...
```

How do we break this problem down into smaller steps?

- Compare (and swap) first two values in the list
- Do a single pass through the list
- Do multiple passes through the list
- Make passes ignore already-sorted end segment

---

Looping through a range of numbers from high to low:

```py
for i in range(5, 0, -1):
    print(i)
```

What does this print?

...

```
5
4
3
2
1
```

...

_(silly Python nonsense)_

---

How to swap values at indices `i` and `j` in a list?

...

```py
tmp = items[i]
items[i] = items[j]
items[j] = tmp
```

...

```
[5, 3, 2, 5, 1, 4, 1]
```

...

```
[5, 3, 2, 5, 1, 4, 1]
 ╰───╮
tmp: 5
```

...

```
[3, 3, 2, 5, 1, 4, 1]
 ╰──╯
tmp: 5
```

...

```
[3, 5, 2, 5, 1, 4, 1]
    ╰╮
tmp: 5
```

---

Alternatively

```py
items[i], items[j] = items[j], items[i]
```

...

_(silly Python nonsense)_

## Challenge: Better Algorithm

Can you come up with a better algorithm for sorting? One that doesn't have
$O(n^2)$ complexity? Do it! Don't worry about writing code, just come up with a
description of your procedure, and an argument for why it has better algorithmic
complexity than bubble sort.

## Complexity Exercise

Which is larger?

$$
100^4
$$

Or

$$
4^{100}
$$

---

$$
4^{100} = (4^4)^{96} = 256^{96} > 100^4
$$

...

$$
log_2(100^4) = 4 \cdot log_2(100)
$$

$$
log_2(4^{100}) = 100 \cdot log_2(4)
$$

---

$$
100^4 = 100000000
$$

...

$$
4^{100} = 1606938044258990275541962092341162602522202993782792835301376
$$

...

In general, for a small number $b$ greater than $1$ and a large number $n$:

$$
b^n >> n^b
$$
