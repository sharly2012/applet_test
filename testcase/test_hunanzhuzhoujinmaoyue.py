#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import pytest
import allure
from utils.basedriver import BaseDriver
from pages.page_hunanzhuzhoujinmaoyue import PageHuNanZhuZhouJinMaoYue
from utils.basefile import make_folder
from utils.baseutil import BaseUtil


@allure.MASTER_HELPER.feature("湖南株洲金茂悦测试")
class TestHuNanZhuZhouJinMaoYue:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/湖南株洲金茂悦"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageHuNanZhuZhouJinMaoYue(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "湖南株洲金茂悦")
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(540 / 1080 * cls.ele_page.width),
                         int(286 / 1920 * cls.ele_page.height))
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(540 / 1080 * cls.ele_page.width),
                         int(286 / 1920 * cls.ele_page.height))
        cls.ele_page.sleep(8)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("首页")
    @allure.MASTER_HELPER.testcase("首页截图测试")
    def test_homepage(self):
        for i in range(3):
            self.ele_page.get_screenshot(self.result_images, "homepage")
            self.ele_page.wechat_swipe_up()
            self.ele_page.sleep(1)
        self.ele_page.go_to_top()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图1测试")
    def test_focus_images_01(self):
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu1", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图2测试")
    def test_focus_images_02(self):
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_left()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu2", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图3测试")
    def test_focus_images_03(self):
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu3", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("资讯")
    @allure.MASTER_HELPER.testcase("资讯测试")
    def test_information(self):
        self.ele_page.click(self.ele_page.information)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "zixun", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("户型鉴赏测试")
    def test_house_type(self):
        self.ele_page.click(self.ele_page.house_type)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxingliebiao")
        self.ele_page.click(self.ele_page.house_list_1)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "huxing_a")
        self.ele_page.click(self.ele_page.house_b)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "huxing_b")
        self.ele_page.click(self.ele_page.house_c)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "huxing_c")
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("楼盘参数测试")
    def test_property_parameters(self):
        self.ele_page.click(self.ele_page.property_parameters)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "loupancanshu", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("周边配套测试")
    def test_area_support(self):
        self.ele_page.click(self.ele_page.area_support)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "zhoubianpeitao")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("实景图测试")
    def test_really_images(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.really_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "shijingtu")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "shijingtu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("样板间图测试")
    def test_sample_room_images(self):
        self.ele_page.click(self.ele_page.sample_room_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("效果图测试")
    def test_effect_images(self):
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("相册切换")
    @allure.MASTER_HELPER.testcase("相册切换测试")
    def test_images_folders_switch(self):
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiangce1")
        self.ele_page.click(self.ele_page.images_folder_02)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiangce2")
        self.ele_page.click(self.ele_page.images_folder_03)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiangce3")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给好友")
    @allure.MASTER_HELPER.testcase("我要分享测试")
    def test_i_will_share(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.i_will_share)
        self.ele_page.sleep(2)
        self.ele_page.click(self.ele_page.recent_chat)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "woyaofenxiang")
        self.ele_page.click(self.ele_page.cancel_button)
        self.ele_page.sleep(2)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给好友")
    @allure.MASTER_HELPER.testcase("生成分享卡片测试")
    def test_create_share_card(self):
        self.ele_page.click(self.ele_page.create_share_card)
        self.ele_page.sleep(1)
        self.ele_page.tap(int(250 / 1080 * self.ele_page.width),
                          int(1700 / 1920 * self.ele_page.height))
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "shengchengfenxiangkapian")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给好友")
    @allure.MASTER_HELPER.testcase("我分享的好友测试")
    def test_share_friends(self):
        self.ele_page.click(self.ele_page.share_friends)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "wofenxiangdehaoyou")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("在线咨询")
    @allure.MASTER_HELPER.testcase("在线咨询测试")
    def test_chat_online(self):
        self.ele_page.click(self.ele_page.chat_online)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "zaixianzixun")
        self.ele_page.click_back()

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()


if __name__ == '__main__':
    pytest.main(["-s", "test_chengduwuhoujinmaofu.py"])
