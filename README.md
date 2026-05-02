# MSTI

本项目采用轻量的 **基于 Python 的静态站点生成（SSG）** 架构，通过 Python Builder 将结构化数据自动化注入前端模板。

## Build

```powershell
uv run main.py
```

生成静态网页目录：`dist/`

## Config Source

前端页面配置由 Python 注入，配置入口是：`config.py` 中的 `XXBI`。

- `dimensions`: 维度定义
- `questions`: 题目列表
- `types`: 人格类型

各字段的意义见 `schema.py`
