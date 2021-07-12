from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driverPath = '/path/to/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=driverPath)
driver.get("https://www.indeed.com/")
#print(driver.page_source)
#driver.quit()

inputElement = driver.find_element_by_xpath("//*[@id='text-input-what']")
inputElement.send_keys('data scientist')
inputElement = driver.find_element_by_xpath("//*[@id='text-input-where']")
inputElement.send_keys('Anywhere').element.submit()
#print(driver.page_source)
searchCount = fltright.find_element(By.CSS_SELECTOR, "div[id$='searchCountPages']")
number = searchCount.text
number = number.replace("Page 1 of ", "") 
number = number.replace("jobs", "") 
number = int(number)
## Number of times to loop
## The default search returns 15 searches per page!
pages = 1+(number//15)



## Initialize empty DataFrame
mainData = []

jobsInaPage = ["//*[@id='sj_c6c8add4ba4796c7')]",
                "//*[@id='sj_01d74653e79ad87a')]",
                "//*[@id='job_c8c865cdae54d117']",
"//*[@id='job_f59b24f7e2326735']",
"//*[@id='job_0063434d1d4baa06']",
"//*[@id='job_2f20ac5e6a13cd47']",
"//*[@id='job_64f7a3fb0fc7b83c']",
"//*[@id='sj_9edc6905aa3ae688']",
"//*[@id='job_c6c8add4ba4796c7']",
"//*[@id='job_4a64a9033cf12d82']",
"//*[@id='job_914e4951f45129fc']",
"//*[@id='job_a3237b13bc2232a0']",
"//*[@id='job_ddcadf5d09c98310']",
"//*[@id='job_6776c113ea6f92d6']",
"//*[@id='job_790c137804ab4d6c']",
] 
i = 0
while page <=pages:
    for i in jobsInaPage:
      inputElement = driver.find_element_by_xpath().click()
      title = driver.find_element_by_xpath("//*[@id='viewJobSSRRoot']/span/div/div[1]/div/div[2]/div[1]"]).element.text
      employer = driver.find_element_by_xpath("//*[@id='viewJobSSRRoot']/span/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/a"]).element.text
      location = driver.find_element_by_xpath("//*[@id='viewJobSSRRoot']/span/div/div[1]/div/div[2]/div[2]/div/div/div[2]"]).element.text
      salary = driver.find_element_by_xpath("//*[@id='viewJobSSRRoot']/span/div/div[1]/div/div[3]/span[1]"]).element.text
      description = driver.find_element_by_xpath("//*[@id='viewJobSSRRoot']/span/div/div[2]"]).element.text  
      dataSinglePage = {'title': [title], 'employer': [employer],'location': [location],salary': [salary],'description': [description]}                                        
      mainDate.append(dataSinglePage)
      mainDate = pd.concat(dataSinglePage)            
      # This is to move to the next stage                    
    inputElement = driver.find_element_by_xpath("//*[@id='resultsCol']/nav/div/ul/li[6]/a"]).click()
    page=page+1

mainData.to_excel("jobs.xlsx")  
