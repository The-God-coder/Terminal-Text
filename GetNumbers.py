import sys, getopt

class CancelProgram(Exception):
   pass

def GetNumbers(argv):
   print("THIS PROGRAM WILL ONLY WORK WITH VERIZON PHONE NUMBERS")
   print("SUPPORT FOR OTHER NUMBER WILL BE COMING SOON\n\n\n")
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hp:m:",["phoneNumber=","message="])
   except getopt.GetoptError:
      print ('USAGE: ./TextPhone.sh -p <Phone Number> -m <Message surrounded by quotes>')
      sys.exit(2)
   if len(sys.argv) == 1:
         print ('USAGE: ./TextPhone.sh -p <Phone Number> -m <Message surrounded by quotes>')
         sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('USAGE: ./TextPhone.sh -p <Phone Number> -m <Message surrounded by quotes>')
         sys.exit()
      elif opt in ("-p", "--phoneNumber"):
         phoneNumber = arg
      elif opt in ("-m", "--message"):
         message = arg
   
   try:
      print ('Phone Number is', phoneNumber)
      print (f'Message is "{message}"')
      if input("Are you sure that you want to send this? y/n  ") == "n": raise CancelProgram
   except CancelProgram: sys.exit(1)
   except: print("\nERROR: ALL VALUES NOT PROVIDED \nUSAGE: print ('./TextPhone.sh -p <Phone Number> -m <Message surrounded by quotes>')")

   return [phoneNumber, message]


if __name__ == "__main__":
   GetNumbers(sys.argv[1:])