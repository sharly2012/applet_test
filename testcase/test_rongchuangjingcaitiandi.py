#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import pytest
import allure
from utils.baseutil import BaseUtil
from utils.basedriver import BaseDriver
from utils.basefile import make_folder
from pages.page_rongchuangjingcaitiandi import PageSUNACWonderfulWorld


@allure.MASTER_HELPER.feature("融创精彩天地测试")
class TestSUNACWonderfulWorld:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/融创精彩天地"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageSUNACWonderfulWorld(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "融创精彩天地")
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
    @allure.MASTER_HELPER.testcase("焦点图测试")
    def test_focus_image(self):
        self.ele_page.click(self.ele_page.focus_image)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu", 7)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("自贸港建设")
    @allure.MASTER_HELPER.testcase("自贸港建设测试")
    def test_fta_build(self):
        self.ele_page.click(self.ele_page.FTA_build)
        self.ele_page.sleep(5)
        self.ele_page.video_screenshots(self.result_images, "zimaogangjianshe")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("政策解读")
    @allure.MASTER_HELPER.testcase("政策解读测试")
    def test_policy_interpretation(self):
        self.ele_page.click(self.ele_page.policy_interpretation)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "zhengcejiedu", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("资讯")
    @allure.MASTER_HELPER.testcase("资讯测试")
    def test_information(self):
        self.ele_page.click(self.ele_page.information)
        self.ele_page.sleep(4)
        self.ele_page.video_screenshots(self.result_images, "zixun")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("区域交通")
    @allure.MASTER_HELPER.testcase("区域交通测试")
    def test_area_translation(self):
        self.ele_page.click(self.ele_page.area_translation)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "quyujiaotong")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目实景")
    @allure.MASTER_HELPER.testcase("全景看房")
    def test_full_view(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.full_view)
        self.ele_page.sleep(8)
        self.ele_page.get_screenshot(self.result_images, "quanjingkanfang_01")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "quanjingkanfang_02")
        self.ele_page.swipe_right()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "quanjingkanfang_03")
        self.ele_page.swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "quanjingkanfang_05")
        self.ele_page.swipe_down()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "quanjingkanfang_05")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目实景")
    @allure.MASTER_HELPER.testcase("户型鉴赏")
    def test_house_type(self):
        self.ele_page.click(self.ele_page.house_type)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxingleibiao")
        self.ele_page.click(self.ele_page.house_1)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxing_01")
        self.ele_page.click(self.ele_page.house_d)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "huxing_02", 2)
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("格调会所")
    @allure.MASTER_HELPER.testcase("格调会所测试")
    def test_style_club(self):
        self.ele_page.click(self.ele_page.style_club)
        self.ele_page.sleep(3)
        self.ele_page.video_screenshots(self.result_images, "gediaohuisuo")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("融创品牌测试")
    def test_sunac_brand(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.SUNAC_brand)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "rongchuangpinpai", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("融创物业测试")
    def test_sunac_property(self):
        self.ele_page.click(self.ele_page.SUNAC_property)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "rongchuangwuye", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("双托管测试")
    def test_double_hosting(self):
        self.ele_page.click(self.ele_page.double_hosting)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "shuangtuoguan", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("融创承租")
    @allure.MASTER_HELPER.testcase("融创承租测试")
    def test_sunac_tenant(self):
        self.ele_page.click(self.ele_page.SUNAC_tenant)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "rongchuangchengzu", 2)
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
        self.ele_page.click(self.ele_page.IM)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "guwen")
        self.ele_page.click_back()

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()


if __name__ == '__main__':
    pytest.main(["-s", "test_rongchuangjingcaitiandi.py"])
