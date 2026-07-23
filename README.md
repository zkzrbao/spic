# 一：项目配置

1.设置环境变量APP_ENV，可选值为prod/dev，如果不设置默认为dev

2.启动命令：nohup bash -c "source .venv/bin/activate && python run.py" > crawler.log 2>&1 &

# 二：配置密钥环境变量

重新创建容器，加环境变量：

docker run -d --name spic-ai-container -e SYS_PARAM=6650a9fbe517bf1fb11e7185ec0c2c25 --dns 10.104.39.207 --privileged=true -p 8191:8190 -v ./:/app spic-ai:amd64-latest tail -f /dev/null

## 测试

```
import os
print(os.getenv("SYS_PARAM"))
```

或者在agent_os中执行python tt.py

# 三：打包

uv export --format requirements-txt -o requirements.txt
