# !/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from appium.webdriver.common.mobileby import By
from utils.baseoperate import BaseOperate


class PageHuNanZhuZhouJinMaoYue(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_images = (By.XPATH, "//*[@resource-id='焦点图模块']")
    information = (By.XPATH, "//*[@resource-id='滚动资讯']/android.view.View[1]")
    house_type = (By.XPATH, "//*[@resource-id='项目介绍模块']/android.view.View[1]/android.view.View[3]")
    house_list_1 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[1]/android.view.View[1]")
    house_a = (By.XPATH, "//*[@text='A户型']")
    house_b = (By.XPATH, "//*[@text='B户型']")
    house_c = (By.XPATH, "//*[@text='C户型']")
    property_parameters = (By.XPATH, "//*[@resource-id='项目介绍模块']/android.view.View[1]/android.view.View[2]")
    area_support = (By.XPATH, "//*[@resource-id='项目介绍模块']/android.view.View[1]/android.view.View[2]")
    really_images = (By.XPATH, "//*[@resource-id='精彩图片模块']/android.view.View[1]/android.view.View[3]")
    sample_room_images = (By.XPATH, "//*[@resource-id='精彩图片模块']/android.view.View[1]/android.view.View[2]")
    effect_images = (By.XPATH, "//*[@resource-id='精彩图片模块']/android.view.View[1]/android.view.View[4]")
    images_folder_01 = (By.XPATH, "//*[@text='可移动']/android.view.View[1]")
    images_folder_02 = (By.XPATH, "//*[@text='可移动']/android.view.View[2]")
    images_folder_03 = (By.XPATH, "//*[@text='可移动']/android.view.View[3]")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    confirm_button = (By.ID, "com.tencent.mm:id/az_")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    chat_online = (By.ID, "IM模块")

    def applet_back(self):
        self.logger.info("click the WeChat back button")
        x1 = int(50 / 1080 * self.width)
        y1 = int(150 / 1920 * self.height)
        self.tap(x1, y1)
        self.sleep(1)

    def focus_swipe_left(self, duration=1000):
        """focus swipe left"""
        self.logger.info("slide left the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.25)
        x2 = int(size[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def focus_swipe_right(self, duration=1000):
        """swipe right"""
        self.logger.info("slide right the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.25)
        y1 = int(size[1] * 0.25)
        x2 = int(size[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)
