#This module contain the encoding and decoding algorithms of funigma

import random


def Encoder(Message):
	length=len(Message)
	if length%26==0:
		Message=Message+" "
		key=1
	else:
		key=length%26
	Secret=""	
	#print(key)
	for c in range(length):
		if 'a'<=Message[c]<='z':
			Secret=Secret+(chr(((ord(Message[c])-ord('a'))+key)%26 + ord('a')))
		elif 'A'<=Message[c]<='Z':	
			Secret=Secret+(chr(((ord(Message[c])-ord('A'))+key)%26 + ord('A')))
		elif Message[c]==' ':
			Secret=Secret+(chr(random.randint(1,10)))
		else:
			Secret=Secret+Message[c]
			
	print("Your secret is ready to send!!!!!")
	#print(Secret)
	return Secret


def Decoder(SecretMessage):
	length=len(SecretMessage)
	if length%26==0:
		Message=Message+" "
		key=1
	else:
		key=length%26
	original=""
	#print(key)
	for c in range(length):
		if 'a'<=SecretMessage[c]<='z':
			original=original+(chr((ord(SecretMessage[c])-ord('a')-key+26)%26+ ord('a')))
		elif 'A'<=SecretMessage[c]<='Z':
			original=original+(chr((ord(SecretMessage[c])-ord('A')-key+26)%26+ ord('A')))
		elif not(chr(1)<=SecretMessage[c]<=chr(10)):
			original=original+SecretMessage[c]
		else:
			original=original+" "
			
	
	print("Enjoy your origial Message!!!!!")
	#print(original)
	return original

