#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from appium.webdriver.common.mobileby import By
from utils.baseoperate import BaseOperate


class PageSUNACMissionHills(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_images = (By.XPATH, "//*[@resource-id='首页焦点图']/android.view.View[1]")
    information = (By.XPATH, "//*[@resource-id='最新动态']/android.view.View[1]")
    HaiNan_holiday = (By.XPATH, "//*[@resource-id='海南度假攻略']/android.view.View[1]")
    MissionHills_time = (By.XPATH, "//*[@resource-id='悦享观澜时光']/android.view.View[1]")
    project_introduce = (By.XPATH, "//*[@resource-id='view_1-3_6']/android.view.View[1]")
    house_type = (By.XPATH, "//*[@resource-id='view_1-3_6']/android.view.View[3]")
    house_01 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[1]/android.view.View[1]")
    house_02 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[1]/android.view.View[2]")
    house_03 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[1]/android.view.View[3]")
    house_b = (By.XPATH, "//*[@text='可移动']/android.view.View[2]")
    house_c = (By.XPATH, "//*[@text='可移动']/android.view.View[3]")
    area_park = (By.XPATH, "//*[@resource-id='view_1-3_6']/android.view.View[2]")
    full_supporting = (By.XPATH, "//*[@resource-id='view_1-3_6']/android.view.View[4]")
    really_images_sample = (By.XPATH, "//*[@resource-id='view_1-2_7']/android.view.View[1]")
    really_images_button = (By.XPATH, "//*[@text='实景图']")
    hardcover_configuration = (By.XPATH, "//*[@resource-id='view_1-2_7']/android.view.View[2]")
    full_view_life = (By.XPATH, "//*[@resource-id='720°全景生活馆']/android.view.View[1]")
    SUNAC_brand = (By.XPATH, "//*[@resource-id='融创品牌']/android.view.View[1]")
    SUNAC_heart_enjoy = (By.XPATH, "//*[@resource-id='融创心享']/android.view.View[1]")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    IM = (By.ID, "在线留电")

    def applet_back(self):
        self.logger.info("click the WeChat back button")
        x1 = int(50 / 1080 * self.width)
        y1 = int(150 / 1920 * self.height)
        self.tap(x1, y1)
        self.sleep(1)
