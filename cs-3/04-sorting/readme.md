# Sorting

## Warm Up

Sort these emojis

```
🦀 🥦 🫖 🐼 🧲 🐼 🏀 🫖 🪭 💩 🍄 ⚽ 🥑 🥦 🦘 🫖
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

---

## Swapping List Values

To swap values at indices `i` and `j`

...

```
tmp = items[i]
items[i] = items[j]
items[j] = tmp
```

...

Or

```
items[i], items[j] = items[j], items[i]
```

...

(^ Helpful language feature, or silly Python nonsense?)

---

## Complexity

For a list with `10` values, how many comparisons do we need?

...

$$
9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
$$

...

For a list with $n$ values, how many comparisons do we need?

...

$$
(n - 1) + (n - 2) + ... + 2 + 1 = \frac{n^2 + n}{2}
$$

## Complexity

$$
\frac{n^2 + n}{2}
$$

<img height="500" src="/assets/quadratic.png"/>

Big O notation (asymptotic notation)

$$
O(n^2)
$$

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

<img height="500" src="/assets/asymptotics.png"/>
