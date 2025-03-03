from scapy.all import *
import random

dst_ip = "173.30.0.4"

secret_message = "HELLO" 

chunks = [secret_message[i:i+2] for i in range(0, len(secret_message), 2)]

num_packets = len(chunks) + 3
secret_indexes = random.sample(range(num_packets), len(chunks))

packets = []
for i in range(num_packets):
    if i in secret_indexes:
        chunk_index = secret_indexes.index(i)
        chunk = chunks[chunk_index]

        if len(chunk) == 2:
            encoded_part = (ord(chunk[0]) << 8) + ord(chunk[1]) 
        else:
            encoded_part = ord(chunk[0])  

        ip = IP(dst=dst_ip, id=encoded_part)
        print(f"[+] Packet {i+1}: contains hidden message")
    else:
        random_id = random.randint(1000, 9000)
        ip = IP(dst=dst_ip, id=random_id)
        print(f"[-] Packet {i+1}: does not contain hidden message")

    tcp = TCP(dport=80)
    pkt = ip / tcp
    packets.append(pkt)

for pkt in packets:
    send(pkt)
    time.sleep(0.1)
