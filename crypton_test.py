__author__ = 'lus'

def main():
    from pbkdf2 import crypt

    pwhash = crypt("secret")
    print pwhash

    alleged_pw = raw_input("Enter password: ")
    print crypt(alleged_pw, pwhash)

    if pwhash == crypt(alleged_pw, pwhash):
        print "Password good"
    else:
        print "Invalid password"

    a = ''

    print a

if __name__ == "__main__":
    main()