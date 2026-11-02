# agent-playground

WorkBuddy 自动巡检链路的演示仓库。

## 工作方式

1. 在 `tickets/` 下新建一个 `.md` 文件（相当于开 issue），头部 `status: open`
2. WorkBuddy 每小时轮询：`git pull` → 读取 open 的 ticket → 读相关源码 → 定位问题
3. 分析结果写入 `analysis/<ticket-id>.md`，ticket 的 `status` 改为 `analyzed`
4. 自动 `git commit` + `git push`，你在 GitHub 网页上就能看到更新

## 目录

- `src/calculator.py` — 基础计算（除零、空列表）
- `src/list_utils.py` — 列表工具（off-by-one、边界检查缺失）
- `src/user_service.js` — 用户服务（异步返回值、错误处理）
- `tickets/` — 待处理任务队列
- `analysis/` — agent 输出的分析报告

> 本仓库仅用于测试，代码故意留有缺陷，不要用于生产。
