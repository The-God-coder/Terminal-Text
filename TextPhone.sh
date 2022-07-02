#! /bin/python3
import sys

from GetNumbers import GetNumbers
from SendEmail import sendEmail

info = GetNumbers(sys.argv[1:])

sendEmail(info[0], info[1], input("Email:   "), input("Password:   "))

