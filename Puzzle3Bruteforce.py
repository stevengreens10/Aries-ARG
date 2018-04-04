# coding: utf-8

import requests

session = requests.session()
session.proxies = {'http':  'socks5h://localhost:9150',
                   'https': 'socks5h://localhost:9150'}
                   
def try_answer(answer):
    url = "http://irrgartenxhc4pur.onion/03-JZJUSRCFKJPUYT2P"
    fields = {
        "♊": str(answer),
        "login": ""
    }
    headers = {'Host': "irrgartenxhc4pur.onion",
               'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               'Accept-Language': "en-US,en;q=0.5",
               'Accept-Encoding': "gzip, deflate",
               'Connection': "keep-alive",
               'Upgrade-Insecure-Requests': "1",
               'Referer': "http://irrgartenxhc4pur.onion/03-JZJUSRCFKJPUYT2P/"
               }
    session.get(url, headers=headers).headers # Gets the page, setting php sess id
    response = session.post(url + "/index.php", data=fields).text # Gets the text of the page
    if("False." in response):
        return False
    else: 
        print True
        
def calculate_answer(disappointments,
                     height,
                     corners,
                     expected,
                     fruit_power):    
    # Already calculated
    step_13 = 17
    
    xiv_answer = step_13
    
    # Step 14
    xiv_answer = xiv_answer * disappointments
    
    # Step 28
    answer = height + corners
    
    # Step 29 (rounded)
    answer = answer / expected
    
    # Step 30
    answer = answer ** fruit_power
    
    # NOT DONE
    
    
    return answer
    
answer = calculate_answer(33, 18000, 12, 17, 3)    
print try_answer(answer)