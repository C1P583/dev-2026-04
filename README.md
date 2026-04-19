**DeepSeek终端流式对话作业**

**项目功能**

实现命令行与DeepSeek模型的流式交互，支持多轮对话、输入指令退出程序。

**环境准备**

&#x20;1. 已通过  python -m venv .venv  创建虚拟环境并激活

&#x20;2. 安装依赖： pip install openai python-dotenv 

**运行步骤**

&#x20;1. 在项目根目录创建  .env  文件，写入  DEEPSEEK\_API\_KEY=

&#x20;2. 运行  python main.py  启动对话

&#x20;3. 输入问题获取流式回复，输入  quit / q / exit  退出

**功能说明**

&#x20;从环境变量读取API密钥，未硬编码敏感信息

&#x20;支持流式输出，回复逐字显示

&#x20;实现正常退出逻辑

