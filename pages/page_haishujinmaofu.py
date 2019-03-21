#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from appium.webdriver.common.mobileby import By
from utils.baseoperate import BaseOperate


class PageHaiShuJinMaoFu(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_images = (By.ID, "焦点图")
    dynamic_information = (By.ID, "最新动态")
    house_type = (By.XPATH, "//*[@resource-id='项目介绍']/android.view.View[1]/android.view.View[3]")
    house_01 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[1]/android.view.View[1]")
    house_131 = (By.XPATH, "//*[@text='131㎡户型']")
    project_parameters = (By.XPATH, "//*[@resource-id='项目介绍']/android.view.View[1]/android.view.View[2]")
    area_supporting = (By.XPATH, "//*[@resource-id='项目介绍']/android.view.View[1]/android.view.View[4]")
    city_full_view = (By.XPATH, "//*[@resource-id='城市VR']/android.view.View[1]")
    demon_area_walking = (By.XPATH, "//*[@resource-id='示范区漫游']/android.view.View[1]")
    technology = (By.XPATH, "//*[@resource-id='府系科技']/android.view.View[1]")
    really_images = (
        By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[3]")
    sample_room_images = (
        By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[2]")
    effect_images = (
        By.XPATH, "//*[@resource-id='精彩图片']/android.view.View[1]/android.view.View[4]")
    image_folder_02 = (By.XPATH, "//*[@text='可移动']/android.view.View[2]")
    image_folder_03 = (By.XPATH, "//*[@text='可移动']/android.view.View[3]")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    confirm_button = (By.ID, "com.tencent.mm:id/az_")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    chat_online = (By.ID, "IM入口")

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
