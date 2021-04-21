# boss直聘生物信息职位爬虫

## 安装

由于boss直聘反爬做得很好，使用scrapy+selenium进行爬虫，
第一步需要安装selenium驱动程序。

### 1. 安装selenium驱动程序

可以参考[文档](https://www.selenium.dev/)完成相应浏览器驱动程序的安装。

### 2. 安装Python包依赖

```shell script
pip install -r requirements.txt
```

## 运行

start_crawl.py为爬虫启动脚本，参数如下：

```shell script
Usage: start_crawl.py [OPTIONS]

Options:
  -c, --city TEXT         城市ID  [default: 101010100]
  -d, --driver-name TEXT  驱动名称  [default: chrome]
  -p, --driver-path TEXT  驱动路径  [default: /usr/local/bin/chromedriver]
  -p, --proxy TEXT        代理地址  [default: http://127.0.0.1:6152]
  -o, --outfile TEXT      输出文件（json格式）  [default: bossxr.json]
  --help                  Show this message and exit.
```

1. -c参数指定城市ID，城市ID需要在boss直聘网站上获取（在URL上有体现），
   例如，默认为北京市，即101010100
2. -d参数指定驱动名称，具体可以参考selenium的文档，例如，chrome浏览器
   驱动的名称为chrome，默认为chrome
3. --driver-path参数指定驱动的可执行文件路径，默认为/usr/local/bin/chromedriver
4. --proxy参数指定代理地址，由于boss直聘反爬比较厉害，这里必须指定代理地址，
   默认的代理地址为http://127.0.0.1:6152
5. -o参数指定保存路径，默认为bossxr.json，jsonlines格式（即每行一个json）
