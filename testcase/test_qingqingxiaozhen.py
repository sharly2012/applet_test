#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import allure
import pytest
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from utils.basedriver import BaseDriver
from pages.page_qingqingxiaozhen import GreenTown
from utils.basefile import make_folder
from utils.baseutil import BaseUtil


@allure.MASTER_HELPER.feature("世茂一渡青青小镇小程序测试")
class TestQingQingXiaoZhen:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/世茂一渡青青小镇"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = GreenTown(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width), int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "世茂一渡青青小镇")
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(540 / 1080 * cls.ele_page.width), int(286 / 1920 * cls.ele_page.height))
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(540 / 1080 * cls.ele_page.width), int(286 / 1920 * cls.ele_page.height))
        cls.ele_page.sleep(8)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("首页")
    @allure.MASTER_HELPER.testcase("首页截图测试")
    def test_homepage(self):
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "homepage", 5)
        self.ele_page.sleep(2)
        self.ele_page.go_to_top()
        self.ele_page.sleep(2)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图1测试")
    def test_focus_images_01(self):
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu1", 6)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图2测试")
    def test_focus_images_02(self):
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_left()
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu2")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图3测试")
    def test_focus_images_03(self):
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu3")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图4测试")
    def test_focus_images_04(self):
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_right()
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu4")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图5测试")
    def test_focus_images_05(self):
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu5")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("轻度假山居小镇")
    @allure.MASTER_HELPER.testcase("轻度假山居小镇测试")
    def test_holiday_town(self):
        self.ele_page.click(self.ele_page.holiday_town)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "qingdujiashanjuxiaozhen", 5)
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("小镇俯瞰")
    @allure.MASTER_HELPER.testcase("小镇俯瞰测试")
    def test_overlook_town(self):
        self.ele_page.click(self.ele_page.overlook_town)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "xiaozhenfukan")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目特点")
    @allure.MASTER_HELPER.testcase("项目特点测试")
    def test_project_feature(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.click(self.ele_page.project_feature)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "xiangmutedian", 3)
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("楼盘参数")
    @allure.MASTER_HELPER.testcase("楼盘参数测试")
    def test_property_parameters(self):
        self.ele_page.click(self.ele_page.property_parameters)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "loupancanshu", 2)
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("实时实景")
    @allure.MASTER_HELPER.testcase("实时实景测试")
    def test_real_time_imaging(self):
        self.ele_page.click(self.ele_page.real_time_imaging)
        self.ele_page.get_screenshot(self.result_images, "shishishijing")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("720°青青合院全景")
    @allure.MASTER_HELPER.testcase("720°青青合院全景测试")
    def test_green_full_view(self):
        self.ele_page.click(self.ele_page.green_full_view)
        self.ele_page.sleep(10)
        self.ele_page.get_screenshot(self.result_images, "qingqingheyuanquanjing")
        self.ele_page.sleep(5)
        self.ele_page.swipe_down()
        self.ele_page.get_screenshot(self.result_images, "qingqingheyuanquanjing_01")
        self.ele_page.sleep(1)
        self.ele_page.swipe_up()
        self.ele_page.get_screenshot(self.result_images, "qingqingheyuanquanjing_02")
        self.ele_page.sleep(1)
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "qingqingheyuanquanjing_03")
        self.ele_page.sleep(1)
        self.ele_page.swipe_right()
        self.ele_page.get_screenshot(self.result_images, "qingqingheyuanquanjing_04")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("投资价值测试")
    def test_investment_values(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.investment_values)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "touzijiazhi", 5)
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("地段配套测试")
    def test_ancillary_facility(self):
        self.ele_page.click(self.ele_page.ancillary_facility)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "diduanpeitao")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("户型测试")
    def test_house_type(self):
        self.ele_page.click(self.ele_page.house_type)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxingliebiao")
        self.ele_page.click(self.ele_page.courtyard)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "huxingliebiao")
        self.ele_page.tap(int(0.5 * self.ele_page.width), int(670 / 2244 * self.ele_page.height))
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "huxing_01")
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "huxing_02")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("周边配套图测试")
    def test_coupling_periphery_images(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.coupling_periphery_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "zhoubianpeitaotu_01")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "zhoubianpeitaotu_02")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("样板间图测试")
    def test_sample_room_images(self):
        self.ele_page.click(self.ele_page.sample_room_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiangbanjiantu_01")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "xiangbanjiantu_02")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("项目实景图")
    def test_project_really_image(self):
        self.ele_page.click(self.ele_page.project_really_image)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiangmushijingtu_01")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "xiangmushijingtu_01")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("720°体验青春HOLI")
    @allure.MASTER_HELPER.testcase("720°体验青春HOLI测试")
    def test_experience_youth_holi(self):
        self.ele_page.click(self.ele_page.experience_youth_holi)
        self.ele_page.sleep(10)
        self.ele_page.get_screenshot(self.result_images, "tiyanqingchunHOLI_01")
        self.ele_page.swipe_up()
        self.ele_page.get_screenshot(self.result_images, "tiyanqingchunHOLI_02")
        self.ele_page.sleep(1)
        self.ele_page.swipe_down()
        self.ele_page.get_screenshot(self.result_images, "tiyanqingchunHOLI_03")
        self.ele_page.sleep(1)
        self.ele_page.swipe_left()
        self.ele_page.get_screenshot(self.result_images, "tiyanqingchunHOLI_04")
        self.ele_page.sleep(1)
        self.ele_page.swipe_right()
        self.ele_page.get_screenshot(self.result_images, "tiyanqingchunHOLI_05")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给好友")
    @allure.MASTER_HELPER.testcase("我要分享")
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
    @allure.MASTER_HELPER.testcase("生成分享卡片")
    def test_generate_share_card(self):
        self.ele_page.click(self.ele_page.create_share_card)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "fenxiangkapian_approved")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "fenxiangkapian_null")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给好友")
    @allure.MASTER_HELPER.testcase("我分享的好友")
    def test_share_friends(self):
        self.ele_page.click(self.ele_page.share_friends)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "wofenxiangdehaoyou")
        self.ele_page.applet_back()
        self.ele_page.sleep(1)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("在线留点")
    @allure.MASTER_HELPER.testcase("在线留点")
    def test_leave_online(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.sleep(1)

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()


if __name__ == '__main__':
    pytest.main(["-s", "test_qingqingxiaozhen.py"])
