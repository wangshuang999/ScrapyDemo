# ScrapyDemo
Scrapy框架学习

Scrapy的数据流由执行引擎（Engine）控制，其基本过程如下：

    引擎从Spider中获取到初始Requests。
    引擎将该Requests放入调度器，并请求下一个要爬取的Requests。
    调度器返回下一个要爬取的Requests给引擎
    引擎将Requests通过下载器中间件转发给下载器(Downloader)。
    一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件(返回(response)方向)发送给引擎。
    引擎从下载器中接收到Response并通过Spider中间件(输入方向)发送给Spider处理。
    Spider处理Response并返回爬取到的Item及(跟进的)新的Request给引擎。
    引擎将(Spider返回的)爬取到的Item交给ItemPipeline处理，将(Spider返回的)Request交给调度器，并请求下一个Requests（如果存在的话）。
    (从第一步)重复直到调度器中没有更多地Request。


**爬虫框架**
    Scrapy
**数据解析**
    Xpath: 
        https://www.w3cschool.cn/xpath/
    CSS
    BeautifulSoup: 
        https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    正则表达：
        难以构造，可读性差，不适应网页更新的变化
**数据存储**
    .json
    
**可视化管理工具**
    scrapinghub： 
        https://scrapinghub.com/scrapy-cloud/        
        wangshuang*/wshshwhws*
    spiderkeeper:
        
        
        
**url去重**
    scrapy-deltafetch
    RFPDupeFilter
