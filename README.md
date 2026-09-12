# cs

编译原理课程 · 实验1：AI 软件开发环境安装与配置

## 实验目的

建立可支撑个人软件持续开发的 IDE、运行时、Git 与 GitHub/Gitee 基础环境，完成 AI 开发工具的安装接入与模型 API 的最小调用。

## 环境清单

| 工具 | 版本 | 说明 |
|------|------|------|
| 操作系统 | Windows | 本机 |
| Git | 2.x | 版本控制 |
| Python | 3.x | 运行时 |
| Node.js | 24.x | 用于安装 AI CLI 工具 |

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API 密钥

复制 `.env.example` 为 `.env`，填入你的 DeepSeek API Key：

```bash
cp .env.example .env
```

> `.env` 已加入 `.gitignore`，不会泄露到仓库。

### 3. 运行模型 API 调用示例

```bash
python deepseek_api_call.py
```

## 仓库结构

```
cs/
├── .env.example          # 环境变量模板
├── .gitignore            # Git 忽略规则（含 .env）
├── README.md             # 本文件
├── requirements.txt      # Python 依赖
└── deepseek_api_call.py  # 模型 API 最小调用脚本（2.5）
```

## AI 开发工具（2.4）

| 工具 | 用途 | 状态 |
|------|------|------|
| DeepSeek Harness | AI 编程助手 | 已配置 |
| Claude Code | AI 编程助手 | 已安装 `npm i -g @anthropic-ai/claude-code` |

## Git 提交记录

| Commit | 说明 |
|--------|------|
| a349860 | 初始化：.gitignore / .env.example / README / API 调用脚本 |

## 许可

MIT
