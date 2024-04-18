from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run()


# 默认监听在 localhost (127.0.0.1)上
# flask run
# 默认监听在 5000 端口
# flask run -h 0.0.0.0
# flask run -h 0.0.0.0 -p 8080
# 使用 1024 以下的端口需要 root 权限
# sudo flask run -h 0.0.0.0 -p 80
