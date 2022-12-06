# FEmailAll

EmailAll 的 Bug fixed 版本，主要修复了 phonebook、snov、veryvp 模块无法收集邮箱的bug。

## 说明

感谢作者，指路原项目 https://github.com/Taonn/EmailAll

挺好的一个收集邮箱的工具，但由于有些功能无法工作，原作者不再维护，觉得有些可惜，所以简单修补了一下。

如果想要验证邮箱的有效性可以尝试我的另一个项目 https://github.com/ccc-f/Femail

## 0x2 安装&使用

```bash
$ git clone https://github.com/ccc-f/FEmailAll.git
$ cd EmailAll
$ pip3 install -r requirements.txt
```

```python
EmailAll is a powerful Email Collect tool

Example:
    python3 emailall.py check
    python3 emailall.py --domain example.com run
    python3 emailall.py --domains ./domains.txt run
```

` python3 emailall.py --domain example.com run`

`python3 emailall.py --domains ./domains.txt run`

最终结果保存至`result`目录，分为不同模块json数据文件和汇总`{domain}_All.json` 和 `{domain}_All.txt` 文件。

## 模块

邮箱信息收集主要来源如下：

- Search
  - Ask                     # 需代理
  - Baidu                   # 反爬虫，无法正常使用
  - Bing                    # cn 版可以，国际版需代理
  - Google                  # 反爬虫，无法正常使用，加需代理
  - QWant                   # 正常
  - SO                      # 反爬虫，无法正常使用
  - Sougou                  # 反爬虫，无法正常使用
  - GithubApi               # 正常
- DataSets
  - Email-Format            # 正常
  - Skymem                  # 正常
  - Veryvp                  # 正常，已修复
  - PhoneBook               # 正常，已修复
  - Snov                    # 正常，已修复

## 配置

proxy配置在 setting.py文件

proxy={'http': '127.0.0.1:2333', 'https': '127.0.0.1:2333'}

API配置在 api.py文件

# http://www.veryvp.com/
veryvp_username = ''
veryvp_password = ''

# https://www.github.com
github_token = ''

# https://app.snov.io/
snov_username = ''
snov_password = ''

# https://phonebook.cz/
pb_url = 'https://2.intelx.io/phonebook/search'
pb_key = ''

- `veryvp`和`snov`去网站免费注册
- `GitHub`的token去设置里创建一个即可

phonebook 的 apikey 的获取方式更新了，先打开 https://phonebook.cz/ ，按提示注册登录，再返回原页面，按F12，搜索框搜索任意一个域名，可以在 Network 里面看到POST请求 	https://2.intelx.io/phonebook/search?k=xxx-xxx-xxx-xxx ， 把key放到配置文件里面的 pb_key 就可以了。

## 免责声明

​	本工具仅能在取得足够合法授权的企业安全建设中使用，在使用本工具过程中，您应确保自己所有行为符合当地的法律法规。 如您在使用本工具的过程中存在任何非法行为，您将自行承担所有后果，本工具所有开发者和所有贡献者不承担任何法律及连带责任。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。 您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
