# steg-identification-lab

## Nội dung

- [Giới thiệu](https://github.com/DucThinh47/steg-identification-lab/tree/main#gi%E1%BB%9Bi-thi%E1%BB%87u)

- [Hướng dẫn thực hành lab](https://github.com/DucThinh47/steg-identification-lab/tree/main#h%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-th%E1%BB%B1c-h%C3%A0nh-lab)

- [Thiết kế xây dựng lab](https://github.com/DucThinh47/steg-identification-lab/tree/main#thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-lab)

- [Thử nghiệm lab](https://github.com/DucThinh47/steg-identification-lab/tree/main#demo-lab)

### Giới thiệu

**Tổng quan**

Bài lab này giúp tìm hiểu một kỹ thuật giấu tin trong mạng dựa trên trường Identification (ID) của gói tin IPv4. Đây là một phương pháp giấu tin trong header giao thức mà không làm thay đổi nội dung của gói tin, giúp che giấu dữ liệu một cách khó phát hiện hơn.

**Nguyên lý giấu tin**

- Trường IP ID (Identification) trong header IPv4 có độ dài 16 bit, thường được sử dụng để nhận diện và tái lắp ráp các gói tin bị phân mảnh. 

- Trong kỹ thuật giấu tin này, thay vì sử dụng IP ID một cách ngẫu nhiên hoặc tuần tự như thông thường, kẻ tấn công sẽ mã hóa thông điệp cần giấu vào giá trị IP ID của gói tin trước khi gửi đi.

- Cụ thể, mỗi ký tự trong thông điệp được chuyển thành giá trị số ASCII, sau đó nhóm thành từng cặp (mỗi cặp 2 ký tự sẽ tạo thành một số 16-bit) và gán vào IP ID của gói tin. 

**Mục tiêu của bài lab**

- Hiểu được cách giấu tin trong header gói tin IPv4 bằng cách kiểm soát trường Identification

- Hiểu cách hoạt động của Scapy để tạo và gửi gói tin chứa thông điệp bí mật

- Sử dụng Wireshark để phân tích lưu lượng mạng, nhận diện và tách thông tin giấu tin

### Hướng dẫn thực hành lab

**Tải và khởi động bài thực hành**
    
Sử dụng lệnh để tải bài thực hành: 
        
    imodule https://github.com/DucThinh47/steg-identification-lab/raw/refs/heads/main/imodule-steg-identification.tar
    
Khởi động bài thực hành: 

    labtainer -r steg-identification

**Task 1: Gửi gói tin**

- Bên máy attacker, chạy lệnh để tiến hành gửi gói tin: 

        python3 attacker.py

- Bên máy monitor, sử dụng lệnh sau để khởi chạy wireshark: 

        wireshark &

- Kết quả mong đợi: Quan sát wireshark bên máy monitor, xác nhận gửi gói tin thành công

**Task 2: Tìm thông điệp giấu trong gói tin**

- Bên máy monitor, chạy lệnh:

        python3 monitor.py

- Quan sát trong wireshark, tìm ra các gói nào là gói có giấu tin bên trong, sau đó nhập giá trị IP ID của các gói tin này.

- Tìm ra thông điệp ẩn là "HELLO"

- Bên máy attacker, chạy lệnh: 

        nano attacker.py

- Sửa giá trị secret_message thành "PTIT< Mã sinh viên >". 

- Gửi lại gói tin: 

        python3 attacker.py

- Bên máy monitor, chạy lệnh:

        python3 monitor.py

- Quan sát wireshark, tìm IP ID và ghép lại thành nội dung secret_message. 

**Kiểm tra kết quả**

    checkwork

**Kết thúc bài lab**

    stoplab
### Thiết kế xây dựng lab

1. **Thiết kế bài thực hành**

Cấu hình docker gồm có:

- Container attacker: 

    - Địa chỉ IP: 173.30.0.3

- •	Container monitor: 

    - Địa chỉ IP: 173.30.0.4

Trong bài lab này, hệ thống cần ghi nhận các thao tác, sự kiện được mô tả và cấu hình như bảng:

| Result Tag  | Container | File              | Field Type | Field ID             | Timestamp Type |
|-------------|-----------|-------------------|------------|----------------------|----------------|
| steg_sent   | attacker  | .bash_history     | CONTAINS   | python3 attacker.py  | File           |
| hidden_mess | monitor   | monitor.py.stdout | CONTAINS   | Hidden message: PTIT | File           |

- *steg_sent*: Xác nhận việc gửi gói tin từ máy attacker đến máy monitor

- *hidden_mess*: Tìm ra thông điệp được giấu trong các gói tin  

2. **Cài đặt và cấu hình các máy ảo**

Giao diện Labedit của bài lab: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image.png?raw=true)

Checkwork của bài lab: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image1.png?raw=true)

Cấu trúc thư mục bài lab: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image2.png?raw=true)

Thư mục attacker: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image3.png?raw=true)

Thư mục monitor: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image4.png?raw=true)

Thư mục Dockerfiles:

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image5.png?raw=true)

Nội dung dockerfile máy attacker: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image6.png?raw=true)

Nội dung dockerfile của máy monitor: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image7.png?raw=true)

3. **Tích hợp và triển khai**

Dockerhub: https://hub.docker.com/u/ducthinhdt472003

Các container của bài lab được lưu trên Dockerhub:

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image8.png?raw=true)

Github: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image9.png?raw=true)

### Thử nghiệm lab

Tải bài lab: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image10.png?raw=true)

Khởi động bài lab: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image11.png?raw=true)

Tiến hành gửi gói tin từ máy attacker:

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image12.png?raw=true)

Quan sát wireshark bên máy monitor: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image13.png?raw=true)

Bên máy monitor, thực thi monitor.py: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image14.png?raw=true)

Tìm các gói có tin giấu và nhập giá trị IP ID của gói: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image15.png?raw=true)

Bên máy attacker, thay đổi secret_message thành "PTIT181":

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image16.png?raw=true)

Gửi lại gói tin: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image17.png?raw=true)

Bên máy monitor, thực hiện tương tự để tìm ra thông điệp: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image18.png?raw=true)

Checkwork: 

![img](https://github.com/DucThinh47/steg-identification-lab/blob/main/images/image19.png?raw=true)





