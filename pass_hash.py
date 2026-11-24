import hashlib, json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    salt = bytes.fromhex(data["Validation"][0]["salt"])

def encrypter(text: str) -> str:
    iterations = 600_000
    password_hash = hashlib.pbkdf2_hmac("sha256", text.encode(), salt, iterations)
    return password_hash.hex()

while True:
    try:
        text = input("> ")
        if not text:
            break
        print(encrypter(text))
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")