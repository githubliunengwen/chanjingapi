# Chanjing API Client

一个用于与禅境API交互的Python客户端库。

## 功能特点

- 提供与禅境API的简单集成
- 健壮的错误处理和日志记录
- 类型提示支持
- 详细的文档和示例
- 完整的测试覆盖

## 安装

使用pip安装：

```bash
pip install chanjing
```

或者使用uv安装（推荐）：

```bash
uv pip install chanjing
```

## 使用方法

### 基本用法

```python
from chanjing import ChanjingHttpClient
from chanjing.schemas import APIResponse

# 初始化客户端
client = ChanjingHttpClient(api_key="your_api_key_here")

# 发送GET请求
response = client.request("GET", "endpoint/path")

# 发送POST请求
data = {"key": "value"}
response = client.request("POST", "endpoint/path", json=data)

# 处理响应
print(f"响应代码: {response.code}")
print(f"响应消息: {response.msg}")
print(f"追踪ID: {response.trace_id}")
print(f"响应数据: {response.data}")
```

### 错误处理

```python
from chanjing import ChanjingHttpClient

client = ChanjingHttpClient(api_key="your_api_key_here")

try:
    response = client.request("GET", "endpoint/path")
    # 处理成功响应
except ValueError as e:
    # 处理参数错误
    print(f"参数错误: {str(e)}")
except ConnectionError as e:
    # 处理连接错误
    print(f"连接错误: {str(e)}")
except TimeoutError as e:
    # 处理超时错误
    print(f"请求超时: {str(e)}")
except Exception as e:
    # 处理其他错误
    print(f"请求失败: {str(e)}")
```

## 开发

### 环境设置

1. 克隆仓库
2. 创建并激活虚拟环境
3. 安装开发依赖

```bash
git clone https://github.com/yourusername/chanjing.git
cd chanjing
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
uv pip install -e ".[dev]"
```

### 运行测试

```bash
pytest
```

## 结构性变更

### 2025-03-04
- 实现了`ChanjingHttpClient.request`方法，提供了与禅境API的HTTP交互功能
- 添加了健壮的错误处理和日志记录
- 添加了请求和响应的类型提示

## 项目结构

```markdown
chanjing/
├── app/                      # 主应用目录
│   ├── module1/                 # 模块1
│   │   ├── __init__.py
│   │   ├── schema.py         # 模型
│   │   ├── utils.py          # 工具函数
├── tests/                     # 测试目录
│   ├── test_module1.py
│   └── __init__.py
├── docs/                      # 文档目录
│   ├── __init__.py
│   └── index.md              # 主页
└── examples/                  # 示例目录
    ├── __init__.py
    └── example1.py           # 示例1
```

## 许可证

MIT
