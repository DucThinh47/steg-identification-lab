def decode_message(ip_ids):
    decoded = ""
    for id_val in ip_ids:
        if id_val > 255:
            decoded += chr((id_val >> 8) & 0xFF) + chr(id_val & 0xFF)
        else:
            decoded += chr(id_val)
    return decoded

hidden_ids = input("Enter the IP ID list containing hidden message (separated by commas): ")
hidden_ids = [int(x.strip()) for x in hidden_ids.split(",")]

print("Hidden message:", decode_message(hidden_ids))

