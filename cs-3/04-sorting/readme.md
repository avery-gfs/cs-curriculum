# Sorting

## Warm Up

Sort these emojis

```
🦀 🥦 🫖 🐼 🧲 🐼 🏀 🫖 🪭 💩 🍄 ⚽ 🥑 🥦 🦘 🫖
```

## Bubble Sort

Bubble sort: compare values that are next to each other, and swap them if
they're out of order.

---

```
[ ( 🦀   🥦 ) 🫖   🐼   🧲   🐼   ]
```

---

```
[ ( 🥦   🦀 ) 🫖   🐼   🧲   🐼   ]
```

---

```
[   🥦 ( 🦀   🫖 ) 🐼   🧲   🐼   ]
```

---

```
[   🥦   🦀 ( 🫖   🐼 ) 🧲   🐼   ]
```

---

```
[   🥦   🦀 ( 🐼   🫖 ) 🧲   🐼   ]
```

---

```
[   🥦   🦀   🐼 ( 🫖   🧲 ) 🐼   ]
```

---

```
[   🥦   🦀   🐼 ( 🧲   🫖 ) 🐼   ]
```

---

```
[   🥦   🦀   🐼   🧲 ( 🫖   🐼 ) ]
```

---

```
[   🥦   🦀   🐼   🧲 ( 🐼   🫖 ) ]
```

---

```
[ ( 🥦   🦀 ) 🐼   🧲   🐼   🫖   ]
```

---

```
[   🥦 ( 🦀   🐼 ) 🧲   🐼   🫖   ]
```

---

```
[   🥦 ( 🐼   🦀 ) 🧲   🐼   🫖   ]
```

---

```
[   🥦   🐼 ( 🦀   🧲 ) 🐼   🫖   ]
```

---

```
[   🥦   🐼   🦀 ( 🧲   🐼 ) 🫖   ]
```

---

```
[   🥦   🐼   🦀 ( 🐼   🧲 ) 🫖   ]
```

---

```
[ ( 🥦   🐼 ) 🦀   🐼   🧲   🫖   ]
```

---

```
[ ( 🐼   🥦 ) 🦀   🐼   🧲   🫖   ]
```

---

```
[   🐼 ( 🥦   🦀 ) 🐼   🧲   🫖   ]
```

---

```
[   🐼   🥦 ( 🦀   🐼 ) 🧲   🫖   ]
```

---

```
[   🐼   🥦 ( 🐼   🦀 ) 🧲   🫖   ]
```

---

```
[ ( 🐼   🥦 ) 🐼   🦀   🧲   🫖   ]
```

---

```
[   🐼 ( 🥦   🐼 ) 🦀   🧲   🫖   ]
```

---

```
[   🐼 ( 🐼   🥦 ) 🦀   🧲   🫖   ]
```

---

```
[ ( 🐼   🐼 ) 🥦   🦀   🧲   🫖   ]
```

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

^ Helpful language feature, or silly Python nonsense?
