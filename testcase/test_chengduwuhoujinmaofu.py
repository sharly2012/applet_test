#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import pytest
import allure
from utils.basedriver import BaseDriver
from pages.page_chengduwuhoujinmaofu import PageChengDuWuHouJinMaoFu
from utils.basefile import make_folder
from utils.baseutil import BaseUtil

image_path = "E:/PycharmProjects/wechat_test/template/成都武侯金茂府/"


@allure.MASTER_HELPER.feature("成都武侯金茂府测试")
class TestChangAnJinMaoFu:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/成都武侯金茂府"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageChengDuWuHouJinMaoFu(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "成都武侯金茂府")
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
        self.ele_page.focus_swipe_right()
        focus_image = self.ele_page.find_element(*self.ele_page.focus_images)
        actual_image = self.ele_page.get_screenshot_by_element(focus_image, self.result_images, "jiaodiantu1")
        temp_image = image_path + "jiaodiantu1.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu1", 5)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图2测试")
    def test_focus_images_02(self):
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_right()
        self.ele_page.focus_swipe_left()
        focus_image = self.ele_page.find_element(*self.ele_page.focus_images)
        actual_image = self.ele_page.get_screenshot_by_element(focus_image, self.result_images, "jiaodiantu2")
        temp_image = image_path + "jiaodiantu2.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu2", 5)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图3测试")
    def test_focus_images_03(self):
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_right()
        focus_image = self.ele_page.find_element(*self.ele_page.focus_images)
        actual_image = self.ele_page.get_screenshot_by_element(focus_image, self.result_images, "jiaodiantu3")
        temp_image = image_path + "jiaodiantu3.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu3", 8)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图4测试")
    def test_focus_images_04(self):
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        self.ele_page.focus_swipe_left()
        focus_image = self.ele_page.find_element(*self.ele_page.focus_images)
        actual_image = self.ele_page.get_screenshot_by_element(focus_image, self.result_images, "jiaodiantu4")
        temp_image = image_path + "jiaodiantu4.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu4", 5)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("最新资讯")
    @allure.MASTER_HELPER.testcase("最新资讯测试")
    def test_information(self):
        # information = self.ele_page.find_element(*self.ele_page.information)
        self.ele_page.click(self.ele_page.information)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "zuixinzixun", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("户型鉴赏测试")
    def test_house_type(self):
        house_type = self.ele_page.find_element(*self.ele_page.house_type)
        actual_image = self.ele_page.get_screenshot_by_element(house_type, self.result_images, "huxingjianshang")
        temp_image = image_path + "huxingjianshang.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.house_type)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxingliebiao")
        self.ele_page.click(self.ele_page.house_list_01)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "huxing_d")
        self.ele_page.click(self.ele_page.house_e)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "huxing_e")
        self.ele_page.click(self.ele_page.house_f)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "huxing_e")
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("楼盘参数测试")
    def test_project_parameters(self):
        project_parameters = self.ele_page.find_element(*self.ele_page.project_parameters)
        actual_image = self.ele_page.get_screenshot_by_element(project_parameters, self.result_images, "loupancanshu")
        temp_image = image_path + "loupancanshu.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.project_parameters)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "loupancanshu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("了解项目")
    @allure.MASTER_HELPER.testcase("周边配套测试")
    def test_area_supporting(self):
        area_supporting = self.ele_page.find_element(*self.ele_page.area_supporting)
        actual_image = self.ele_page.get_screenshot_by_element(area_supporting, self.result_images, "zhoubianpeitao")
        temp_image = image_path + "zhoubianpeitao.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.area_supporting)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "zhoubianpeitao")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("府系科技")
    @allure.MASTER_HELPER.testcase("府系科技测试")
    def test_technology(self):
        self.ele_page.wechat_swipe_up()
        technology = self.ele_page.find_element(*self.ele_page.technology)
        actual_image = self.ele_page.get_screenshot_by_element(technology, self.result_images, "fuxikeji")
        temp_image = image_path + "fuxikeji.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.technology)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "fuxikeji", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("实景图测试")
    def test_really_images(self):
        really_images = self.ele_page.find_element(*self.ele_page.really_images)
        actual_image = self.ele_page.get_screenshot_by_element(really_images, self.result_images, "shijingtu")
        temp_image = image_path + "shijingtu.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.really_images)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "shijingtu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "shijingtu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("样板间图测试")
    def test_sample_room_images(self):
        sample_room_images = self.ele_page.find_element(*self.ele_page.sample_room_images)
        actual_image = self.ele_page.get_screenshot_by_element(sample_room_images, self.result_images, "yangbanjiantu")
        temp_image = image_path + "yangbanjiantu.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.sample_room_images)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "yangbanjiantu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("精彩图片")
    @allure.MASTER_HELPER.testcase("效果图测试")
    def test_effect_images(self):
        effect_images = self.ele_page.find_element(*self.ele_page.effect_images)
        actual_image = self.ele_page.get_screenshot_by_element(effect_images, self.result_images, "xiaoguotu")
        temp_image = image_path + "xiaoguotu.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "xiaoguotu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("相册切换")
    @allure.MASTER_HELPER.testcase("相册切换测试")
    def test_images_folder_switch(self):
        self.ele_page.click(self.ele_page.effect_images)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "xiangce_01")
        self.ele_page.click(self.ele_page.image_folder_02)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce_02")
        self.ele_page.click(self.ele_page.image_folder_03)
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce_03")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("人物访谈")
    @allure.MASTER_HELPER.testcase("人物访谈测试")
    def test_interview(self):
        self.ele_page.wechat_swipe_up()
        interview = self.ele_page.find_element(*self.ele_page.interview)
        actual_image = self.ele_page.get_screenshot_by_element(interview, self.result_images, "renwucaifang")
        temp_image = image_path + "renwucaifang.png"
        assert self.ele_page.same_as(temp_image, actual_image)
        self.ele_page.click(self.ele_page.interview)
        self.ele_page.video_screenshots(self.result_images, "renwufangtan")
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
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.chat_online)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "zaixianzixun")
        self.ele_page.click_back()

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()


if __name__ == '__main__':
    pytest.main(["-s", "test_chengduwuhoujinmaofu.py"])
