#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import allure
import pytest
from utils.basedriver import BaseDriver
from pages.page_gonghejiayuan import PageRepublicanHome
from utils.basefile import make_folder
from utils.baseutil import BaseUtil


@allure.MASTER_HELPER.feature("恭和家园小程序测试")
class TestGongHeJiaYuan:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/恭和家园"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageRepublicanHome(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "恭和家园")
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
        for i in range(4):
            self.ele_page.get_screenshot(self.result_images, "homepage")
            self.ele_page.wechat_swipe_up()
            self.ele_page.sleep(1)
        self.ele_page.go_to_top()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图1测试")
    def test_focus_images_01(self):
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu1")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("focus_image")
    @allure.MASTER_HELPER.testcase("焦点图2测试")
    def test_focus_images_02(self):
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu2")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("focus_image")
    @allure.MASTER_HELPER.testcase("焦点图3测试")
    def test_focus_images_03(self):
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu3")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("动态视频")
    @allure.MASTER_HELPER.testcase("动态视频测试")
    def test_video_dynamic(self):
        self.ele_page.click(self.ele_page.video_dynamic)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "dongtaishipin")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩视角")
    @allure.MASTER_HELPER.testcase("项目特点测试")
    def test_project_feature(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.project_feature)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "xiangmutedian", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩视角")
    @allure.MASTER_HELPER.testcase("精彩生活测试")
    def test_wonderful_life(self):
        self.ele_page.click(self.ele_page.wonderful_life)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "jingcaishenghuo")
        self.ele_page.swipe_left(swipe_times=3)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "jingcaishenghuo")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩视角")
    @allure.MASTER_HELPER.testcase("主题活动测试")
    def test_theme_activities(self):
        self.ele_page.click(self.ele_page.theme_activities)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "zhutihuodong")
        self.ele_page.click_back()
        self.ele_page.sleep(1)
        self.ele_page.click_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("价值分析测试")
    def test_value_analyze(self):
        self.ele_page.click(self.ele_page.value_analyze)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiazhifenxi", 12)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("地段交通测试")
    def test_lot_transportation(self):
        self.ele_page.click(self.ele_page.lot_transportation)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "diduanjiaotong_01")
        self.ele_page.click(self.ele_page.park_green)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "diduanjiaotong_02")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("精装公寓测试")
    def test_hardcover_apartments(self):
        self.ele_page.click(self.ele_page.hardcover_apartments)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jingzhuanggongyu", 2)
        self.ele_page.tap(int(self.ele_page.width / 2), int(500 / 2244 * self.ele_page.height))
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "huxingtu")
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("样板间实景测试")
    def test_sample_room_images(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.sample_room_images)
        self.ele_page.sleep(3)
        self.ele_page.swipe_left(swipe_times=3)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("医疗养护测试")
    def test_health_maintenance(self):
        self.ele_page.click(self.ele_page.health_maintenance)
        self.ele_page.sleep(3)
        self.ele_page.swipe_left(swipe_times=5)
        self.ele_page.get_screenshot(self.result_images, "yiliaoyanghu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("餐饮娱乐测试")
    def test_dining_entertainment(self):
        self.ele_page.click(self.ele_page.dining_entertainment)
        self.ele_page.sleep(3)
        self.ele_page.swipe_left(swipe_times=8)
        self.ele_page.get_screenshot(self.result_images, "canyinyule")
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

    # @allure.MASTER_HELPER.severity("blocker")
    # @allure.MASTER_HELPER.story("在线留电")
    # @allure.MASTER_HELPER.testcase("同意在线留电测试")
    # def test_ok_button(self):
    #     self.ele_page.tap(int(845 / 1080 * self.ele_page.width),
    #                       int(1920 / 2244 * self.ele_page.height))
    #     self.ele_page.sleep(1)
    #     self.ele_page.get_screenshot(self.result_images, "zaixianliudian")

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()


if __name__ == '__main__':
    pytest.main(["-s", "test_gonghejiayuan.py"])
