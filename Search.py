import secrets

print(secrets.token_bytes(64))
print(secrets.token_hex(32))

passwordResetLink = "demo.com/customer/eric/reset="
passwordResetLink += secrets.token_urlsafe(32)
print(passwordResetLink)