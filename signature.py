import hashlib

def generate_signature(phone_number):
    if phone_number.startswith("0"):
        phone_number = phone_number[1:]
    raw = f"v3/user/signup/phone+62{phone_number}IDR952Smyxue8SUDjoneqH3"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

start_end = "81234560000-81234560100"
start, end = start_end.split("-")
start_int = int(start)
end_int = int(end)

for i in range(start_int, end_int + 1):
    phone = f"0{i}"
    print(generate_signature(phone))
