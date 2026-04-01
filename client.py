import socket

# 1. ตั้งค่า Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. ระบุ IP ของ Server (ตรวจสอบให้ตรงกับที่ Server รันอยู่)
server_address = ('172.19.184.107', 10000) 

try:
    client_socket.connect(server_address)
    
    # --- แสดง Banner ทันทีเมื่อเชื่อมต่อสำเร็จ ---
    banner = client_socket.recv(4096) # รับข้อมูล Banner ขนาดใหญ่หน่อย
    print(banner.decode())

    while True:
        message = input('You: ')
        if not message.strip(): continue
        
        client_socket.sendall(message.encode())

        if message.lower().strip() == 'exit':
            print("Disconnecting...")
            break

        # รับการตอบกลับ (จาก Bot หรือ Admin)
        data = client_socket.recv(4096)
        print(data.decode())

finally:
    client_socket.close()