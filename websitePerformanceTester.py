from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
url="http://burymewithmymoney.com/"

linksRepo = [url]
linksTime = []

def linkstab(url):
    driver.get(url)
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    pageLoad = driver.execute_script("return window.performance.timing.loadEventEnd")
    pageLoad = (pageLoad - navigationStart)/1000

    linksTime.append(pageLoad)
    linkElements = driver.find_elements_by_xpath("//a[@href]")
    links=[]

    for i in linkElements:
        links.append(i.get_attribute("href"))

    for i in links:
        if i.find("#") ==-1:
            if i not in linksRepo:
                linksRepo.append(i)
                linkstab(i)


linkstab(url)
for i in range(0,len(linksRepo)):
    print(linksRepo[i],linksTime[i])