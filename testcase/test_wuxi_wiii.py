#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import pytest
import allure
from pages.page_wuxi_wiii import WIIIPages
from utils.basedriver import BaseDriver
from utils.basefile import make_folder
from utils.baseutil import BaseUtil


@allure.MASTER_HELPER.feature("无锡WIII小程序测试")
class TestWuXiWiii:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/无锡WIII"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = WIIIPages(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(950 / 1080 * cls.ele_page.width), int(180 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "无锡WIII")
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(100 / 1080 * cls.ele_page.width), int(220 / 1920 * cls.ele_page.height))
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(100 / 1080 * cls.ele_page.width), int(220 / 1920 * cls.ele_page.height))
        cls.ele_page.sleep(10)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("首页")
    @allure.MASTER_HELPER.testcase("首页截图")
    def test_homepage(self):
        # 首页截图
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "homepage", 4)
        # 回到顶部
        self.ele_page.go_to_top()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图")
    @pytest.mark.skip()
    def test_focus_images(self):
        # 焦点图 1
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(3)
        self.ele_page.video_screenshots(self.result_images, "jiaodiantu1")
        self.ele_page.applet_back()
        # 焦点图 2
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_left()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "jiaodiantu2")
        self.ele_page.applet_back()
        # 焦点图 3
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_right()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "jiaodiantu2")
        self.ele_page.applet_back()
        # 焦点图 4
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("资讯")
    @allure.MASTER_HELPER.testcase("资讯测试")
    def test_information(self):
        # 资讯
        self.ele_page.click(self.ele_page.information)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "zixun", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("地段配套")
    @allure.MASTER_HELPER.testcase("地段配套测试")
    def test_ancillary_facility(self):
        # 地段配套
        self.ele_page.click(self.ele_page.surround_supporting)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "diduanpeitao")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("3D看房")
    @allure.MASTER_HELPER.testcase("3D看房测试")
    def test_3d_house(self):
        # 3D看房
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.cloud_life)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "3dkanfang_list")
        self.ele_page.tap(int(500 / 1080 * self.ele_page.width), int(300 / 1920 * self.ele_page.height))
        self.ele_page.sleep(10)
        self.ele_page.get_screenshot(self.result_images, "quanyuvr_01")
        self.ele_page.swipe_up()
        self.ele_page.get_screenshot(self.result_images, "quanyuvr_02")
        self.ele_page.swipe_down()
        self.ele_page.get_screenshot(self.result_images, "quanyuvr_03")
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "quanyuvr_04")
        self.ele_page.swipe_right()
        self.ele_page.get_screenshot(self.result_images, "quanyuvr_05")
        self.ele_page.sleep(1)
        self.ele_page.applet_back()
        self.ele_page.sleep(1)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("户型")
    @allure.MASTER_HELPER.testcase("户型测试")
    def test_house_type(self):
        # 户型
        self.ele_page.click(self.ele_page.house_type)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxing_list")
        self.ele_page.sleep(2)
        self.ele_page.tap(int(180 / 1080 * self.ele_page.width), int(500 / 1920 * self.ele_page.height))
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxing_detail")
        self.ele_page.sleep(1)
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("卖点轮播")
    @allure.MASTER_HELPER.testcase("卖点轮播测试")
    def test_selling_points(self):
        # 卖点轮播
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.sell_carousel)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "youcesuojin_01", 3)
        self.ele_page.applet_back()
        self.ele_page.carousel_swipe_left()
        self.ele_page.click(self.ele_page.sell_carousel)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "youcesuojin_02", 3)
        self.ele_page.applet_back()
        self.ele_page.carousel_swipe_left()
        self.ele_page.click(self.ele_page.sell_carousel)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "youcesuojin_03", 3)
        self.ele_page.applet_back()
        self.ele_page.carousel_swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "youcesuojin_04")
        self.ele_page.carousel_swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "youcesuojin_05")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("自住&投资")
    @allure.MASTER_HELPER.testcase("视频看房测试")
    def test_video_houses(self):
        # 视频看房
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.video_house)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "shipinkanfang")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("自住&投资")
    @allure.MASTER_HELPER.testcase("效果图测试")
    def test_effect_pictures(self):
        # 效果图
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu_01")
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu_02")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("自住&投资")
    @allure.MASTER_HELPER.testcase("实景图测试")
    def test_realistic_pictures(self):
        # 实景图
        self.ele_page.click(self.ele_page.really_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "shijingtu_01")
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "shijingtu_02")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("自住&投资")
    @allure.MASTER_HELPER.testcase("投资看点测试")
    def test_investment_attraction(self):
        # 投资看点
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.click(self.ele_page.investment_focus)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "touzikandian", 5)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("自住&投资")
    @allure.MASTER_HELPER.testcase("投资回报测试")
    def test_investment_return(self):
        # 投资回报
        self.ele_page.click(self.ele_page.investment_return)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "touzihuibao", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("自住&投资")
    @allure.MASTER_HELPER.testcase("投资保障测试")
    def test_investment_guarantee(self):
        # 投资保障
        self.ele_page.click(self.ele_page.investment_guarantee)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "touzibaozhang", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给朋友")
    @allure.MASTER_HELPER.testcase("我要分享测试")
    def test_i_share(self):
        # 我要分享
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.i_will_share)
        self.ele_page.sleep(2)
        self.ele_page.click(self.ele_page.recent_chat)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "woyaofenxiang")
        self.ele_page.click(self.ele_page.cancel_button)
        self.ele_page.sleep(2)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给朋友")
    @allure.MASTER_HELPER.testcase("生成分享卡片测试")
    def test_create_share_card(self):
        # 生成分享卡片
        self.ele_page.click(self.ele_page.create_share_card)
        self.ele_page.sleep(2)
        self.ele_page.tap(int(100 / 1080 * self.ele_page.width), int(1700 / 1920 * self.ele_page.height))
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "fenxiangkapian")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给朋友")
    @allure.MASTER_HELPER.testcase("我分享的好友测试")
    def test_share_friends(self):
        # 我分享的好友
        self.ele_page.click(self.ele_page.share_friends)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "wofenxiangdehaoyou")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("在线留点")
    @allure.MASTER_HELPER.testcase("在线留点测试")
    def test_leave_phone_online(self):
        # 在线留点
        self.ele_page.tap(int(845 / 1080 * self.ele_page.width), int(1545 / 1920 * self.ele_page.height))
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "tongyiliudian")

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()


if __name__ == '__main__':
    pytest.main(["-s", "test_wuxi_wiii.py"])
