import re

from setuptools import setup

with open("src/flask/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask",
    version=version,
    install_requires=[
        "Werkzeug>=0.15",       # WSGI规范的实用函数库
        "Jinja2>=2.10.1",       # 模板引擎
        "itsdangerous>=0.24",   # 生成临时身份令牌
        "click>=5.1",           # 轻松将一个函数变成一个命令行工具
    ],
    extras_require={"dotenv": ["python-dotenv"]},
)
