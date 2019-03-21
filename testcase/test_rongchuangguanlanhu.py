#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import pytest
import allure
from utils.baseutil import BaseUtil
from utils.basedriver import BaseDriver
from utils.basefile import make_folder
from pages.page_rongchuangguanlanhu import PageSUNACMissionHills


@allure.MASTER_HELPER.feature("融创观澜湖公园壹号")
class TestSUNACMissionHills:
    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/融创观澜湖公园壹号"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageSUNACMissionHills(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "融创观澜湖公园壹号")
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
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.sleep(0.5)
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu_01")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图2测试")
    def test_focus_images_02(self):
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_left()
        self.ele_page.sleep(0.5)
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu_02")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图3测试")
    def test_focus_images_03(self):
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(0.5)
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu_03")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图4测试")
    def test_focus_images_04(self):
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_right()
        self.ele_page.sleep(0.5)
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu_04")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图5测试")
    def test_focus_images_05(self):
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(0.5)
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu_05")

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("资讯")
    @allure.MASTER_HELPER.testcase("资讯测试")
    def test_information(self):
        self.ele_page.click(self.ele_page.information)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "zixun", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("海南度假攻略")
    @allure.MASTER_HELPER.testcase("海南度假攻略测试")
    def test_hainan_holiday(self):
        self.ele_page.click(self.ele_page.HaiNan_holiday)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "hainandujia", 5)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("悦享观澜湖时光")
    @allure.MASTER_HELPER.testcase("悦享观澜湖时光测试")
    def test_mission_hills_time(self):
        self.ele_page.click(self.ele_page.MissionHills_time)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "yuexiangguanlanhushiguang", 5)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目介绍")
    @allure.MASTER_HELPER.testcase("项目介绍测试")
    def test_project_introduce(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.project_introduce)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "xiangmujieshao", 5)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("区位风采")
    @allure.MASTER_HELPER.testcase("区位风采测试")
    def test_area_park(self):
        self.ele_page.click(self.ele_page.area_park)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshot(self.result_images, "quweifengcai")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("户型鉴赏")
    @allure.MASTER_HELPER.testcase("户型鉴赏测试")
    def test_house_type(self):
        self.ele_page.click(self.ele_page.house_type)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxingliebiao")
        self.ele_page.click(self.ele_page.house_01)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "huxing_a", 2)
        self.ele_page.click(self.ele_page.house_c)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "huxing_c", 2)
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("全盛配套")
    @allure.MASTER_HELPER.testcase("全盛配套测试")
    def test_full_supporting(self):
        self.ele_page.click(self.ele_page.full_supporting)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "quanshengpeitao", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("实景样板")
    @allure.MASTER_HELPER.testcase("实景样板间测试")
    def test_really_images_sample(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.really_images_sample)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "shijingyangban_01")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "shijingyangban_02")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("相册切换")
    @allure.MASTER_HELPER.testcase("相册切换测试")
    def test_image_folders_switch(self):
        self.ele_page.click(self.ele_page.really_images_sample)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "xiangceqiehuan_01")
        self.ele_page.click(self.ele_page.really_images_button)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangceqiehuan_02")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精装品质")
    @allure.MASTER_HELPER.testcase("精装品质测试")
    def test_hardcover_configuration(self):
        self.ele_page.click(self.ele_page.hardcover_configuration)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jingzhuangpinzhi", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("720°全景生活馆")
    @allure.MASTER_HELPER.testcase("720°全景生活馆测试")
    def test_full_view_life(self):
        self.ele_page.click(self.ele_page.full_view_life)
        self.ele_page.sleep(8)
        self.ele_page.get_screenshot(self.result_images, "quanjingshenghuoguan_01")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "quanjingshenghuoguan_02")
        self.ele_page.swipe_right()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "quanjingshenghuoguan_03")
        self.ele_page.swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "quanjingshenghuoguan_04")
        self.ele_page.swipe_down()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "quanjingshenghuoguan_05")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("融创品牌")
    @allure.MASTER_HELPER.testcase("融创品牌测试")
    def test_sunac_brand(self):
        self.ele_page.click(self.ele_page.SUNAC_brand)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "rongchuangpinpai", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("融创心享")
    @allure.MASTER_HELPER.testcase("融创心享测试")
    def test_sunac_heart_enjoy(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.SUNAC_heart_enjoy)
        self.ele_page.sleep(4)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "rongchuangxinxiang", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("分享给好友")
    @allure.MASTER_HELPER.testcase("我要分享测试")
    def test_i_will_share(self):
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
    pytest.main(["-s", "test_rongchuangguanlanhu.py"])
