#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import os
import sys
import pytest
import time

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from utils.baseutil import BaseUtil
from utils.shell import Shell
from utils.logger import Logger

logger = Logger(logger="run").get_log()

if __name__ == '__main__':
    # # 打开appium
    # Shell.invoke("appium -a 127.0.0.1 -p 4723")
    # time.sleep(5)
    # 获取report的路径
    xml_report_path = BaseUtil().get_yaml_value("EnvironmentInfo", "xml_report")
    html_report_path = BaseUtil().get_yaml_value("EnvironmentInfo", "html_report")
    # 开始执行测试
    args = ['-s', '-q', '--alluredir', xml_report_path]
    self_args = sys.argv[1:]
    pytest.main(args + self_args)
    # 生成html测试报告
    cmd = 'allure generate %s -o %s  --clean' % (xml_report_path, html_report_path)
    try:
        Shell.invoke(cmd)
        logger.info("Html测试报告生成成功")
    except Exception as e:
        logger.error("Html测试报告生成失败,确保已经安装了Allure-Commandline % s" % e)
