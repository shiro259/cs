# -*- coding: utf-8 -*-
"""
DeepSeek API 最小调用示例（实验 2.5：模型服务与 API 密钥安全）

功能：
  1. 从环境变量 DEEPSEEK_API_KEY 读取密钥（不硬编码）
  2. 调用 DeepSeek chat/completions 接口
  3. 打印模型名称、返回内容、响应时延、token 用量

用法：
  1. 在系统环境变量中设置 DEEPSEEK_API_KEY，或在 .env 文件中写入
     setx DEEPSEEK_API_KEY "sk-你的密钥"   （Windows）
  2. python deepseek_api_call.py
"""

import os
import time
import json
import sys

try:
    import requests
except ImportError:
    print("请先安装 requests：pip install requests")
    sys.exit(1)

# 尝试从 .env 文件加载（如果安装了 python-dotenv）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
BASE_URL = "https://api.deepseek.com/v1"
MODEL = "deepseek-chat"


def main():
    if not API_KEY:
        print("[错误] 未找到 DEEPSEEK_API_KEY")
        print("请先设置环境变量：setx DEEPSEEK_API_KEY \"sk-你的密钥\"")
        print("或在项目根目录创建 .env 文件写入：DEEPSEEK_API_KEY=sk-你的密钥")
        sys.exit(1)

    # 打印密钥脱敏（仅前 6 位 + 后 4 位），用于验证
    masked = API_KEY[:6] + "****" + API_KEY[-4:] if len(API_KEY) > 10 else "****"
    print(f"[密钥] DEEPSEEK_API_KEY = {masked}")
    print(f"[模型] {MODEL}")
    print(f"[接口] {BASE_URL}/chat/completions")
    print("-" * 60)

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "你是一个简洁的助手。"},
            {"role": "user", "content": "用一句话解释什么是词法分析。"},
        ],
        "temperature": 0.7,
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    start = time.time()
    try:
        resp = requests.post(
            f"{BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
    except requests.exceptions.RequestException as e:
        print(f"[网络错误] {e}")
        sys.exit(1)

    elapsed = time.time() - start

    print(f"[HTTP 状态] {resp.status_code}")
    print(f"[响应时延] {elapsed:.3f} 秒")

    if resp.status_code != 200:
        print(f"[错误响应] {resp.text[:500]}")
        sys.exit(1)

    data = resp.json()
    content = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})

    print("-" * 60)
    print("[返回内容]")
    print(content)
    print("-" * 60)
    print(f"[Token 用量] 提示: {usage.get('prompt_tokens', '?')}  "
          f"补全: {usage.get('completion_tokens', '?')}  "
          f"总计: {usage.get('total_tokens', '?')}")


if __name__ == "__main__":
    main()
