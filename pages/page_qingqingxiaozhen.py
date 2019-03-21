#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from utils.baseoperate import BaseOperate
from appium.webdriver.common.mobileby import By


class GreenTown(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    applet_search = (950, 180)
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_images = (By.ID, "首页焦点图")
    holiday_town = (By.XPATH, "//*[@resource-id='运营位']/android.view.View[1]")
    overlook_town = (By.XPATH, "//*[@resource-id='小镇俯瞰视频']/android.view.View[1]")
    project_feature = (By.XPATH, "//*[@resource-id='精彩视角']/android.view.View[1]/android.view.View[2]")
    property_parameters = (By.XPATH, "//*[@resource-id='精彩视角']/android.view.View[1]/android.view.View[3]")
    real_time_imaging = (By.XPATH, "//*[@resource-id='精彩视角']/android.view.View[1]/android.view.View[4]")
    green_full_view = (By.ID, "view_1-1_8")
    investment_values = (By.XPATH, "//*[@resource-id='了解项目']/android.view.View[1]/android.view.View[1]")
    ancillary_facility = (By.XPATH, "//*[@resource-id='了解项目']/android.view.View[1]/android.view.View[3]")
    house_type = (By.XPATH, "//*[@resource-id='了解项目']/android.view.View[1]/android.view.View[4]")
    courtyard = (By.XPATH, "//*[@text='合院']")
    coupling_periphery_images = (By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[2]")
    sample_room_images = (By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[3]")
    project_really_image = (By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[4]")
    experience_youth_holi = (By.ID, "view_1-1_14")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    im = (By.ID, "在线咨询")

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
        x2 = int(size[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def focus_swipe_right(self, duration=1000):
        """swipe right"""
        self.logger.info("slide right the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.05)
        y1 = int(size[1] * 0.25)
        x2 = int(size[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)
