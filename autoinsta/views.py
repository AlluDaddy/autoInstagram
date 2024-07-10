from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
# import templates
from django import forms
from better_profanity import profanity
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException, ElementNotVisibleException
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException, TimeoutException, ElementNotVisibleException)


class LoginForm(forms.Form):
    usern = forms.CharField(label='usern', max_length=100)
    passw = forms.CharField(label='passw', max_length=100)


def login(request):
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':

        # return redirect('/processing')
    return render(request, "login.html")


def process(request:HttpRequest):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.data)
            print(form.data["usern"])
            print(form.data['passw'])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/home', {"data": form.data})
    print(request.body)
    return render(request, "process.html")



def home(request):
    print(2+3)
    global block_list

    block_list = []

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.data)
            print(form.data["usern"])
            print(form.data['passw'])
            # print()
            # friends_list = ["Instagram User"].append()
            friends_list = form.data['friends_list'].split(",")
            friends_list = [i.strip() for i in friends_list]
            friends_list.append("Instagram User")
            friends_list.append(",")
            # friends_list = form.data['friends_list'].split(",").append("Instagram User")
            print(friends_list)
#selenium starts
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome()
            # driver_path = 'D:\Download(D)\chromedriver_win32\chromedriver.exe'
            # driver = webdriver.Chrome(options=options, executable_path=driver_path)
            driver.get("https://www.instagram.com/")
            driver.maximize_window()
            time.sleep(6)
# autoinsta_123
# autoinsta_123!

            driver.find_element("name", "username").send_keys(form.data["usern"])
            driver.find_element("name", "password").send_keys(form.data['passw'])
            ele = driver.find_element("xpath",'//*[@id="loginForm"]/div/div/button/div')
            ele.click()
            time.sleep(5)
            try:
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '*//div[contains(text(),"Not now")]')))
                # if element:
                # if driver.find_element_by_xpath("//*/section/main/div/div/div/div/button"):
                #     not_btn = driver.find_element_by_xpath("//*/section/main/div/div/div/div/button")
                # if driver.find_element_by_xpath('*//button[contains(text(),"Not Now")]'):
                    # not_btn = driver.find_element_by_xpath('*//button[contains(text(),"Not Now")]')
                driver.execute_script("arguments[0].click();", element)
            except:
                # assert False, "Failed"
                driver.refresh()
                pass
            # print("56789098765")
            # driver.close()
            time.sleep(3)
            try:
                print("TRY 1")
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '*//button[contains(text(),"Not Now")]' )))
                print("1. ",element)
                driver.execute_script("arguments[0].click();", element)
                print("CLICKED")
            except:
                # assert False, "Failed"
                driver.refresh()
                pass


            print(2)
            element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "*//span[text()='Messages']")))
            message_icon = driver.find_element("xpath","*//span[text()='Messages']")
            message_icon.click()
            # element = WebDriverWait(driver, 30).until(EC.elements_to_be_clickable(By.XPATH,"*//span/div/div/span"))
            # ele = driver.find_elements("xpath","//*/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div")[0:]
            # ele = driver.find_elements("xpath","*//span/div/div/span")

            count = -1
            while True:
            # for i in range(len(element)):
                # ele = driver.find_elements("xpath", "*//span/div/div/span")
                time.sleep(5)
                # ele = driver.find_elements("xpath", "*//div[@role='listitem']")
                ele = driver.find_elements("xpath", "*//div[@role='listitem']//*//div[2]/div")
                count+=1
                if count==len(ele):
                    break
                
                print("COunt1 -", count)
                # print(ele)

                # for i in ele:
                #     print(i.text)

                time.sleep(1)
                try:
                    WebDriverWait(driver, 50,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(ele[count]) or EC.element_to_be_selected(ele[count]))
                    print(ele[count].text)
                    entire_text = ele[count].text
                    lines = entire_text.split('\n')
                    # Strip leading and trailing spaces from the first line
                    first_line = lines[0].strip()
                    print(first_line)
                except:
                    pass
                print("COunt2 -", count)

                # if ele[count].is_displayed and ele[count].is_enabled:
                    # name = ele[count].text
                print("name ---->"+ first_line)
                if first_line in friends_list:
                    print(f"This user is a friend {first_line}")
                    continue
                time.sleep(1)
                if ele[count].is_enabled:
                    ele[count].click()

# ?????????????????????????????????? Might be already blocked contact
                try:
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '*//div[text()="Unblock"]')))
                    print("-----------> already blocked")
                    continue


                    # element = WebDriverWait(driver, 30).until(
                    #     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Stay")]')))

                    # driver.execute_script("arguments[0].click();", element)
                except:
                    pass

                time.sleep(10)
                # ele_mess = driver.find_elements("xpath","//*[contains(@class, '_aacl _aaco _aacu _aacx _aad9 _aadf')]")
                ele_mess = driver.find_elements("xpath","*//div[@role='presentation']/span/div")
                data = " "
                for j in range(len(ele_mess)):
                    ele_mess = driver.find_elements("xpath",
                                                    "*//div[@role='presentation']/span/div")
                    time.sleep(0.5)
                    # WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reply-button"))).click()

                    # mes = WebDriverWait(driver, 20).until(EC.presence_of_element_located(j))
                    # b = WebDriverWait(driver, 30).until(EC.presence_of_element_located(j))
                    if ele_mess[j].is_displayed:
                        WebDriverWait(driver, 30,ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(ele_mess[j]))
                        data+= f" {ele_mess[j].text} " 
                    # print(data)
                    time.sleep(0.5)
                print("data: -", data)
                x = profanity.contains_profanity(data)
                if x:
                    try:
                        # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_abm0"]/*[name()="svg"][@aria-label="View Thread Details"]'))).click()
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '*//div//*[@aria-label="Conversation information"]'))).click()
                        time.sleep(2)
                        # driver.execute_script("arguments[0].click();", element)
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "*//div/span[text()='Block']" ))).click()

                        time.sleep(2)

                        # # driver.execute_script("arguments[0].click();", element)
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "*//div/button[text()='Block']" ))).click()
                        # driver.execute_script("arguments[0].click();", element) 
                        # time.sleep(2)
                        block_list.append(ele[count].text)
                        print(block_list)

                    except:
                        pass
        driver.close()
    return render(request, "home.html", context={"block_list": block_list}) 
        
    
 

#  can add censor words and can adjust threshold to find offensive sentences