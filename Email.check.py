import time
import sys as n
import time as mm
def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 120)
print('required documents : >>>')
slow("""
insta.email.txt / gmail.txt / hotmail.txt""")
time.sleep(1)
lib = input("""
The tool checks if the email is linked to one of the written sites
( instagram / gmail / hotmail ) 
Before running, put the e-mail in its file

Click enter to start ...
==========================================
""")
import os
import sys
import json
import time
import requests
import sys as n
import time as mm
#JOKER @vv1ck
def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 120)
slow(""" 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
▌  ____  _                _            ▐
▌ / ___ |#|__   ___  ___ | | __        ▐
▌| |    |#'##\ / _ \/ __ | |/ /        ▐
▌| |___ |#| |#|  __/ (__ |   <         ▐
▌ \____ |#| |#|\___|\___ |_|\_\        ▐
▌                           ╔═╗ ╦   ╦  ▐
▌    insta/gmail/hotmail    ╠═╣ ║   ║  ▐
▌       vv1ck , JOKER       ╩ ╩ ╩═╝ ╩═╝▐
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
time.sleep(1)
slow("""
  [1]> instagram [2]> gmail [3]> hotmail
""")
print(" ")
joker = input(">> [Enter the number] : ")
print("""

""")
if joker == '1':
	slow("""
██ ███    ██ ███████ ████████  █████  
██ ████   ██ ██ vv1ck   ██    ██   ██ 
██ ██ ██  ██ ███████    ██    ███████
██ ██  ██ ██      ██    ██    ██   ██ 
██ ██   ████ ███████    ██    ██   ██
              
              CHECK EMAIL (insta) ..

""")
	slow("wait a little bit ..")
	time.sleep(1)
	#JOKER @vv1ck
	jok = 'insta.email.txt'
	file = open(jok, "r")
	while True:
		jok = file.readline().split('\n')[0]
		url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
		headers = {
	        "accept": "*/*",
	        "accept-encoding": "gzip,deflate,br",
	        "accept-language": "ar,en-US;q=0.9,en;q=0.8",
	        "content-length": "49",
	        "content-type": "application/x-www-form-urlencoded",
	        "origin": "https://www.instagram.com",
	        "referer": "https://www.instagram.com/accounts/password/reset/",
	        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
	        "x-csrftoken": "j4u26vxxC6D7eE63HhBde0ahZeN4mVfK",
	        "x-ig-app-id": "936619743392459"
	    }#JOKER @vv1ck
		data = {"email_or_username":jok, "recaptcha_challenge_field": ""}
		req = requests.post(url, headers=headers, data=data)
		if req.status_code == 200:
			print ('>> The email is used [insta] :\n ' + jok)
			print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			with open ('[$] insta.Unavailable.txt', 'a') as x:
				x.write (jok + '\n')
				print ("")
		else:
			print ('>> Email is available [insta] :\n ' + jok)
			print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			with open ('[$] insta.Available.txt', 'a') as x:
				x.write (jok + '\n')
				print ("")	
#JoKER @vv1ck
elif joker == '2':
	slow("""
 ██████╗ ███╗   ███╗ █████╗ ██╗██╗     
██╔════╝ ████╗ ████║██╔══██╗██║██║     
██║  ███╗██╔████╔██║███████║██║██║     
██║   ██║██║╚██╔╝██║██╔══██║██║██║     
╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗
 ╚═════╝ ╚═╝vv1ck╚═╝╚═╝  ╚═╝╚═╝╚══════╝
             
             CHECK EMAIL (gmail) ..

""")
	slow("wait a little bit ..")
	time.sleep(1)
	
	ins = 'gmail.txt'
	file = open(ins, "r")
	while True:
		ins = file.readline().split('\n')[0]
		url = "https://mmo69.com/_check_live_email/api.php?email=" +ins
		headers = {
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
 "Accept-Encoding": "gzip, deflate, br",
 "Accept-Language": "ar",
 "Connection": "keep-alive",
 "Host": "mmo69.com",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
 }#JOKER @vv1ck
		
		data = {"email":ins}
		rr = requests.get(url, headers=headers, data=data)
		if rr.text.find("LIVE") >= 0:
			print (' >> The email is used [gmail] :\n ' + ins)
			print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			with open ('[$] gmail.Unavailable.txt', 'a') as x:
				x.write (ins + '\n')
				print ("")
		else:
			print(" >> Email is available [gmail] :\n" + ins)
			print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			with open ('[$] gmail.Available.txt', 'a') as x:
				x.write (ins + '\n')
				print ("")
elif joker == '3':
	slow("""
██╗  ██╗ ██████╗ ████████╗ 
██║  ██║██╔═══██╗╚══██╔══╝   [Check]
███████║██║   ██║   ██║  
██╔══██║██║   ██║   ██║  ┌┬┐ ┌─┐ ┬ ┬      
██║  ██║╚██████╔╝   ██║  │││ ├─┤ │ │      
╚═╝  ╚═╝ ╚═════╝5zr6╚═╝  ┴ ┴ ┴ ┴ ┴ ┴─┘  
               
           CHECK EMAIL (hotmail) ..
""")
	slow("wait a little bit ..")
	time.sleep(1)
	vv1ck = 'hotmail.txt'
	joker = open (vv1ck, 'r').read ().splitlines ()
	for email in joker:
		j_n_q = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
		payload = ''
		#JOKER @vv1ck
		headers = {
                        "Accept": "*/*",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                        "Connection": "close",
                        "Host": "odc.officeapps.live.com",
                        "Accept-Encoding": "gzip, deflate",
                        "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                        "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                        "uaid": "d06e1498e7ed4def9078bd46883f187b",
                        "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                    }#JOKER @vv1ck
		response = requests.get (j_n_q, data=payload, headers=headers)
		if 'MSAccount' in response.text:
			print ('>>The email is used [Hotmail] :\n ' + email)
			with open ('[$] hotmail.Unavailable.txt', 'a') as x:
				x.write (email + '\n')
			print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		elif "Neither" in response.text:
			print ('>> Email is available [Hotmail] :\n' + email)
			print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			with open ('[$] hotmail.Available.txt', 'a') as x:
				x.write (email + '\n')
				print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
				print ("")
