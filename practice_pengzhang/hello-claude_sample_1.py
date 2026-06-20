# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "anthropic>=0.109.1",
#     "python-dotenv>=1.2.2",
# ]
# ///
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv() # 这将从 .env 文件加载环境变量，确保你已经在项目根目录下创建了 .env 文件，并在其中设置了 ANTHROPIC_API_KEY=你的密钥

client = Anthropic() # 这里会自动从环境变量中加载 API 密钥

query = "what's the temperature in Jinan today?"

msg = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": f"{query}"
        }
    ],

)

print(msg.content[0].text)

