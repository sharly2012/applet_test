#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from utils.baseoperate import BaseOperate
from appium.webdriver.common.mobileby import By


class PageRepublicanHome(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_image = (By.ID, "首页焦点图")
    video_dynamic = (By.XPATH, "//*[@resource-id='最新动态']/android.view.View[1]")
    project_feature = (By.XPATH, "//*[@resource-id='精彩视角']/android.view.View[1]/android.view.View[3]")
    wonderful_life = (By.XPATH, "//*[@resource-id='精彩视角']/android.view.View[1]/android.view.View[2]")
    theme_activities = (By.XPATH, "//*[@resource-id='精彩视角']/android.view.View[1]/android.view.View[4]")
    value_analyze = (By.XPATH, "//*[@resource-id='了解项目']/android.view.View[1]/android.view.View[1]")
    lot_transportation = (By.XPATH, "//*[@resource-id='了解项目']/android.view.View[1]/android.view.View[3]")
    location_transportation = (By.XPATH,
                               "//*[@resource-id='zong-map']/android.view.View[1]/android.view.View[1]"
                               "/android.view.View[3]/android.view.View[1]")
    park_green = (By.XPATH, "//*[@resource-id='zong-map']/android.view.View[1]/android.view.View[1]"
                            "/android.view.View[3]/android.view.View[2]")
    shop = (By.XPATH,
            "//*[@resource-id='zong-map']/android.view.View[1]/android.view.View[1]"
            "/android.view.View[3]/android.view.View[3]")
    medical = (By.XPATH,
               "//*[@resource-id='zong-map']/android.view.View[1]/android.view.View[1]"
               "/android.view.View[3]/android.view.View[4]")
    hardcover_apartments = (By.XPATH, "//*[@resource-id='了解项目']/android.view.View[1]/android.view.View[4]")
    sample_room_images = (By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[3]")
    health_maintenance = (By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[2]")
    dining_entertainment = (By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[4]")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    ok_button = (By.XPATH, "//*[@text='好的']")

    def applet_back(self):
        self.logger.info("click the WeChat back button")
        x1 = int(50 / 1080 * self.width)
        y1 = int(150 / 1920 * self.height)
        self.tap(x1, y1)
        self.sleep(1)
