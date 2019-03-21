#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import allure
import pytest
from utils.basedriver import BaseDriver
from pages.page_chaojiwan import PageSuperBay
from utils.basefile import make_folder
from utils.baseutil import BaseUtil


@allure.MASTER_HELPER.feature("超级湾小程序测试")
class TestSuperBay:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/超级湾"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageSuperBay(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "超级湾")
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
        for i in range(5):
            self.ele_page.get_screenshot(self.result_images, "homepage")
            self.ele_page.wechat_swipe_up()
            self.ele_page.sleep(1)
        self.ele_page.go_to_top(7)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图测试")
    def test_focus_image(self):
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu_04")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("news")
    @allure.MASTER_HELPER.testcase("news测试")
    def test_information(self):
        self.ele_page.click(self.ele_page.information)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "xuanchuang", 1)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目简介")
    @allure.MASTER_HELPER.testcase("Video 1")
    def test_video_1(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.video_1)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "video_1")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目简介")
    @allure.MASTER_HELPER.testcase("Video 2")
    def test_video_2(self):
        self.ele_page.click(self.ele_page.video_2)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "video_1")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目简介")
    @allure.MASTER_HELPER.testcase("VR漫游")
    def test_vr(self):
        self.ele_page.click(self.ele_page.vr)
        self.ele_page.sleep(8)
        self.ele_page.get_screenshot(self.result_images, "vrmanyou")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "vrmanyou")
        self.ele_page.swipe_right()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "vrmanyou")
        self.ele_page.swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "vrmanyou")
        self.ele_page.swipe_down()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "vrmanyou")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目简介")
    @allure.MASTER_HELPER.testcase("全景直播")
    def test_panoramic_live(self):
        self.ele_page.click(self.ele_page.full_view)
        self.ele_page.sleep(8)
        self.ele_page.video_screenshots(self.result_images, "quanjingzhibo")
        self.ele_page.click_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目简介")
    @allure.MASTER_HELPER.testcase("漫游厦门湾")
    def test_walk_xiamen_bay(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.visit_xiamen)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "manyouxiamenwan", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目简介")
    @allure.MASTER_HELPER.testcase("点击你的超级生活")
    def test_super_life(self):
        self.ele_page.click(self.ele_page.super_life)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "dianjinidechaojishenghuo", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目简介")
    @allure.MASTER_HELPER.testcase("拥有厦门湾的理由")
    def test_owner_xiamen_bay(self):
        self.ele_page.click(self.ele_page.own_xiamen)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "yongyouxiamenwan", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("户型鉴赏")
    @allure.MASTER_HELPER.testcase("岛屿海组团 ")
    def test_island_sea(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.island_sea)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "daoyuhai")
        self.ele_page.click(self.ele_page.house_01)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "gaoceng-A1")
        self.ele_page.click(self.ele_page.house_a3)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "gaoceng-A3")
        self.ele_page.click(self.ele_page.house_a4)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "gaoceng-A4")
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("户型鉴赏")
    @allure.MASTER_HELPER.testcase("山屿海组团")
    def test_cloud_sea(self):
        self.ele_page.click(self.ele_page.cloud_sea)
        self.ele_page.click(self.ele_page.house_list_02)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "shanyuhai")
        self.ele_page.click(self.ele_page.house_02)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "guanhaiju-1")
        self.ele_page.click(self.ele_page.house_002)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "guanhaiju-2")
        self.ele_page.click(self.ele_page.house_003)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "guanhaiju-3")
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("户型鉴赏")
    @allure.MASTER_HELPER.testcase("望云海组团")
    def test_mountain_sea(self):
        self.ele_page.click(self.ele_page.mountain_sea)
        self.ele_page.click(self.ele_page.house_list_03)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "wangyunhai")
        self.ele_page.click(self.ele_page.house_03)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "gaoceng-1")
        self.ele_page.click(self.ele_page.house_0002)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "gaoceng-2")
        self.ele_page.click(self.ele_page.house_0003)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "gaoceng-3")
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("美图鉴赏")
    @allure.MASTER_HELPER.testcase("样板间图")
    def test_sample_room_switch(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.sample_room_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("美图鉴赏")
    @allure.MASTER_HELPER.testcase("周边配套图")
    def test_area_support(self):
        self.ele_page.click(self.ele_page.area_support_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "zhoubianpeitaotu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "zhoubianpeitaotu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("美图鉴赏")
    @allure.MASTER_HELPER.testcase("实景图")
    def test_really_images(self):
        self.ele_page.click(self.ele_page.really_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "shijingtu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "shijingtu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("美图鉴赏")
    @allure.MASTER_HELPER.testcase("效果图")
    def test_effect_images(self):
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("相册切换")
    @allure.MASTER_HELPER.testcase("相册切换")
    def test_images_folder_switch(self):
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiangce_01")
        self.ele_page.click(self.ele_page.image_folder_02)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce_02")
        self.ele_page.click(self.ele_page.image_folder_03)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce_03")
        self.ele_page.click(self.ele_page.image_folder_04)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce_04")
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
    @allure.MASTER_HELPER.story("IM")
    @allure.MASTER_HELPER.testcase("IM")
    def test_share_friends(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.chat_online)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "zaixianzixun")
        self.ele_page.click_back()

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()


if __name__ == '__main__':
    pytest.main(["-s", "test_chaojiwan.py"])
