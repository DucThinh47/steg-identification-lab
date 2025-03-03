# steg-identification-lab

## Nội dung

- [Giới thiệu]()

- [Hướng dẫn thực hành lab]()

- [Thiết kế xây dựng lab]()

- [Thử nghiệm lab]()

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

1. Tải bài thực hành

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

![img](0)

Checkwork của bài lab: 

![img](1)

Cấu trúc thư mục bài lab: 

![img](2)

Thư mục attacker: 

![img](3)

Thư mục monitor: 

![img](4)

Dockerfiles:

![img](5)

Nội dung dockerfile máy attacker: 

![img](6)

Nội dung dockerfile của máy monitor: 

![img](7)

3. **Tích hợp và triển khai**

Dockerhub: https://hub.docker.com/repositories/ducthinhdt472003

Các container của bài lab được lưu trên Dockerhub:

![img](8)

Github: 

### Demo lab

