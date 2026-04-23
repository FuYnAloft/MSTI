# MSTI

## Build

```powershell
uv run python main.py
```

生成静态网页目录：`dist/`

## Config Source

前端页面配置由 Python 注入，配置入口是：`config.py` 中的 `XXBI`。

- `dimensions`: 维度定义（含 `explanation` 和 `thresholds`）
- `questions`: 题目列表（支持 `dependsOn`）
- `types`: 人格类型（含 `image`、`pattern`）
