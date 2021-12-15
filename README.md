# DingdingChatbotAPIWrapper

## Installation

```shell
pip install .
```

## Usage

```python
from dingchatbot import send_markdown

title = 'Hello!'
markdown = """
# Hello

**[info]**: this is info
"""

secret: str = 'XXXX'
access_token: str = 'YYYY'
#
send_markdown(secret, access_token)(title, markdown)
```

![example](assets/example.png)

