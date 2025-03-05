"""
蝉镜 - 定制声音实例

本示例展示如何使用create方法创建定制声音
"""
from chanjing.core import ChanjingHttpClient
from chanjing.customised.audio import CustomisedAudio,CreateCustomisedAudioRequest
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
    """演示如何使用create方法创建定制声音"""
    # 初始化客户端
    client = ChanjingHttpClient(APP_ID, APP_SECRET)

    # 定制声音
    request = CreateCustomisedAudioRequest(
            name="2测试2",
            url="https://www.cambridgeenglish.org/images/153149-movers-sample-listening-test-vol2.mp3",
            callback="https://xx.com",
        )
    
    print("创建定制声音示例")
    print("-" * 30)

    response = CustomisedAudio(client).create(request)
    
    print("创建定制声音返回结果:")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())