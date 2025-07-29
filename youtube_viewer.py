from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

video_url = "https://youtu.be/bNiUTlv8B-k"  # ဒီကို မင်းရဲ့ video URL ထည့်

options = Options()
options.add_argument("--headless")  # မမြင်အောင်ဖွင့်
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1280x720")

driver = webdriver.Chrome(options=options)
driver.get(video_url)

print("▶️ Viewing video for 40 seconds...")
time.sleep(40)

driver.quit()
print("✅ View sent successfully.")
