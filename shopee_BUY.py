from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 用cmd 到 C:program files\google\chrome\application 執行下面指令開啟chrome
# chrome.exe --remote-debugging-port=9527 --user-data-dir="D:\selenium\AutomationProfile"

# 要先在開啟的chrome登入蝦皮才能知道購物車內容
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")

#把chromeDriver.exe放在跟檔案同個目錄下，所以括號內不用指定路徑
driver=webdriver.Chrome(options=options)

#購物車連結
driver.get('https://shopee.tw/cart')

def product():# 點擊產品
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div:nth-child(3) > div > div > div.container > div.if-swd > div:nth-child(3) > div.SFF7z2 > div > div._5sTIHk > label"))).click()
    driver.find_element_by_css_selector("#main > div > div:nth-child(3) > div > div > div:nth-child(3) > div.rnocow.uEhFYV > div.s1Gxkq.c2pfrq > button.shopee-button-solid.shopee-button-solid--primary").click()

def seller_coupon():# 點擊賣場優惠券
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div:nth-child(3) > div > div.OX-2Lj > div.sqxwIi > div:nth-child(2) > div > div:nth-child(1) > div > div.uw1QJu > div.za7qoR > div.zjjc32 > div > div > button"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shopVouchersModal > div.\+idyFV.Bk\+p3j > ul > div:nth-child(1) > div > div.vc_VoucherStandardTemplate_template > div.vc_VoucherStandardTemplate_right > div.vc_VoucherStandardTemplate_center"))).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shopVouchersModal > div.\+idyFV.Bk\+p3j > div.qll9xC > button.btn.btn-solid-primary.btn--s.btn--inline.jisMFY"))).click()

def address():# address
    driver.find_element_by_css_selector("#main > div > div:nth-child(3) > div > div.OX-2Lj > div.sqxwIi > div:nth-child(2) > div > div.wVzdz- > div.OUah6W.Fzg\+Gz > button.elfp9W.div-style.G2khyK").click()
    driver.find_element_by_css_selector("#modal > div.xqPzbI > div.Jctoqx > div.V\+iu34 > div.Jk2CC4 > div > div:nth-child(1) > div.ZtGG3s > div:nth-child(2) > div.E0Vlko").click()
    driver.find_element_by_css_selector("#modal > div.xqPzbI > div.Jctoqx > div.goH\+bH > div > div > div > button.stardust-button.stardust-button--primary.jJRY5R").click()

def coupon():# 優惠券

    driver.find_element_by_css_selector("#main > div > div:nth-child(3) > div > div.OX-2Lj > div.\+w8dNn > div.At3Wkr > div._84yUzo > button").click()
        # 免運券
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal > div.stardust-popup > div.stardust-popup__dialog--wrapper > div > div.stardust-popup__dialog--wrapper-top > div > div > div > div > div > div.shopee-popup-form__main > div > div.u6HdhE.d9WDAK > div.vc_Card_container.vc_Card_fsv.vc_Card_inapplicable.vc_VoucherStandardTemplate_fsv.vc_VoucherStandardTemplate_inapplicable.vc_free-shipping-voucher_pc > div > div.vc_VoucherStandardTemplate_template > div.vc_VoucherStandardTemplate_right > div.vc_VoucherStandardTemplate_center > div"))).click()
        # 打折券
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal > div.stardust-popup > div.stardust-popup__dialog--wrapper > div > div.stardust-popup__dialog--wrapper-top > div > div > div > div > div > div.shopee-popup-form__main > div > div.u6HdhE.d9WDAK > div:nth-child(5) > div:nth-child(2) > div > div.vc_VoucherStandardTemplate_template > div.vc_VoucherStandardTemplate_right > div.vc_VoucherStandardTemplate_center > div"))).click()
    driver.find_element_by_css_selector("#modal > div.stardust-popup > div.stardust-popup__dialog--wrapper > div > div.stardust-popup__dialog--wrapper-top > div > div > div > div > div > div.shopee-popup-form__footer > button.btn.btn-solid-primary.btn--s.btn--inline.e5P6KA").click()

def shop_coin():# 蝦幣
    driver.find_element_by_css_selector("#main > div > div:nth-child(3) > div > div.OX-2Lj > div.\+w8dNn > div.a\+7foE > div._5bMjRo > label > div").click()

def confirm():#下訂單
    driver.find_element_by_css_selector("#main > div > div:nth-child(3) > div > div.OX-2Lj > div.DS2ZYY > div.KQyCj0 > div.uTFqRt > button").click()

product()
seller_coupon()
address()
coupon()
# shop_coin()
# confirm()
