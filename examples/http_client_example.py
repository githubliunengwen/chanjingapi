"""
禅境API客户端基本用法示例
"""

import logging
import os
from chanjing.core import ChanjingHttpClient

# 设置日志级别
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """演示禅境API客户端基本用法"""
    print("禅境API客户端演示")
    print("-" * 30)
    
    # 从环境变量获取API密钥（推荐做法）
    api_key = "cj_test_id"
    api_secret  = "cj_test_secret_key"
    if not api_key:
        print("警告: 未设置CHANJING_API_KEY环境变量，使用示例API密钥")
        print("在实际使用中，请设置您的API密钥:")
        print("  Windows (PowerShell): $env:CHANJING_API_KEY='your_api_key'")
        print("  Linux/Mac: export CHANJING_API_KEY='your_api_key'")
        api_key = "example_api_key"  # 这只是一个示例，实际使用时需要替换
    
    # 初始化客户端
    client = ChanjingHttpClient(app_id=api_key,app_secret=api_secret)
    
    try:
        # # 示例1: 发送GET请求
        # print("\n示例1: 发送GET请求")
        # print("-" * 20)
        # # 注意: 这是一个示例端点，实际使用时需要替换为真实的API端点
        # response = client.request("GET", "persons")
        # print_response(response)
        
        # # 示例2: 发送带参数的GET请求
        # print("\n示例2: 发送带参数的GET请求")
        # print("-" * 20)
        # params = {
        #     "page": 1,
        #     "size": 10,
        #     "keyword": "示例"
        # }
        # response = client.request("GET", "persons", params=params)
        # print_response(response)
        
        # 示例3: 发送POST请求
        print("\n示例3: 发送POST请求")
        print("-" * 20)
        data = {
            "name": "open_api_测试",
            "material_video": "http://vjs.zencdn.net/v/oceans.mp4",
            "callback":"https://xx.com",
            "train_type":""
            }
        response = client.request("POST", "create_customised_person", json=data)
        print_response(response)
        
    except ValueError as e:
        print(f"参数错误: {e}")
    except ConnectionError as e:
        print(f"连接错误: {e}")
    except TimeoutError as e:
        print(f"请求超时: {e}")
    except Exception as e:
        print(f"请求失败: {e}")


def print_response(response):
    """打印响应信息"""
    print(f"响应代码: {response.code}")
    print(f"响应消息: {response.msg}")
    print(f"追踪ID: {response.trace_id}")
    
    if response.data and hasattr(response.data, "list") and response.data.list:
        print(f"返回数据条数: {len(response.data.list)}")
        print(f"第一条数据: {response.data.list[0].name if response.data.list else '无'}")
    
    if response.data and hasattr(response.data, "page_info"):
        page_info = response.data.page_info
        print(f"分页信息: 第{page_info.page}页，每页{page_info.size}条，共{page_info.total_count}条")


if __name__ == "__main__":
    main()
