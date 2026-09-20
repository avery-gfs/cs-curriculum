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
3 2 5 1 4 1
```

---

```
3 2 5 1 4 1
^ ^
```

---

```
2 3 5 1 4 1
^ ^
```

---

```
2 3 5 1 4 1
  ^ ^
```

---

```
2 3 5 1 4 1
    ^ ^
```

---

```
2 3 1 5 4 1
    ^ ^
```

---

```
2 3 1 5 4 1
      ^ ^
```

---

```
2 3 1 4 5 1
      ^ ^
```

---

```
2 3 1 4 5 1
        ^ ^
```

---

```
2 3 1 4 1 5
        ^ ^
```

---

```
2 3 1 4 1 5
^ ^
```

---

```
2 3 1 4 1 5
  ^ ^
```

---

```
2 1 3 4 1 5
  ^ ^
```

---

```
2 1 3 4 1 5
    ^ ^
```

---

```
2 1 3 4 1 5
      ^ ^
```

---

```
2 1 3 1 4 5
      ^ ^
```

---

```
2 1 3 1 4 5
^ ^
```

---

```
1 2 3 1 4 5
^ ^
```

---

```
1 2 3 1 4 5
  ^ ^
```

---

```
1 2 3 1 4 5
    ^ ^
```

---

```
1 2 1 3 4 5
    ^ ^
```

---

```
1 2 1 3 4 5
^ ^
```

---

```
1 2 1 3 4 5
  ^ ^
```

---

```
1 1 2 3 4 5
  ^ ^
```

---

```
1 1 2 3 4 5
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

```
items[i], items[j] = items[j], items[i]
```

...

^ Helpful language feature, or silly Python nonsense?
