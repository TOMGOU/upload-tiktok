from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def isElementExist(browser, element):
  flag=True
  try:
    browser.find_element_by_css_selector(element)
    return flag
  except:
    flag=False
    return flag

def upload_video(browser):
  # 点击上传按钮
  WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'upload-icon'))
  )
  upload_button = browser.find_element_by_class_name('upload-icon')
  upload_button.click()
  # 上传视频
  WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'upload-btn-input--36XER'))
  )
  video_upload_button = browser.find_element_by_class_name('upload-btn-input--36XER')
  video_upload_button.send_keys('/Users/tangyong/Desktop/NBA/kiviberry.mp4')
  WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'stage-2-text--3_0-C'))
  )
  WebDriverWait(browser, 100).until_not(
    EC.presence_of_element_located((By.CLASS_NAME, 'stage-2-text--3_0-C'))
  )
  # 标题输入
  video_title_input = browser.find_element_by_class_name('public-DraftStyleDefault-block')
  video_title_input.send_keys('tiktok upload video test')
  submit_button = browser.find_elements_by_class_name('button--1SZwR')
  submit_button[1].click()

option = webdriver.ChromeOptions()
option.add_argument(r'user-data-dir=/Users/tangyong/Library/Application Support/Google/Chrome')
browser = webdriver.Chrome(chrome_options=option, executable_path='/Users/tangyong/Application/chromedriver')
# browser = webdriver.Chrome(executable_path='/Users/tangyong/Application/chromedriver')
browser.get('https://www.tiktok.com/foryou?loginType=google&lang=en')

isExistLogin = isElementExist(browser, '.login-button')
if isExistLogin:
  # 点击登录按钮
  WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'login-button'))
  )
  login_button = browser.find_element_by_class_name('login-button')
  login_button.click()
  # 切换iframe
  WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
  )
  login_iframe = browser.find_element_by_tag_name('iframe')
  # browser.switch_to_frame(login_iframe)
  browser.switch_to.frame(login_iframe)
  # 选择谷歌登录方式
  WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'channel-item-wrapper-27bh9'))
  )
  google_login_element = browser.find_elements_by_class_name('channel-item-wrapper-27bh9')
  google_login_element[2].click()
  time.sleep(5)
  # 选择账号
  handles = browser.window_handles
  browser.switch_to.window(handles[1])
  isExistAcount = isElementExist(browser, '.WBW9sf')
  if isExistAcount:
    WebDriverWait(browser, 100).until(
      EC.presence_of_element_located((By.CLASS_NAME, 'WBW9sf'))
    )
    google_acount_element = browser.find_element_by_class_name('WBW9sf')
    google_acount_element.click()
    browser.switch_to.window(handles[0])
    time.sleep(15)
    upload_video(browser)
else:
  upload_video(browser)
  