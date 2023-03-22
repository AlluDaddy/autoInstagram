from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# import templates



import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By





def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # print("87656789767876")
        # create a form instance and populate it with data from the request:
        # form = NameForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        return redirect('/processing')
    # redirect("87656789767876")

    # return redirect('/login')
    return render(request, "login.html")


def process(request):

    # def __init__(self):
        # return render(request, "process.html")
        
    return render(request, "process.html")







# def home(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def home(request):
    print(2+3)


    # profanity-check -https://towardsdatascience.com/build-your-language-filter-with-python-d6502f9c224b


    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver_path = 'D:\Download(D)\chromedriver_win32\chromedriver.exe'
    # driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    time.sleep(6)
    driver.find_element("name", "username").send_keys("madarauchiha_1702")
    driver.find_element("name", "password").send_keys("@Madarauchiha1")
    ele = driver.find_element("xpath",'//*[@id="loginForm"]/div/div[3]/button/div')
    ele.click()
    time.sleep(5)
    try:
        element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '*//div[contains(text(),"Not Now")]' )))
        # if element:
        # if driver.find_element_by_xpath("//*/section/main/div/div/div/div/button"):
        #     not_btn = driver.find_element_by_xpath("//*/section/main/div/div/div/div/button")
        # if driver.find_element_by_xpath('*//button[contains(text(),"Not Now")]'):
            # not_btn = driver.find_element_by_xpath('*//button[contains(text(),"Not Now")]')
        driver.execute_script("arguments[0].click();", element)
    except:
        assert False, "Failed"
        # pass
    # print("56789098765")
    # driver.close()
    time.sleep(5)
    try:
        print("TRY 1")
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '*//button[contains(text(),"Not Now")]' )))
        print("1. ",element)
        driver.execute_script("arguments[0].click();", element)
        print("CLICKED")
    except:
        assert False, "Failed"
        # pass

    time.sleep(10)
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='xh8yej3 x1iyjqo2']/div[5]" )))
    message_icon = driver.find_element("xpath","//*[@class='xh8yej3 x1iyjqo2']/div[5]")
    message_icon.click()
    time.sleep(10)
    ele = driver.find_elements("xpath","//*/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div")[0:]


    # count = 0

    # for i in ele:
    #     count+=1
    #     if count ==3:
    #         try:
    #             WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_abm0"]/*[name()="svg"][@aria-label="View Thread Details"]'))).click()
    #             time.sleep(2)
    #             # driver.execute_script("arguments[0].click();", element)
    #             WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "*//div[contains(text(),'Block')]" ))).click()

    #             time.sleep(2)

    #             # driver.execute_script("arguments[0].click();", element)
    #             WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "*//button[contains(text(),'Block')]" ))).click()
    #             # driver.execute_script("arguments[0].click();", element)
    #             time.sleep(2)
    #         except:
    #             pass
    #     i.click()
    #     time.sleep(10)    
    #     ele_mess = driver.find_elements("xpath","//*[contains(@class, '_aacl _aaco _aacu _aacx _aad9 _aadf')]")
    #     data = []
    #     for j in ele_mess:
    #         data.append(j.text)
    #         print(data)
    #         time.sleep(5)


    driver.close()

    return render(request, "home.html")