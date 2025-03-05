"""
蝉镜 - 定制数字人实例

本示例展示如何使用create方法创建定制数字人
"""
from chanjing.core import ChanjingHttpClient
import chanjing.schemas
from chanjing.customised.person import CustomisedPerson,CreateCustomisedPersonRequest
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
    """演示如何使用create方法创建定制数字人"""
    # 初始化客户端
    client = ChanjingHttpClient(APP_ID, APP_SECRET)

    # 定制数字人
    request = CreateCustomisedPersonRequest(
            name="2测试2",
            material_video="https://www.w3school.com.cn/example/html5/mov_bbb.mp4",
            callback="https://xx.com",
            train_type=""
        )
    
    print("建定制数字人示例")
    print("-" * 30)

    response = CustomisedPerson(client).create(request)
    
    print("创建定制数字人返回结果:")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())