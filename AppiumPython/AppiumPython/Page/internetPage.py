#coding=utf-8
import Base
import time

class internetPage():
    #driver = Base.Base.driver
    def __init__(self,driver):
        self.driver=driver
    # 页面标题
    def pagetitle(self):
        time.sleep(1)
        return self.driver.find_element_by_id("com.guokr.mentor:id/top_bar_text")

    # 返回按钮
    def back(self):
        time.sleep(1)
        return self.driver.find_element_by_id("com.guokr.mentor:id/top_bar_lefticon")

