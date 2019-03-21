#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: gb18030 -*-

# @author: sharly

import pytest
import allure
from utils.basedriver import BaseDriver
from pages.page_dongyin import PageDongYin
from utils.basefile import make_folder
from utils.baseutil import BaseUtil


@allure.MASTER_HELPER.feature("东印")
class TestDongYin:

    @classmethod
    def setup_class(cls):
        cls.screenshots_folder = BaseUtil().root_path + "/screenshots/东印"
        make_folder(cls.screenshots_folder)
        current_time = BaseUtil().get_current_time()
        cls.result_images = cls.screenshots_folder + "/" + current_time
        make_folder(cls.result_images)
        base_driver = BaseDriver()
        cls.driver = base_driver.applet_driver()
        # 打开微信
        cls.ele_page = PageDongYin(cls.driver)
        cls.ele_page.click(cls.ele_page.discovery)
        cls.ele_page.swipe_up()
        # 打开小程序
        cls.ele_page.click(cls.ele_page.applet)
        cls.ele_page.sleep(3)
        cls.ele_page.tap(int(995 / 1080 * cls.ele_page.width),
                         int(145 / 1920 * cls.ele_page.height))
        # 搜索小程序
        cls.ele_page.click(cls.ele_page.search_applet)
        cls.ele_page.send_keys(cls.ele_page.search_applet, "东印")
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
        for i in range(8):
            self.ele_page.get_screenshot(self.result_images, "homepage")
            self.ele_page.wechat_swipe_up()
            self.ele_page.sleep(1)
        self.ele_page.go_to_top(scroll_times=9)

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图1测试")
    def test_focus_images_01(self):
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu1", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图2测试")
    def test_focus_images_02(self):
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_right()
        self.ele_page.swipe_left()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu2")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图3测试")
    def test_focus_images_03(self):
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_right()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "jiaodiantu3")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("焦点图")
    @allure.MASTER_HELPER.testcase("焦点图4测试")
    def test_focus_images_04(self):
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.click(self.ele_page.focus_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaodiantu4", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("项目概述")
    @allure.MASTER_HELPER.testcase("项目概述测试")
    def test_project_overview(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.project_overview)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "xiangmujieshao", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("CBD黄金地段")
    @allure.MASTER_HELPER.testcase("CBD黄金地段测试")
    def test_gold_area(self):
        self.ele_page.click(self.ele_page.gold_area)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "CBDhuangjindiduan", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("推荐户型效果")
    @allure.MASTER_HELPER.testcase("推荐户型效果测试")
    def test_house_effect_images(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.house_effect_images)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "tuijianhuxingxiaoguotu", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("户型区域")
    @allure.MASTER_HELPER.testcase("户型介绍测试")
    def test_house_introduce(self):
        self.ele_page.click(self.ele_page.house_introduce)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "huxingliebiao")
        self.ele_page.click(self.ele_page.house_list_01)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "huxing_1")
        self.ele_page.click(self.ele_page.administrative_mansion)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "gerenxingzhengguandi")
        self.ele_page.click(self.ele_page.personal_mansion)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "gerenguandi")
        self.ele_page.applet_back()
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("户型区域")
    @allure.MASTER_HELPER.testcase("楼盘参数测试")
    def test_property_parameters(self):
        self.ele_page.click(self.ele_page.property_parameters)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "loupancanshu")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("户型区域")
    @allure.MASTER_HELPER.testcase("交付标准测试")
    def test_delivery_standards(self):
        self.ele_page.click(self.ele_page.delivery_standards)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "jiaofubiaozhun", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("3D看房")
    @allure.MASTER_HELPER.testcase("3D看房测试")
    def test_view_3D(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.view_3D)
        self.ele_page.sleep(8)
        self.ele_page.get_screenshot(self.result_images, "3dkanfang")
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "3dkanfang")
        self.ele_page.swipe_right()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "3dkanfang")
        self.ele_page.swipe_up()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "3dkanfang")
        self.ele_page.swipe_down()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "3dkanfang")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("装修风格")
    @allure.MASTER_HELPER.testcase("装修风格测试")
    def test_decoration_style(self):
        self.ele_page.click(self.ele_page.decoration_style)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshot(self.result_images, "xiangce1")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce1")
        self.ele_page.click(self.ele_page.images_folder_02)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "xiangce2")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce2")
        self.ele_page.click(self.ele_page.images_folder_03)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "xiangce3")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce3")
        self.ele_page.click(self.ele_page.images_folder_04)
        self.ele_page.sleep(2)
        self.ele_page.get_screenshot(self.result_images, "xiangce4")
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.swipe_left()
        self.ele_page.sleep(1)
        self.ele_page.get_screenshot(self.result_images, "xiangce4")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("轮播区域")
    @allure.MASTER_HELPER.testcase("轮播区域1测试")
    def test_carousel_area_01(self):
        self.ele_page.carousel_area_right()
        self.ele_page.carousel_area_right()
        self.ele_page.carousel_area_right()
        self.ele_page.click(self.ele_page.carousel_area)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "wujiwubiandeyouyongchi", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("轮播区域")
    @allure.MASTER_HELPER.testcase("轮播区域2测试")
    def test_carousel_area_02(self):
        self.ele_page.carousel_area_left()
        self.ele_page.carousel_area_left()
        self.ele_page.carousel_area_left()
        self.ele_page.carousel_area_right()
        self.ele_page.click(self.ele_page.carousel_area)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "kongzhonghuayuan", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("轮播区域")
    @allure.MASTER_HELPER.testcase("轮播区域3测试")
    def test_carousel_area_03(self):
        self.ele_page.carousel_area_left()
        self.ele_page.carousel_area_left()
        self.ele_page.carousel_area_left()
        self.ele_page.click(self.ele_page.carousel_area)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "datangrukou", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("多图区域")
    @allure.MASTER_HELPER.testcase("多图区域1测试")
    def test_multiple_images_area_01(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.multiple_images_area)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "huwaiyundong", 5)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("多图区域")
    @allure.MASTER_HELPER.testcase("多图区域2测试")
    def test_multiple_images_area_02(self):
        self.ele_page.multiple_images_left()
        self.ele_page.click(self.ele_page.multiple_images_area)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "taotianmeishi", 4)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("投资向左")
    @allure.MASTER_HELPER.testcase("投资价值测试")
    def test_investment_value(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.investment_value)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "touzijiazhi", 3)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("投资向左")
    @allure.MASTER_HELPER.testcase("物业服务测试")
    def test_property_service(self):
        self.ele_page.click(self.ele_page.property_service)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "wuyefuwu", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("投资向左")
    @allure.MASTER_HELPER.testcase("购房流程测试")
    def test_purchase_process(self):
        self.ele_page.click(self.ele_page.purchase_process)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "goufanganju", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("投资向左")
    @allure.MASTER_HELPER.testcase("无忧托管测试")
    def test_safe_custody(self):
        self.ele_page.click(self.ele_page.safe_custody)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "wuyoutuoguan", 1)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("移民向右")
    @allure.MASTER_HELPER.testcase("移民资格测试")
    def test_immigrant_status(self):
        self.ele_page.swipe_left()
        self.ele_page.click(self.ele_page.immigrant_status)
        self.ele_page.sleep(3)
        self.ele_page.get_screenshot(self.result_images, "yiminzige")
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("移民向右")
    @allure.MASTER_HELPER.testcase("移民政策测试")
    def test_immigrant_policy(self):
        self.ele_page.click(self.ele_page.immigrant_policy)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "yiminzhengce", 1)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("移民向右")
    @allure.MASTER_HELPER.testcase("物业服务测试")
    def test_property_service_2(self):
        self.ele_page.click(self.ele_page.property_service_2)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "wuyefuwu", 2)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("移民向右")
    @allure.MASTER_HELPER.testcase("安居流程测试")
    def test_housing_services(self):
        self.ele_page.click(self.ele_page.housing_services)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "anjuliucheng", 1)
        self.ele_page.applet_back()

    @allure.MASTER_HELPER.severity("blocker")
    @allure.MASTER_HELPER.story("开发商介绍")
    @allure.MASTER_HELPER.testcase("开发商介绍测试")
    def test_developers_introduce(self):
        self.ele_page.wechat_swipe_up()
        self.ele_page.click(self.ele_page.developers_introduce)
        self.ele_page.sleep(5)
        self.ele_page.get_screenshots_by_slide_up(self.result_images, "kaifangshangjieshao", 2)
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
    pytest.main(["-s", "test_dongyin.py"])
