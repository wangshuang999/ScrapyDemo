# -*- coding=utf8 -*-
import os
import random
import threading

import re
from scrapy import cmdline

# cmdline.execute("scrapy crawl douyu".split())

# cmdline.execute([
# 	'scrapy',
# 	'crawl',
# 	'itcast'])


# os.system('scrapy crawl douyu')



import schedule
import time
import subprocess


def job():
    print("I'm working...",time.strftime('%H%M%S', time.localtime()))
    subprocess.Popen('scrapy crawl itcast', shell=True if os.name == 'posix' else False)
    subprocess.Popen('scrapy crawl douyu', shell=True if os.name == 'posix' else False)

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)


