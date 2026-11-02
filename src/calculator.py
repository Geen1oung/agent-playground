"""基础计算工具，用于演示 WorkBuddy 自动巡检。"""


def divide(a, b):
    """返回 a / b。"""
    return a / b  # BUG: 未处理 b == 0，直接 ZeroDivisionError


def average(numbers):
    """返回列表平均值。"""
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)  # BUG: 空列表时 len == 0，ZeroDivisionError


def percent(part, whole):
    """返回 part 占 whole 的百分比。"""
    return (part / whole) * 100  # BUG: whole == 0 时崩溃
