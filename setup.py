import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dingchatbot",
    version="0.0.1",
    author="cjwcommuny",
    author_email="cjwcommuny@outlook.com",
    description="Dingding Chatbot API Wrapper",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cjwcommuny/DingdingChatbotAPIWrapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
