#!/usr/bin/env python3

"""
Created on April 20th, 2018
@author: andres.fernandez

"""

import sys
import os
import subprocess
import time
import logging

script_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(script_dir, "../lib"))

import testlogging

logger = testlogging.get_logger(script_dir + '/../logs/test-hash-app.log', logging.INFO, True)

logging.info("Platform: " + sys.platform)

os.environ["PORT"] = "8088"

print(os.getcwd())

hash_app_process = 0

os_extension_name = "darwin"

try:
    hash_app_process = subprocess.Popen(["..//resources//broken-hashserve_" + os_extension_name, ""])
except subprocess.CalledProcessError:
    print("There was an error starting the process")

print("Waiting for 30 seconds before closing process")

time.sleep(30)

hash_app_process.terminate()

#returnCode = 0

#try:
#    returnCode = subprocess.check_output(["..//resources//broken-hashserve_darwin", ""], 0)
#except subprocess.CalledProcessError:
#    print("There was an error running the application")

#print("What is the return code: " + returnCode)






