"""
蝉镜 - 定制声音实例 

本示例展示如何使用list方法获取定制声音列表
"""
from chanjing.core import ChanjingHttpClient
from chanjing.customised.audio import CustomisedAudio,ListCustomisedAudioRequest
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
    """演示如何使用list方法获取定制声音列表"""
    # 初始化客户端
    client = ChanjingHttpClient(APP_ID, APP_SECRET)

    # 列表参数
    request = ListCustomisedAudioRequest(
           page=1,
           page_size=10
        )
    
    print("获取定制声音列表示例")
    print("-" * 30)

    response =  CustomisedAudio(client).list(request)
    print("获取定制声音列表返回结果:")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())