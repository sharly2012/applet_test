#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from utils.baseoperate import BaseOperate
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction


class WIIIPages(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_images = (By.XPATH, "//*[@resource-id='首页焦点图']/android.view.View[1]")
    information = (By.XPATH, "//*[@resource-id='最新动态']/android.view.View[1]")
    surround_supporting = (By.ID, "view_1-1_3")
    cloud_life = (By.ID, "view_1-1_4")
    full_view_vr = (By.XPATH, "//*[@text='全域VR']")
    house_type = (By.ID, "view_1-1_5")
    sell_carousel = (By.ID, "卖点轮播")
    video_house = (By.XPATH,
                   "//*[@resource-id='view_3-5_7']/android.view.View[2]/android.widget.ListView[1]"
                   "/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]")
    effect_images = (By.XPATH,
                     "//*[@resource-id='view_3-5_7']/android.view.View[2]/android.widget.ListView[1]"
                     "/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]")
    really_images = (By.XPATH,
                     "//*[@resource-id='view_3-5_7']/android.view.View[2]/android.widget.ListView[1]"
                     "/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]")
    investment_focus = (By.XPATH,
                        "//*[@resource-id='view_3-5_7']/android.view.View[2]/android.widget.ListView[1]"
                        "/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]")
    investment_return = (By.XPATH,
                         "//*[@resource-id='view_3-5_7']/android.view.View[2]/android.widget.ListView[1]"
                         "/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[3]")
    investment_guarantee = (By.XPATH,
                            "//*[@resource-id='view_3-5_7']/android.view.View[2]/android.widget.ListView[1]"
                            "/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[4]")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    chat_online = (By.ID, "IM入口")
    ok_button = (By.XPATH, "//*[@text='好的']")

    def applet_back(self):
        x1 = int(50 / 1080 * self.width)
        y1 = int(150 / 1920 * self.height)
        self.tap(x1, y1)
        self.sleep(1)

    def carousel_swipe_left(self):
        """carousel swipe left"""
        self.logger.info("carousel slide left ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.4)
        x2 = int(size[0] * 0.25)
        action = TouchAction(self.driver)
        action.press(x=x1, y=y1).wait(800).move_to(x=x2, y=y1).wait(800).release()
        action.perform()

    def carousel_swipe_right(self):
        """carousel swipe right"""
        self.logger.info("carousel slide right ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.25)
        y1 = int(size[1] * 0.4)
        x2 = int(size[0] * 0.75)
        action = TouchAction(self.driver)
        action.press(x=x1, y=y1).wait(800).move_to(x=x2, y=y1).wait(800).release()
        action.perform()
