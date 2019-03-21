#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from appium.webdriver.common.mobileby import By
from utils.baseoperate import BaseOperate


class PageSUNACWonderfulWorld(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_image = (By.XPATH, "//*[@resource-id='焦点图']/android.view.View[1]")
    FTA_build = (By.XPATH, "//*[@resource-id='view_1-2_1']/android.view.View[1]")
    policy_interpretation = (By.XPATH, "//*[@resource-id='view_1-2_1']/android.view.View[1]")
    information = (By.ID, "view_1-1_2")
    area_translation = (By.XPATH, "//*[@resource-id='区域交通']/android.view.View[1]")
    full_view = (By.XPATH, "//*[@resource-id='项目实景']/android.view.View[1]/android.view.View[1]")
    house_type = (By.XPATH, "//*[@resource-id='项目实景']/android.view.View[1]/android.view.View[4]")
    house_1 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[1]/android.view.View[1]")
    house_d = (By.XPATH, "//*[@text='D户型']")
    style_club = (By.XPATH, "view_1-1_6")
    SUNAC_brand = (By.XPATH, "//*[@resource-id='项目介绍']/android.view.View[1]/android.view.View[3]")
    SUNAC_property = (By.XPATH, "//*[@resource-id='项目介绍']/android.view.View[1]/android.view.View[2]")
    double_hosting = (By.XPATH, "//*[@resource-id='项目介绍']/android.view.View[1]/android.view.View[4]")
    SUNAC_tenant = (By.ID, "view_1-1_9")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    IM = (By.ID, "留电")

    def applet_back(self):
        self.logger.info("click the WeChat back button")
        x1 = int(50 / 1080 * self.width)
        y1 = int(150 / 1920 * self.height)
        self.tap(x1, y1)
        self.sleep(1)
