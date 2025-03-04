"""
测试禅境HTTP客户端
"""

import pytest
import responses
import json
from unittest.mock import patch, MagicMock
from chanjing.core import ChanjingHttpClient
from chanjing.schemas import APIResponse, ResponseData, PageInfo


@pytest.fixture
def client():
    """创建测试客户端"""
    return ChanjingHttpClient(api_key="test_api_key")


@pytest.fixture
def mock_response_data():
    """创建模拟响应数据"""
    return {
        "trace_id": "test-trace-id",
        "code": 0,
        "msg": "success",
        "data": {
            "list": [],
            "page_info": {
                "page": 1,
                "size": 10,
                "total_count": 0,
                "total_page": 0
            }
        }
    }


@responses.activate
def test_request_get(client, mock_response_data):
    """测试GET请求"""
    # 设置模拟响应
    responses.add(
        responses.GET,
        "https://www.chanjing.cc/api/open/v1/test/endpoint",
        json=mock_response_data,
        status=200
    )
    
    # 发送请求
    response = client.request("GET", "test/endpoint")
    
    # 验证响应
    assert isinstance(response, APIResponse)
    assert response.trace_id == "test-trace-id"
    assert response.code == 0
    assert response.msg == "success"
    assert isinstance(response.data, ResponseData)
    assert isinstance(response.data.page_info, PageInfo)


@responses.activate
def test_request_post(client, mock_response_data):
    """测试POST请求"""
    # 设置模拟响应
    responses.add(
        responses.POST,
        "https://www.chanjing.cc/api/open/v1/test/endpoint",
        json=mock_response_data,
        status=200
    )
    
    # 发送请求
    data = {"key": "value"}
    response = client.request("POST", "test/endpoint", json=data)
    
    # 验证响应
    assert isinstance(response, APIResponse)
    assert response.trace_id == "test-trace-id"
    assert response.code == 0
    assert response.msg == "success"


@responses.activate
def test_request_error_status_code(client):
    """测试HTTP错误状态码"""
    # 设置模拟响应
    responses.add(
        responses.GET,
        "https://www.chanjing.cc/api/open/v1/test/endpoint",
        json={"error": "Internal Server Error"},
        status=500
    )
    
    # 验证异常
    with pytest.raises(Exception) as excinfo:
        client.request("GET", "test/endpoint")
    
    assert "500" in str(excinfo.value)


@responses.activate
def test_request_invalid_json(client):
    """测试无效的JSON响应"""
    # 设置模拟响应
    responses.add(
        responses.GET,
        "https://www.chanjing.cc/api/open/v1/test/endpoint",
        body="Invalid JSON",
        status=200
    )
    
    # 验证异常
    with pytest.raises(ValueError) as excinfo:
        client.request("GET", "test/endpoint")
    
    assert "无效的JSON响应" in str(excinfo.value)


def test_request_invalid_method(client):
    """测试无效的HTTP方法"""
    with pytest.raises(ValueError) as excinfo:
        client.request("INVALID", "test/endpoint")
    
    assert "不支持的HTTP方法" in str(excinfo.value)


@patch("requests.Session.request")
def test_request_connection_error(mock_request, client):
    """测试连接错误"""
    # 模拟连接错误
    mock_request.side_effect = requests.exceptions.ConnectionError("连接被拒绝")
    
    # 验证异常
    with pytest.raises(ConnectionError) as excinfo:
        client.request("GET", "test/endpoint")
    
    assert "无法连接到禅境API" in str(excinfo.value)


@patch("requests.Session.request")
def test_request_timeout(mock_request, client):
    """测试请求超时"""
    # 模拟超时
    mock_request.side_effect = requests.exceptions.Timeout("请求超时")
    
    # 验证异常
    with pytest.raises(TimeoutError) as excinfo:
        client.request("GET", "test/endpoint")
    
    assert "禅境API请求超时" in str(excinfo.value)


@responses.activate
def test_request_api_error(client):
    """测试API错误码"""
    # 设置模拟响应
    error_response = {
        "trace_id": "test-trace-id",
        "code": 1001,
        "msg": "Invalid parameter",
        "data": {
            "list": [],
            "page_info": {
                "page": 1,
                "size": 10,
                "total_count": 0,
                "total_page": 0
            }
        }
    }
    
    responses.add(
        responses.GET,
        "https://www.chanjing.cc/api/open/v1/test/endpoint",
        json=error_response,
        status=200
    )
    
    # 发送请求
    with patch("logging.Logger.warning") as mock_warning:
        response = client.request("GET", "test/endpoint")
    
    # 验证响应
    assert response.code == 1001
    assert response.msg == "Invalid parameter"
    
    # 验证警告日志
    mock_warning.assert_called_once()
    assert "API错误" in mock_warning.call_args[0][0]
