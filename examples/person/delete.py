"""
蝉镜 - 定制数字人实例

本示例展示如何使用delete方法删除定制数字人
"""
from chanjing.core import ChanjingHttpClient
from chanjing.customised.person import CustomisedPerson,DeleteCustomisedPersonRequest
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
    """演示如何使用detail方法获取定制数字人详情"""
    # 初始化客户端
    client = ChanjingHttpClient(APP_ID, APP_SECRET)

    print("删除定制数字人示例")
    print("-" * 30)

    # 删除定制数字人参数
    request = DeleteCustomisedPersonRequest(
        id = "C-9c70756460a246b59e377e45e9cc7990"
    )

    response = CustomisedPerson(client).delete(request)

    print("删除定制数字人返回结果:")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())