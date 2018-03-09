# A test for using Funigma mechanism
import funigma

testMessage="Return a randomly selected element from range(start, stop, step)." 
secretMessage=funigma.Encoder(testMessage)
print("encrypted message: "+secretMessage)

originalMessage=funigma.Decoder(secretMessage)
print("decrypted message: "+originalMessage)
