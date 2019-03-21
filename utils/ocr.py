import configparser
from aip import AipOcr


class OCR(object):

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read("E:/PycharmProjects/wechat_test/conf/config.ini")
        APP_ID = conf.get("OCR", "APP_ID")
        API_KEY = conf.get("OCR", "API_KEY")
        SECRET_KEY = conf.get("OCR", "SECRET_KEY")
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def get_ocr_words(self, filePath):
        """ 调用通用文字识别, 图片参数为本地图片 """
        words_list = []
        image = self.get_file_content(filePath)
        response = self.client.basicGeneral(image)
        words_length = response.get("words_result_num")
        for i in range(words_length):
            words_list.append(response.get("words_result")[i]["words"])
            print(response.get("words_result")[i]["words"])
        return words_list

    def get_ocr_words_option(self, filePath):
        """ 带参数调用通用文字识别, 图片参数为本地图片 """
        words_list = []
        image = self.get_file_content(filePath)
        options = {"language_type": "CHN_ENG",
                   "detect_direction": "true",
                   "detect_language": "true",
                   "probability": "true"
                   }
        response = self.client.basicGeneral(image, options)
        words_length = response.get("words_result_num")
        for i in range(words_length):
            words_list.append(response.get("words_result")[i]["words"])
            print(response.get("words_result")[i]["words"])
        return words_list


if __name__ == '__main__':
    file_path = "E:/PycharmProjects/wechat_test/screenshots/成都武侯金茂府/2019-03-20_10/2019-03-20_10-15-28_jiaodiantu1_0.png"
    ocr = OCR()
    ll = ocr.get_ocr_words(file_path)
    print("***************************")
    ocr.get_ocr_words_option(file_path)
