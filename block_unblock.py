#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:35:31 2018

@author: taimasuid
"""

#hosts_temp="hosts"
hosts_path=r"/private/etc/hosts"
#hosts_path = "C:\Windows\System32\drivers\etc\hosts"# change hosts path according to your OS
redirect = "127.0.0.1"# localhost's IP
website_list =["www.facebook.com"]

Remove_website =["www.facebook.com"]# websites That you want to Unblock



import os

with open(hosts_path, 'r+') as file:
    content = file.read()
    
file.close()
for web in Remove_website:
    if web in content:  
        os.popen('type '+ hosts_path +' | findstr /v '+web).read()
        print ("Websites are unblocked succefully")
    else:
        pass
with open(hosts_path, 'w') as file:
    for website in website_list:
        if website in content:
           file.write(redirect + " " + website + "\n") 
        else:
            # mapping hostnames to your localhost IP address
            file.write(redirect + " " + website + "\n")
            print ("Websites are blocked succefully")
  
file.close()

