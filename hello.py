import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import json
import sys

# # 定义一个要返回的 JSON 数据
# data_to_return = {
#     "name": "John Doe",
#     "age": 30,
#     "email": "johndoe@example.com"
# }

# # 将数据转换为 JSON 字符串并输出到标准输出
# print(json.dumps(data_to_return))

def pre() :
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # 使用無頭模式，不顯示瀏覽器視窗
    options.add_argument('--disable-gpu')  # 禁用GPU加速，避免一些可能的問題

    # 使用Chrome瀏覽器
    driver = webdriver.Chrome(options=options)
    driver.get('https://serv.gcis.nat.gov.tw/pub/cmpy/prefCaseListAction.do')
    driver.implicitly_wait(10)

    input_field1 = driver.find_element( By.NAME, 'prefixNo')  
    input_field1.send_keys("112047018")

    input_field1 = driver.find_element( By.NAME, 'applyNameForPrefixNo')  
    input_field1.send_keys("李子龍")

    button = driver.find_element( By.XPATH, '/html/body/form/table[6]/tbody/tr[1]/th/div/input[1]')
    button.click()

    button = driver.find_element( By.XPATH, '/html/body/form/table[4]/tbody/tr[1]/td[2]/a')
    button.click()
    # alert = driver.switch_to.alert
    # alert.dismiss()

    # 找到對應的元素
    cell_element = driver.find_element(By.XPATH, "/html/body/form/table[4]/tbody/tr/td/table/tbody/tr[1]/td[1]")

    # 取得文字內容
    precheck_num = cell_element.text
    print(precheck_num)

    cell_element = driver.find_element(By.XPATH, "/html/body/form/table[4]/tbody/tr/td/table/tbody/tr[3]/td[1]")

    # 取得文字內容
    company_name = cell_element.text
    print(company_name)

    driver.close()
    # word = driver.f
    # time.sleep( 5 )

def main() :

    success = False
    pre()

    # # 获取命令行参数
    # name = sys.argv[1]
    # age = int(sys.argv[2])
    # email = sys.argv[3]

    # # 定义一个要返回的 JSON 数据
    # data_to_return = {
    #     "name": name,
    #     "age": age,
    #     "email": email
    # }

    # # 将数据转换为 JSON 字符串并输出到标准输出
    # print(json.dumps(data_to_return))
    
    # while not success :
    #     try :
    #         pre()
    #         success = True
    #     except Exception as exp:
    #         print(exp)

if __name__ == "__main__":
    main()