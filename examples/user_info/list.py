"""
蝉镜 - 用户信息实例

本示例展示如何使用list方法获取公共数字人
"""
from chanjing.core import ChanjingHttpClient
from chanjing.user_info import UserInfo
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
    """演示如何使用list方法获取公共数字人"""
    # 初始化客户端
    client = ChanjingHttpClient(APP_ID, APP_SECRET)

    print("获取公共数字人列表示例")
    print("-" * 30)

    response =  UserInfo(client).list_common_dp()
    print("获取公共数字人返回结果:")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())