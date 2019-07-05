import time
import bridge
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

canal_web_source = 'http://www.greatlakes-seaway.com/R2/jsp/mNiaBrdgStatus.jsp?language=E'
welland_canal_api = 'https://wellandcanalapi.kaluba.tech'

try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get(canal_web_source)

    list_elements = driver.find_element_by_css_selector('div.sections')

    list_items = list_elements.find_elements_by_tag_name("li")

    json_output = "[ "

    for item in list_items:
        split_item = item.text.replace('Bridge ', '').replace(
            'Bridge Status:', '').replace('Status: ', '').replace('Next Arrival: ', '').splitlines()

        bridge_id = split_item[0]
        bridge_status = split_item[2]
        next_arrival = split_item[3]

        canal_bridge = bridge.Bridge(bridge_id, bridge_status, next_arrival)
        json_output += canal_bridge.toJsonString() + " ,"

    driver.quit()

    json_output = json_output[:-1]
    json_output += " ]"

    data = {'payload': json_output}

    update_status_url = welland_canal_api+'/update_bridge_status'

    request = requests.post(url=update_status_url, data=data)
    print(json_output)
except:
    print('An error occured.')
