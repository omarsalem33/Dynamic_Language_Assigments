import secrets

token = secrets.token_bytes(64)
url = secrets.token_urlsafe()
print(token)
print(url)