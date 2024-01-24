### 安装需求

```bash
# 推荐python版本3.7+
# 推荐在conda或venv等虚拟环境中运行
pip install -r requirements.txt
```

### 安装Chrome

- 搜索官网下载安装即可

### 下载chromedriver

- 运行update.py
- 更新chrome浏览器后，再次运行update.py即可

### 填入信息

- 在config.py中填入账号、密码信息
- 可根据情况修改test列表，其中各项用于测试网络连通性

### 测试运行

- 注销网络
- 运行net.py，测试是否能连接

```python
# 本程序使用xpath定位登录页中元素
# 若遇到登录页改版，可使用普通浏览器，F12开发者工具，定位用户名输入框、密码输入框、登录按钮，将新的xpath复制入net.py即可
```

### 打包

```bash
# 推荐在conda或venv等虚拟环境中运行，否则可能导致打包过大。
# 推荐使用字母a开头的名称，若遇到问题，在任务管理器中可以轻松找到，并强制停止运行。
pyinstaller --name=anetwork anetwork.py -w -F # -i net.ico # （可选）定制图标
```

