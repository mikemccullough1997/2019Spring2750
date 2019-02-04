3) In chapter 3, we went more in depth with "strings" and several different methods that we can use in conjunction with strings and variables. These methods allow objects to be altered and converted into different objects. Furthermore, the chapter introduced three different operaters that we can apply to strings: concatenation, repitition, and indexing. Later within the text, "cryptography" and "encryption" are introduced. Simply, cryptography is the science of hiding a message that can later be translated into its intended meaning. This process of disguising and revealing a message is called encoding and decoding. These messages or encyrption code can be decoded using a "key". Lastly, three ciphers were discussed: substitution, Vignere, and transposition.


5) Three Basic String Methods:
        The Replace Method - Replaces a specified substring and replaces it with a new substring
        The Lower Method - Turns a string into all lower case characters
        The Count Method - Returns how many times a specified character or item occurs within a string


6) Three Encryption Ciphers:
        Transposition - 
        In the Transposition Cipher, essentially a plaintext is divided into two parts and scrambled. For example, you could write a string that only takes out the even characters within a plaintext, forming a new text. You could do this again for all of the odd characters and concatenate the two strings.
        
        Substitution - 
        A much more secure encryption cipher than transposition because it uses a key that only the sending and recieving end are aware of. Using a key,       substitution at its basic level can replace one letter for another. For example, we could replace the letter "m" with "a", wherever "m" exists within the text.
        
        Vignere -
        The Vignere Cipher, unlike the other two ciphers previously mentioned actually creates a key for each individual character. Each character can be mapped to a different position (row). In return, this makes unwanted decryption much more difficult. 


7) I believe the numbering on this Lab Guide is off. It goes from 1-7 and then 4-6. To avoid confusion, I'll paste the code from both algorithms that you want us to identify. 
## This algorithm uses Substitution 
def encrypt(plainText ,key):  
  alphabet = "abcdefghijklmnopqrstuvwxyz"  
  plainText = plainText.lower ()  
  cipherText = ""  

  for ch in plainText:  
      idx = alphabet.find(ch)  
      cipherText = cipherText + key[idx]  
  return cipherText 


4) 
## This algorithm uses Transposition
def scramble2Encrypt(plainText):  
  evenChars = ""  
  oddChars = ""  
  charCount = 0  

  for ch in plainText:  
      if charCount % 2 == 0:  
          evenChars = evenChars + ch  
      else:  
          oddChars = oddChars + ch  
    charCount = charCount + 1  
  cipherText = oddChars + evenChars  
  return cipherText  