#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import pytest
import allure
from utils.basedriver import BaseDriver
from pages.page_huangtingqixingzuo import PageHuangTingQiXingZuo
from utils.basefile import make_folder
from utils.baseutil import BaseUtil


@allure.MASTER_HELPER.feature("皇廷七星座")
class TestHuangTingQiXingZuo:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/皇廷七星座"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageHuangTingQiXingZuo(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "皇廷七星座")
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
        for i in range(11):
            self.ele_page.get_screenshot(self.result_images, "homepage")
            self.ele_page.wechat_swipe_up()
            self.ele_page.sleep(1)
        self.ele_page.go_to_top(12)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("视频")
    @allure.MASTER_HELPER.testcase("视频")
    def test_video(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.video)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "shipin")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("向上滑动")
    @allure.MASTER_HELPER.testcase("向上滑动")
    def test_scrolling(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "2")
        self.ele_page.wechat_swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "3")
        self.ele_page.wechat_swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "4")
        self.ele_page.wechat_swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "5")
        self.ele_page.wechat_swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "6")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("教育资源")
    @allure.MASTER_HELPER.testcase("喇沙书院")
    def test_education_01(self):
        self.ele_page.carousel_swipe_right()
        self.ele_page.carousel_swipe_right()
        self.ele_page.carousel_swipe_right()
        self.ele_page.click(self.ele_page.scrolling_information)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "lashashuyuan", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("教育资源")
    @allure.MASTER_HELPER.testcase("香港浸会大学")
    def test_education_02(self):
        self.ele_page.carousel_swipe_right()
        self.ele_page.carousel_swipe_right()
        self.ele_page.carousel_swipe_right()
        self.ele_page.carousel_swipe_left()
        self.ele_page.click(self.ele_page.scrolling_information)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jinhuidaxue", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("教育资源")
    @allure.MASTER_HELPER.testcase("九龙塘基督堂幼稚园")
    def test_education_03(self):
        self.ele_page.carousel_swipe_left()
        self.ele_page.carousel_swipe_left()
        self.ele_page.carousel_swipe_left()
        self.ele_page.click(self.ele_page.scrolling_information)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jidutangyouzhiyuan", 1)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("天枢座")
    @allure.MASTER_HELPER.testcase("天枢座")
    def test_tianshuzuo(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.tianshuzuo)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "tianshuzuo", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("摇光座")
    @allure.MASTER_HELPER.testcase("")
    def test_yaoguangzuo(self):
        self.ele_page.click(self.ele_page.yaoguangzuo)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "yaoguangzuo")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("天玑座")
    @allure.MASTER_HELPER.testcase("")
    def test_tianjizuo(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.tianjizuo)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "tianjizuo")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("天璇座")
    @allure.MASTER_HELPER.testcase("")
    def test_tianxuanzuo(self):
        self.ele_page.click(self.ele_page.tianxuanzuo)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "tianxuanzuo")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("天权座")
    @allure.MASTER_HELPER.testcase("")
    def test_tianquanzuo(self):
        self.ele_page.click(self.ele_page.tianquanzuo)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "tianquanzuo")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("玉衡座")
    @allure.MASTER_HELPER.testcase("")
    def test_yuhengzuo(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.yuhengzuo)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "yuhengzuo")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("开阳座")
    @allure.MASTER_HELPER.testcase("")
    def test_kaiyangzuo(self):
        self.ele_page.click(self.ele_page.kaiyangzuo)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "kaiyangzuo")
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
    pytest.main(["-s", "test_dongyin.py"])
