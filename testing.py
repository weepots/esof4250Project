import pyotp

# verifying TOTP codes with PyOTP

totp = pyotp.TOTP("base32secret3232")
test = totp.now()
print(totp.verify(test))
