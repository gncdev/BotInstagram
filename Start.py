from selenium import webdriver
import time
import random
import string
import sys


def start():
	while True:
		try:
			text = str(input("Please put Special(s) or Unlimited(u)"))
			if text == "s":
				number = int(input("Please put a above number"))
				special(number)
			elif text == "u":
				unlimited()
			else:
				print("Please put Special(s) or Unlimited(u)")
		except Exception:
			sys.exit(1)


def special(number: int):
	if number is 0:
		print("Please put a someone value")
		sys.exit(1)
	for i in range(number):
		browser = webdriver.Chrome()
		browser.get("https://www.instagram.com")
		time.sleep(1)
		try:
			def mail(stringLength=8):
				letters = string.ascii_lowercase
				return ''.join(random.choice(letters) for i in range(stringLength))
			
			
			def password(stringLength=8):
				lettersAndDigits = string.ascii_letters + string.digits
				return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
			
			
			def clickKaydol():
				browser.find_element_by_xpath(
					'//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span').click()
			
			
			clickKaydol()
			time.sleep(1)
			newemail = mail() + "@gmail.com"  # Mail
			newname = mail() + " " + mail()  # Full Name
			newuser = mail()  # Username
			newpass = password()  # Password
			
			email = browser.find_element_by_name("emailOrPhone")
			name = browser.find_element_by_name("fullName")
			user = browser.find_element_by_name("username")
			passwordd = browser.find_element_by_name("password")
			
			email.send_keys(newemail)
			name.send_keys(newname)
			user.send_keys(newuser)
			passwordd.send_keys(newpass)
			time.sleep(1)
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click()
			time.sleep(2)
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[2]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[1]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[31]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button').click()
			print(newemail)
			print(newname)
			print(newpass)
			print(newuser)
			print("------------")
			f = open("accounts.txt", "a+")
			f.write("\nMail: " + newemail + "\n")
			f.write("Name: " + newname + "\n")
			f.write("Username: " + newuser + "\n")
			f.write("Password: " + newpass + "\n")
			f.write("------------------")
			f.close()
		except Exception:
			browser.close()
			browser = webdriver.Chrome()
			browser.get("https://www.instagram.com")
			time.sleep(1)
			
			def mail(stringLength=8):
				letters = string.ascii_lowercase
				return ''.join(random.choice(letters) for i in range(stringLength))
			
			
			def password(stringLength=8):
				lettersAndDigits = string.ascii_letters + string.digits
				return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
			
			
			def clickKaydol():
				browser.find_element_by_xpath(
					'//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span').click()
			
			
			clickKaydol()
			time.sleep(1)
			newemail = mail() + "@gmail.com"  # Mail
			newname = mail() + " " + mail()  # Full Name
			newuser = mail()  # Username
			newpass = password()  # Password
			
			email = browser.find_element_by_name("emailOrPhone")
			name = browser.find_element_by_name("fullName")
			user = browser.find_element_by_name("username")
			passwordd = browser.find_element_by_name("password")
			
			email.send_keys(newemail)
			name.send_keys(newname)
			user.send_keys(newuser)
			passwordd.send_keys(newpass)
			
			time.sleep(3)
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button').click()
			time.sleep(2)
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[2]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[1]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[31]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button').click()
			print(newemail)
			print(newname)
			print(newpass)
			print(newuser)
			print("------------")
			f = open("accounts.txt", "a+")
			f.write("\nMail: " + newemail + "\n")
			f.write("Name: " + newname + "\n")
			f.write("Username: " + newuser + "\n")
			f.write("Password: " + newpass + "\n")
			f.write("------------------\n")
			f.close()


def unlimited():
	while True:
		browser = webdriver.Chrome()
		browser.get("https://www.instagram.com")
		time.sleep(1)
		try:
			def mail(stringLength=8):
				letters = string.ascii_lowercase
				return ''.join(random.choice(letters) for i in range(stringLength))
			
			
			def password(stringLength=8):
				lettersAndDigits = string.ascii_letters + string.digits
				return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
			
			
			def clickKaydol():
				browser.find_element_by_xpath(
					'//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span').click()
			
			
			clickKaydol()
			time.sleep(1)
			newemail = mail() + "@gmail.com"  # Mail
			newname = mail() + " " + mail()  # Full Name
			newuser = mail()  # Username
			newpass = password()  # Password
			
			email = browser.find_element_by_name("emailOrPhone")
			name = browser.find_element_by_name("fullName")
			user = browser.find_element_by_name("username")
			passwordd = browser.find_element_by_name("password")
			
			email.send_keys(newemail)
			name.send_keys(newname)
			user.send_keys(newuser)
			passwordd.send_keys(newpass)
			time.sleep(1)
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click()
			time.sleep(2)
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[2]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[1]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[31]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button').click()
			print(newemail)
			print(newname)
			print(newpass)
			print(newuser)
			print("------------")
			f = open("accounts.txt", "a+")
			f.write("\nMail: " + newemail + "\n")
			f.write("Name: " + newname + "\n")
			f.write("Username: " + newuser + "\n")
			f.write("Password: " + newpass + "\n")
			f.write("------------------")
			f.close()
		except Exception:
			browser.close()
			browser = webdriver.Chrome()
			browser.get("https://www.instagram.com")
			time.sleep(1)
			
			def mail(stringLength=8):
				letters = string.ascii_lowercase
				return ''.join(random.choice(letters) for i in range(stringLength))
			
			
			def password(stringLength=8):
				lettersAndDigits = string.ascii_letters + string.digits
				return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))
			
			
			def clickKaydol():
				browser.find_element_by_xpath(
					'//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span').click()
			
			
			clickKaydol()
			time.sleep(1)
			newemail = mail() + "@gmail.com"  # Mail
			newname = mail() + " " + mail()  # Full Name
			newuser = mail()  # Username
			newpass = password()  # Password
			
			email = browser.find_element_by_name("emailOrPhone")
			name = browser.find_element_by_name("fullName")
			user = browser.find_element_by_name("username")
			passwordd = browser.find_element_by_name("password")
			
			email.send_keys(newemail)
			name.send_keys(newname)
			user.send_keys(newuser)
			passwordd.send_keys(newpass)
			
			time.sleep(3)
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button').click()
			time.sleep(2)
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[2]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[1]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[31]').click()
			browser.find_element_by_xpath(
				'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button').click()
			print(newemail)
			print(newname)
			print(newpass)
			print(newuser)
			print("------------")
			f = open("accounts.txt", "a+")
			f.write("\nMail: " + newemail + "\n")
			f.write("Name: " + newname + "\n")
			f.write("Username: " + newuser + "\n")
			f.write("Password: " + newpass + "\n")
			f.write("------------------\n")
			f.close()


start()
