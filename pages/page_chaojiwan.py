#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from appium.webdriver.common.mobileby import By
from utils.baseoperate import BaseOperate


class PageSuperBay(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_image = (By.ID, "焦点图")
    information = (By.XPATH, "//*[@resource-id='资讯']/android.view.View[1]")
    video_1 = (By.XPATH, "//*[@resource-id='view_1-1_3']")
    video_2 = (By.XPATH, "//*[@resource-id='view_1-4_4']/android.view.View[1]")
    vr = (By.XPATH, "//*[@resource-id='view_1-4_4']/android.view.View[2]")
    full_view = (By.XPATH, "//*[@resource-id='view_1-4_4']/android.view.View[3]")
    visit_xiamen = (By.XPATH, "//*[@resource-id='view_2-4_6']/android.view.View[1]")
    super_life = (By.XPATH, "//*[@resource-id='view_2-4_6']/android.view.View[3]")
    own_xiamen = (By.XPATH, "//*[@resource-id='view_2-4_6']/android.view.View[4]")
    island_sea = (By.XPATH, "//*[@resource-id='view_1-1_9']")
    house_01 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[2]/android.view.View[1]")
    house_list_01 = (By.XPATH, "//*[@text='岛屿海']")
    house_a3 = (By.XPATH, "//*[@text='高层-A3户型']")
    house_a4 = (By.XPATH, "//*[@text='高层-A4户型']")
    cloud_sea = (By.XPATH, "//*[@resource-id='view_1-1_10']")
    house_list_02 = (By.XPATH, "//*[@text='山屿海']")
    house_02 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[2]/android.view.View[1]")
    house_002 = (By.XPATH, "//*[@text='观海居-2户型']")
    house_003 = (By.XPATH, "//*[@text='观澜居']")
    mountain_sea = (By.XPATH, "//*[@resource-id='view_1-1_11']")
    house_list_03 = (By.XPATH, "//*[@text='望云海']")
    house_03 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[2]/android.view.View[1]")
    house_0002 = (By.XPATH, "//*[@text='高层-2户型']")
    house_0003 = (By.XPATH, "//*[@text='高层-3户型']")
    sample_room_images = (By.XPATH, "//*[@resource-id='view_1-3_14']/android.view.View[1]")
    area_support_images = (By.XPATH, "//*[@resource-id='view_1-3_14']/android.view.View[2]")
    really_images = (By.XPATH, "//*[@resource-id='view_1-3_14']/android.view.View[3]")
    effect_images = (By.XPATH, "//*[@resource-id='view_1-3_14']/android.view.View[4]")
    image_folder_01 = (By.XPATH, "//*[@text='可移动']/android.view.View[1]")
    image_folder_02 = (By.XPATH, "//*[@text='可移动']/android.view.View[2]")
    image_folder_03 = (By.XPATH, "//*[@text='可移动']/android.view.View[3]")
    image_folder_04 = (By.XPATH, "//*[@text='可移动']/android.view.View[4]")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    chat_online = (By.ID, "IM")

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
