---
id: T-001
title: calculator.py 除数为 0 时崩溃
type: bug
status: analyzed
created: 2026-11-02
---

调用 `divide(10, 0)` 直接崩溃：

```
Traceback (most recent call last):
  File "src/calculator.py", line 7, in divide
    return a / b
ZeroDivisionError: division by zero
```

`average([])` 也一样崩。希望加上保护。
