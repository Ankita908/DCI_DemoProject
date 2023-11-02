import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class SelectFilters:

    drptimerange_ele = "//select[@class='timeRange ng-pristine ng-valid ng-touched']"
    drpfrequency_ele= "//div[@id='timeIntervals']//div//select[@id='DropDown']"
    frequency_bubble = "//span[text()='Time Intervals: 24 Hours']"
    drpcalculation_ele = "//div[@id='calculationContext']//div//select[@id='DropDown']"
    calculation_bubble = "//span[text()='Calculation Context: California LCFS (Energy)']"
    drpdisplaycontent_ele = "//span[text()='Select Display Content']"
    dropdown = "//div[@id='displayContent']//ul[@class ='items']"
    displaycontent_bubble = "//span[text()='Display Content: Fueling Stations']"
    selectall_checkbox = "//input[@id='header-checkbox-displayContent']"
    fuelingstation_checkbox = "//input[@id='checkbox-Fueling Stations']"

    def __init__(self,driver):
        self.driver = driver
        self.timerange_selected = None
        self.timerange_option = None
        self.frequency_selected = None
        self.frequency_option = None
        self.time_interval_bubble = None
        self.calculation_selected = None
        self.calculation_option =None
        self.chk_selectall =None
        self.displaycontent_option =None

    def select_timerange(self):
        time.sleep(10)
        self.timerange_selected = Select(self.driver.find_element(By.XPATH, self.drptimerange_ele))
        self.timerange_selected.click()
        self.timerange_selected.select_by_index(3)
        self.timerange_option = self.timerange_selected.first_selected_option
        print("Selected option is:", self.timerange_option.text)

    def select_frequency(self):
        time.sleep(20)
        self.frequency_selected = Select(self.driver.find_element(By.XPATH, self.drpfrequency_ele))
        self.frequency_selected.select_by_index(0)
        self.frequency_option = self.frequency_selected.first_selected_option
        print("dsfdsfdsfsd")
        print("sdfdsfdsfdss")
        print("Selected option is:", self.frequency_option.text)

        time.sleep(10)
        self.time_interval_bubble = self.driver.find_element(By.XPATH, self.frequency_bubble).get_attribute("textContent")
        #print("Time interval is", self.time_interval_bubble)

    def select_calculationcontext(self):
        time.sleep(10)
        self.calculation_selected = Select(self.driver.find_element(By.XPATH, self.drpcalculation_ele))
        self.calculation_selected.select_by_index(0)
        self.calculation_option = self.calculation_selected.first_selected_option
        print("Selected option is: ", self.calculation_option.text)

        time.sleep(10)
        self.calculation_bubble = self.driver.find_element(By.XPATH, self.calculation_bubble).get_attribute("textContent")
        print("Calculation Context is: ", self.calculation_bubble)

    def select_displaycontent(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.drpdisplaycontent_ele).click()
        self.chk_selectall = self.driver.find_element(By.XPATH, self.selectall_checkbox)
        if self.chk_selectall.is_selected():
            self.chk_selectall.click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, self.drpdisplaycontent_ele).click()
        self.driver.find_element(By.XPATH, self.fuelingstation_checkbox).click()
        self.displaycontent_option = self.driver.find_element(By.XPATH, self.fuelingstation_checkbox).get_attribute("value")
        print("selected Content option is: ", self.displaycontent_option)

        time.sleep(10)
        self.displaycontent_bubble = self.driver.find_element(By.XPATH, self.displaycontent_bubble).get_attribute("textContent")
        print("Display Content is: ", self.displaycontent_bubble)






