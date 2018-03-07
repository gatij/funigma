#This module contain the encoding and decoding algorithms 

Secret="!!!!!"
Original=""
def Encoder(Message):
	secret=Secret+Message+Secret
	print("Your secret is ready to send!!!!!")
	#print(Secret)
	return secret


def Decoder(SecretMessage):
	original="*****"+SecretMessage+"*****"
	print("Enjoy your origial Message!!!!!")
	#print(original)
	return original

