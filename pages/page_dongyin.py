# !/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

from appium.webdriver.common.mobileby import By
from utils.baseoperate import BaseOperate


class PageDongYin(BaseOperate):
    discovery = (By.XPATH,
                 "//*[@resource-id='com.tencent.mm:id/bq']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    applet = (By.XPATH, "//*[@text='小程序']")
    search_applet = (By.XPATH, "//*[@text='搜索小程序']")
    focus_images = (By.ID, "焦点图")
    project_overview = (By.ID, "项目概况1级")
    gold_area = (By.XPATH, "//*[@resource-id='地段介绍1级']/android.view.View[1]")
    house_effect_images = (By.ID, "uinitA效果图")
    house_introduce = (By.XPATH, "//*[@resource-id='户型区域']/android.view.View[1]/android.view.View[1]")
    house_list_01 = (By.XPATH, "//*[@text='可滚动']/android.view.View[1]/android.view.View[1]/android.view.View[1]")
    administrative_mansion = (By.XPATH, "//*[@text='顶级行政官邸']")
    personal_mansion = (By.XPATH, "//*[@text='顶级私人华宅']")
    property_parameters = (By.XPATH, "//*[@resource-id='户型区域']/android.view.View[1]/android.view.View[2]")
    delivery_standards = (By.XPATH, "//*[@resource-id='户型区域']/android.view.View[1]/android.view.View[3]")
    view_3D = (By.XPATH, "//*[@resource-id='view_1-1_8']")
    decoration_style = (By.XPATH, "//*[@resource-id='view_1-1_9']")
    images_folder_01 = (By.XPATH, "//*[@text='可移动']/android.view.View[1]")
    images_folder_02 = (By.XPATH, "//*[@text='可移动']/android.view.View[2]")
    images_folder_03 = (By.XPATH, "//*[@text='可移动']/android.view.View[3]")
    images_folder_04 = (By.XPATH, "//*[@text='可移动']/android.view.View[4]")
    carousel_area = (By.XPATH, "//*[@resource-id='轮播区域']/android.view.View[1]")
    multiple_images_area = (By.XPATH, "//*[@resource-id='多图区域']/android.view.View[1]")
    investment_left = (By.XPATH, "//*[@text='投资向左']")
    investment_value = (By.XPATH, "//*[@resource-id='view_3-5_15']/android.view.View[2]/android.widget.ListView[1]"
                                  "/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]")
    property_service = (By.XPATH, "//*[@resource-id='view_3-5_15']/android.view.View[2]/android.widget.ListView[1]"
                                  "/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]")
    purchase_process = (By.XPATH, "//*[@resource-id='view_3-5_15']/android.view.View[2]/android.widget.ListView[1]"
                                  "/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]")
    safe_custody = (By.XPATH, "//*[@resource-id='view_3-5_15']/android.view.View[2]/android.widget.ListView[1]"
                              "/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]")
    immigrant_right = (By.XPATH, "//*[@text='移民向右']")
    immigrant_status = (By.XPATH, "//*[@resource-id='view_3-5_15']/android.view.View[2]/android.widget.ListView[1]"
                                  "/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]")
    immigrant_policy = (By.XPATH, "//*[@resource-id='view_3-5_15']/android.view.View[2]/android.widget.ListView[1]"
                                  "/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[3]")
    property_service_2 = (By.XPATH, "//*[@resource-id='view_3-5_15']/android.view.View[2]/android.widget.ListView[1]"
                                    "/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]")
    housing_services = (By.XPATH, "//*[@resource-id='view_3-5_15']/android.view.View[2]/android.widget.ListView[1]"
                                  "/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[4]")
    developers_introduce = (By.ID, "开发商介绍1级")
    i_will_share = (By.XPATH, "//*[@text='我要分享']")
    recent_chat = (By.XPATH, "//*[@resource-id='com.tencent.mm:id/i9']/android.widget.RelativeLayout[2]")
    cancel_button = (By.ID, "com.tencent.mm:id/az9")
    confirm_button = (By.ID, "com.tencent.mm:id/az_")
    create_share_card = (By.XPATH, "//*[@text='生成分享卡片']")
    share_friends = (By.XPATH, "//*[@text='我分享的好友']")
    chat_online = (By.ID, "咨询")

    def applet_back(self):
        self.logger.info("click the WeChat back button")
        x1 = int(50 / 1080 * self.width)
        y1 = int(150 / 1920 * self.height)
        self.tap(x1, y1)
        self.sleep(1)

    def carousel_area_left(self, duration=1000):
        self.logger.info("carousel_area swipe left")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.80)
        x2 = int(size[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def carousel_area_right(self, duration=1000):
        self.logger.info("carousel_area swipe right")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.25)
        y1 = int(size[1] * 0.80)
        x2 = int(size[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def multiple_images_left(self, duration=1000):
        self.logger.info("carousel_area swipe left")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.60)
        x2 = int(size[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def multiple_images_right(self, duration=1000):
        self.logger.info("carousel_area swipe right")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.25)
        y1 = int(size[1] * 0.60)
        x2 = int(size[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)
