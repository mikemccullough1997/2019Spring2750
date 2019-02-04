## I'll be using Substitution in the following algorithm
messageOne = "123456789"
key = "627193580"
def encryptThis(plainText, key):
		message = "123456789"
		cipherText = ""
		for char in plainText:
			idx = message.find(char)
		cipherText = cipherText + key[idx]
		return cipherText
cipherText = encryptThis("123456789", key)
print(cipherText)

## It continues to output a 0 and I'm not sure why...
## My goal is to create an algorithm that encrypts a string of numbers
## For instance, if a company wanted to hide a specific number





