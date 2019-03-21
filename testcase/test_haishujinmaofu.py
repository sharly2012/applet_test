#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import pytest
import allure
from utils.basedriver import BaseDriver
from pages.page_haishujinmaofu import PageHaiShuJinMaoFu
from utils.basefile import make_folder
from utils.baseutil import BaseUtil


@allure.MASTER_HELPER.feature("海曙金茂府测试")
class TestHaiShuJinMaoFu:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/海曙金茂府"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageHaiShuJinMaoFu(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "海曙金茂府")
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
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu1", 6)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图2测试")
    def test_focus_images_02(self):
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_left()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu2", 6)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图2测试")
    def test_focus_images_03(self):
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu2", 6)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("动态资讯")
    @allure.MASTER_HELPER.testcase("动态资讯测试")
    def test_dynamic_information(self):
        self.ele_page.click(self.ele_page.dynamic_information)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "dongtaizixun", 6)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("户型鉴赏测试")
    def test_house_view(self):
        self.ele_page.click(self.ele_page.house_type)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxingliebiao")
        self.ele_page.click(self.ele_page.house_01)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "huxing1", 2)
        self.ele_page.click(self.ele_page.house_131)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "huxing")
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("项目参数测试")
    def test_project_parameters(self):
        self.ele_page.click(self.ele_page.project_parameters)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "xiangmucanshu", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("周边配套测试")
    def test_area_supporting(self):
        self.ele_page.click(self.ele_page.area_supporting)
        self.ele_page.sleep(5)
        self.ele_page.click(self.ele_page.cancel_button)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "zhoubianpeitao")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("城市全景")
    @allure.MASTER_HELPER.testcase("城市全景测试")
    def test_city_full_view(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.city_full_view)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "chengshiquanjing")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("示范区漫游")
    @allure.MASTER_HELPER.testcase("示范区漫游测试")
    def test_demon_area_walking(self):
        self.ele_page.click(self.ele_page.demon_area_walking)
        self.ele_page.sleep(8)
        self.ele_page.get_screenshot(self.result_images, "shifanqumanyou_01")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "shifanqumanyou_02")
        self.ele_page.swipe_right()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "shifanqumanyou_03")
        self.ele_page.swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "shifanqumanyou_04")
        self.ele_page.swipe_down()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "shifanqumanyou_05")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("府系科技")
    @allure.MASTER_HELPER.testcase("府系科技测试")
    def test_jinmao_technology(self):
        self.ele_page.click(self.ele_page.technology)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "fuxikeji", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("实景图测试")
    def test_really_images(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.really_images)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "shijingtu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "shijingtu2")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("样板间图测试")
    def test_sample_room_images(self):
        self.ele_page.click(self.ele_page.sample_room_images)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("效果图测试")
    def test_effect_images(self):
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("相册切换")
    @allure.MASTER_HELPER.testcase("相册切换测试")
    def test_images_folder_switch(self):
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "xiangce1")
        self.ele_page.click(self.ele_page.image_folder_02)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce2")
        self.ele_page.click(self.ele_page.image_folder_03)
        self.ele_page.sleep(1)
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
    pytest.main(["-s", "test_haishujinmaofu.py"])
