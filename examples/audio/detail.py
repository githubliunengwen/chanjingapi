"""
蝉镜 - 定制声音实例

本示例展示如何使用detail方法获取定制声音详情
"""
from chanjing.core import ChanjingHttpClient
from chanjing.customised.audio import CustomisedAudio
import asyncio
import os

"""
   APP_ID: API应用ID
   APP_SECRET: API应用密钥

"""
APP_ID = "cj_test_id"
APP_SECRET = "cj_test_secret_key"

# from dotenv import load_dotenv


# # 加载环境变量
# load_dotenv()

# # 从环境变量获取API密钥和基础URL
# ADMIN_API_KEY = os.getenv("DIFY_ADMIN_KEY")
# BASE_URL = os.getenv("DIFY_BASE_URL")


async def main():
    """演示如何使用detail方法获取定制声音详情"""
    # 初始化客户端
    client = ChanjingHttpClient(APP_ID, APP_SECRET)

    print("获取定制声音详情示例")
    print("-" * 30)

    response = CustomisedAudio(client).detail("C-Audio-039372c2c3854155808c3097b6e7897f")
    print("获取定制声音详情返回结果:")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())