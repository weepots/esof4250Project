import pyotp

# verifying TOTP codes with PyOTP

# totp = pyotp.TOTP("base32secret3232")
# test = totp.now()
# print(totp.verify(test))

# generating HOTP codes with PyOTP
hotp = pyotp.HOTP("base32secret3232")
print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(1401))

# verifying HOTP codes with PyOTP
print(hotp.verify("316439", 1401))
print(hotp.verify("316439", 1402))
