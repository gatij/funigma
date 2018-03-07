# A test for using Funigma mechanism
import funigma

testMessage="test message"
secretMessage=funigma.Encoder(testMessage)
print("encrypted message: "+secretMessage)

originalMessage=funigma.Decoder(secretMessage)
print("decrypted message: "+originalMessage)
