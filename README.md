cs
编译原理课程 · 实验1：AI 软件开发环境安装与配置

实验目的
建立可支撑个人软件持续开发的 IDE、运行时、Git 与 GitHub/Gitee 基础环境，完成 AI 开发工具的安装接入与模型 API 的最小调用。

环境清单
工具	版本	说明
操作系统	Windows 10/11	本机
Git	2.x	版本控制
Python	3.14	运行时
Node.js	24.x	用于安装 AI CLI 工具
Claude Code	2.1.269	AI 编程助手（CLI）
DeepSeek Harness	最新版	AI 编程助手（Web 界面）
快速开始
1. 安装依赖



py -m pip install -r requirements.txt
依赖说明：requests（调用 DeepSeek API）、python-docx（生成实验报告 Word 文档）。

2. 配置 API 密钥
使用 Windows 用户环境变量管理密钥（不会进入仓库）：




setx DEEPSEEK_API_KEY "sk-你的密钥"
或将 .env.example 复制为 .env 填入 Key；.env 已加入 .gitignore。

3. 运行模型 API 调用示例



py deepseek_api_call.py
成功输出：HTTP 200、响应时延、Token 用量与模型回复。

仓库结构



cs/
├── .env.example          # 环境变量模板（不含真实密钥）
├── .gitignore            # Git 忽略规则（含 .env）
├── README.md             # 本文件
├── LICENSE               # MIT 开源许可
├── requirements.txt      # Python 依赖（requests / python-docx）
├── deepseek_api_call.py  # 模型 API 最小调用脚本（2.5）
└── generate_report.py    # 实验报告 Word 文档生成脚本
AI 开发工具（2.4）
工具	用途	状态
DeepSeek Harness	AI 编程助手（图形界面）	已配置
Claude Code	AI 编程助手（命令行，接入 DeepSeek 兼容端点）	已配置
Git 提交记录
Commit	类型	说明
2f1cd87	init	首个提交：.gitignore / .env.example / README / API 调用脚本
aa9c5d9	init	补充项目文件
（本次）	docs	更新 README：依赖说明、仓库结构、commit hash
许可
本项目基于 MIT License 开源，详见 LICENSE 文件。
