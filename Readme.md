# 博客园爬虫，边学边做

## 参考

[官方文档](https://docs.scrapy.org/en/latest/intro/tutorial.html#creating-a-project)

## 安装

### 安装scrapy

直接`pip install scrapy`安装就行了，不过完后，我的电脑报错:
```bash
AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1
```
网上查了一下原因，[说是因为twisted版本不对](https://stackoverflow.com/questions/42731760/attributeerror-module-object-has-no-attribute-op-no-tlsv1-1)，我本地是17.xx，于是重新安装一下即可:
```bash
sudo pip install twisted==13.1.0
```

### 创建工程

```bash
> scrapy startproject CNBlogsScrapy

New Scrapy project 'CNBlogsScrapy', using template directory '/Library/Python/2.7/site-packages/scrapy/templates/project', created in:
    /Users/xingoo/PycharmProjects/CNBlogsScrapy

You can start your first spider with:
    cd CNBlogsScrapy
    scrapy genspider example example.com
```
这样就创建成功了一个spider工程，然后按照提示，生成默认的spdier类:
```bash
> scrapy genspider cnblogsSpider https://www.cnblogs.com/
Created spider 'cnblogsSpider' using template 'basic' in module:
  CNBlogsScrapy.spiders.cnblogsSpider
```

### 爬取想要的内容

输入命令
```bash
> scrapy shell 'http://www.cnblogs.com'
```
进入shell调试，比如
```bash
response.xpath('//div[@class="post_item"]/div[@class="post_item_body"]/h3/a/text()').extract()
```
能够获得首页文章的标题。