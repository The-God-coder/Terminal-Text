
# Terminal Text

Terminal Text is a open source way of sending SMS text messages through your terminal. It uses SMS gateways (Currently Verizon but others are being added) to send text message using a Google's Gmail to send the request to the gateway.

We currently support Verizon SMS gateways but support for other carriers will be added soon.

The current usage for the command is 

 ./TerminalText.sh -p (Phone Number) -m (Message surrounded by quotes)
 
 which is then followed by a prompt for your email and password
 Please note that google has stopped third party apps from using your direct password so you will have to make an app password for this program
 
 ### The Email and password can also be hard-coded into the file by replacing
 
 sendEmail(info[0], info[1], **input("Email:   ")**, **input("Password:   ")**) in TextPhone.sh on Line 8
 
 Where **input("Email:   ")** Will Become a string so it will look like "(Email)" 
 And **input("Password:   ")** Will Become a string so it will look like "(Password)"
 In the end your Line 8 should look like
 
 sendEmail(info[0], info[1], **"(Email)"**, **"(Password)"**) in TextPhone.sh on Line 8
 
 **NOTE: THIS PROGRAM WILL ONLY WORK WITH VERIZON PHONE NUMBERS AND GOOGLE EMAIL ADRESSES, SUPPORT FOR OTHER CARRIERS AND ADRESSES IS COMING SOON**
 
 If you like my work then me support at
 
 # [!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/GodCoder)

