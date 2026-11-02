"""列表工具函数，用于演示 WorkBuddy 自动巡检。"""


def get_last_n(items, n):
    """返回列表最后 n 个元素。"""
    return items[-n - 1:]  # BUG: off-by-one，实际取到 n+1 个元素


def find_index(items, target):
    """返回 target 的下标，找不到返回 -1。"""
    for i, value in enumerate(items):
        if value == target:
            return i
    return -1


def safe_get(items, index):
    """安全取下标，越界返回 None。"""
    return items[index]  # BUG: 函数名承诺安全，但没有边界检查，越界抛 IndexError
