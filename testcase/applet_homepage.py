#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-


import time
from appium import webdriver
from utils.baseoperate import BaseOperate
from pages.page_chengduwuhoujinmaofu import PageChengDuWuHouJinMaoFu

desired_caps = {
    'platformName': "Android",
    'platformVersion': "8.1.0",
    'deviceName': "CLB0219116000104",
    'appPackage': "com.tencent.mm",
    'appActivity': ".ui.LauncherUI",
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
base_operate = BaseOperate(driver)
base_operate.sleep(8)
ele_page = PageChengDuWuHouJinMaoFu(driver)
m, n = base_operate.get_screen_size()
print(m, n)
driver.find_element_by_xpath(
    "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]").click()
base_operate.sleep(2)
base_operate.swipe_up()
driver.find_element_by_xpath("//*[@text='小程序']").click()
base_operate.sleep(2)
base_operate.tap(int(995 / 1080 * base_operate.width), int(145 / 1920 * base_operate.height))
time.sleep(3)
driver.find_element_by_xpath("//*[@text='搜索小程序']").click()
driver.find_element_by_xpath("//*[@text='搜索小程序']").send_keys("成都武侯金茂府")
time.sleep(2)
base_operate.tap(int(540 / 1080 * base_operate.width), int(286 / 1920 * base_operate.height))
time.sleep(5)
base_operate.tap(int(540 / 1080 * base_operate.width), int(286 / 1920 * base_operate.height))
time.sleep(10)
image_path = "E:/PycharmProjects/wechat_test/template/成都武侯金茂府"
focus_image = base_operate.find_element(*ele_page.focus_images)
house_type = base_operate.find_element(*ele_page.house_type)
base_operate.get_screenshot_by_element(house_type, image_path, "huxingjianshang")
project_parameters = base_operate.find_element(*ele_page.project_parameters)
base_operate.get_screenshot_by_element(project_parameters, image_path, "loupancanshu")
area_supporting = base_operate.find_element(*ele_page.area_supporting)
base_operate.get_screenshot_by_element(area_supporting, image_path, "zhoubianpeitao")
base_operate.wechat_swipe_up()
technology = base_operate.find_element(*ele_page.technology)
base_operate.get_screenshot_by_element(technology, image_path, "fuxikeji")
sample_room_images = base_operate.find_element(*ele_page.sample_room_images)
base_operate.get_screenshot_by_element(sample_room_images, image_path, "yangbanjiantu")
really_images = base_operate.find_element(*ele_page.really_images)
base_operate.get_screenshot_by_element(really_images, image_path, "shijingtu")
effect_images = base_operate.find_element(*ele_page.effect_images)
base_operate.get_screenshot_by_element(effect_images, image_path, "xiaoguotu")
base_operate.wechat_swipe_up()
interview = base_operate.find_element(*ele_page.interview)
base_operate.get_screenshot_by_element(interview, image_path, "renwucaifang")
time.sleep(5)
driver.close_app()
driver.find_element_by_xpath().tag_name