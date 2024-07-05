import time

from selenium import webdriver
from selenium.webdriver.common.by import By


text1= 'SCENE: As the curtain rises, we see a BURGLAR making a forced entry through a window, into a third-floor flat in a high-class apartment block. He is carrying the classic burglars torch. He takes a look around. In the darkness we begin to make out furniture, drapes and tapestries, and valuable old paintings. The BURGLAR closes the shutters, and then switches the light on. Just as he is about to open a drawer, the phone rings. He panics. His first impulse is to beat a hasty retreat, but then he realises that there is no sign of life in the house, and so he has nothing to fear. He returns to his work. He tries to ignore the ringing phone, but cant. Stealthily he creeps up to the phone, and leaps on it. He picks up the handset, and holds it to his chest, covering it with his jacket. As if trying to suffocate it.\n SCENE: As the curtain rises, we see a BURGLAR making a forced entry through a window, into a third-floor flat in a high-class apartment block. He is carrying the classic burglars torch. He takes a look around. In the darkness we begin to make out furniture, drapes and tapestries, and valuable old paintings. The BURGLAR closes the shutters, and then switches the light on. Just as he is about to open a drawer, the phone rings. He panics. His first impulse is to beat a hasty retreat, but then he realises that there is no sign of life in the house, and so he has nothing to fear. He returns to his work. He tries to ignore the ringing phone, but cant. Stealthily he creeps up to the phone, and leaps on it. He picks up the handset, and holds it to his chest, covering it with his jacket. As if trying to suffocate it. '
print(text1[:400])
print(text1[400:800])
print(text1[800:1200])
time.sleep(8)   

driver =webdriver.Firefox()
driver.get("https://translate.google.co.in/?sl=en&tl=hi&op=translate")
time.sleep(8)

obj_len = 400
starting = 0
for i in range(0,3):
    if len(text1)>=obj_len:
        driver.find_element(By.CSS_SELECTOR, ".er8xn").send_keys(text1[starting:obj_len])
        time.sleep(8)
        starting = obj_len
        obj_len = obj_len + 400

        converted_text = driver.find_element(By.CSS_SELECTOR, ".ChMk0b > span:nth-child(1)").text
        print(converted_text)
        time.sleep(10)

        n = 2
        for j in range(n,9):
            try:
                converted_text2 = driver.find_element(By.CSS_SELECTOR,
                                                      f'span.jCAhz:nth-child({str(n)}) > span:nth-child(1)').text
                n = n + 1
                print(converted_text2)
                time.sleep(10)
            except:
                pass

            driver.find_element(By.CSS_SELECTOR, ".er8xn").clear()
            time.sleep(10)

'''
        n = 2
        try:
            converted_text2= driver.find_element(By.CSS_SELECTOR,f'span.jCAhz:nth-child({str(n)}) > span:nth-child(1)').text
            n = n + 1
            print(converted_text2)
            time.sleep(10)
        except:
            pass
        try:
            converted_text2 = driver.find_element(By.CSS_SELECTOR,
                                                  f'span.jCAhz:nth-child({str(n)}) > span:nth-child(1)').text
            n = n + 1
            print(converted_text2)
            time.sleep(10)
        except:
            pass
        try:
            converted_text2 = driver.find_element(By.CSS_SELECTOR,
                                                  f'span.jCAhz:nth-child({str(n)}) > span:nth-child(1)').text
            n = n + 1
            print(converted_text2)
            time.sleep(10)
        except:
            pass

        driver.find_element(By.CSS_SELECTOR, ".er8xn").clear()
        time.sleep(10)

        '''







