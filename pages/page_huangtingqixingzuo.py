# !/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from appium.webdriver.common.mobileby import By
from utils.baseoperate import BaseOperate


class PageHuangTingQiXingZuo(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    video = (By.XPATH, "//*[@resource-id='视频']/android.view.View[1]")
    scrolling_information = (By.XPATH, "//*[@resource-id='view_3-1_6']")
    tianshuzuo = (By.XPATH, "//*[@resource-id='天枢座']")
    yaoguangzuo = (By.XPATH, "//*[@resource-id='瑶光座']")
    tianjizuo = (By.XPATH, "//*[@resource-id='天机座']")
    tianxuanzuo = (By.XPATH, "//*[@resource-id='天璇座']")
    tianquanzuo = (By.XPATH, "//*[@resource-id='view_1-1_13']")
    yuhengzuo = (By.XPATH, "//*[@resource-id='玉衡座']")
    kaiyangzuo = (By.XPATH, "//*[@resource-id='开阳座']")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    confirm_button = (By.ID, "com.tencent.mm:id/az_")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    chat_online = (By.ID, "IM")

    def applet_back(self):
        self.logger.info("click the WeChat back button")
        x1 = int(50 / 1080 * self.width)
        y1 = int(150 / 1920 * self.height)
        self.tap(x1, y1)
        self.sleep(1)

    def carousel_swipe_left(self, duration=1000):
        """focus swipe left"""
        self.logger.info("slide left the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.36)
        x2 = int(size[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def carousel_swipe_right(self, duration=1000):
        """swipe right"""
        self.logger.info("slide right the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.25)
        y1 = int(size[1] * 0.36)
        x2 = int(size[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)
