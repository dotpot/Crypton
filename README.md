#Crypton
PBKDF2 implementation in pyton. Original package is [here](http://pypi.python.org/pypi/pbkdf2)

##Usage

	from pbkdf2 import crypt

    pwhash = crypt("secret")
    print pwhash

    alleged_pw = raw_input("Enter password: ")
    print crypt(alleged_pw, pwhash)

    if pwhash == crypt(alleged_pw, pwhash):
        print "Password good"
    else:
        print "Invalid password"
        
        


### Please feel free to improve it if you like :)

![image](http://img193.imageshack.us/img193/5605/tumblrlznr805hcb1r3zat8.png)