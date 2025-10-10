# 🧭 Hướng Dẫn Kết Nối Server Qua Tailscale

Tailscale giúp bạn tạo **VPN riêng** giữa máy cá nhân và server mà **không cần mở port SSH hay IP tĩnh**.  
Sau khi setup xong, bạn có thể SSH bằng **tên Tailscale** thay vì IP thật.

---

## ⚙️ 1. Đăng ký & Cài đặt Tailscale trên máy cá nhân

### ✅ Truy cập trang chủ
- https://tailscale.com/
- Đăng ký bằng **Google, GitHub, hoặc Microsoft account**.

### ✅ Cài Tailscale trên máy local
**Windows / macOS:**
- Download tại [https://tailscale.com/download](https://tailscale.com/download)
- Cài đặt và **Đăng nhập (Sign in)**.

**Linux (local):**
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

Sau lệnh trên, trình duyệt sẽ mở ra để bạn đăng nhập và kết nối thiết bị.

## 🖥️ 2. Cài đặt Tailscale trên server Linux (VD: Ubuntu, Debian, CentOS...)

SSH vào server (bằng IP tạm thời hoặc console của VPS provider).

### Cài đặt Tailscale
```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

### Kết nối server vào mạng Tailscale
```bash
sudo tailscale up
```

### ➡️ Hệ thống sẽ in ra 1 URL, ví dụ:
```bash
To authenticate, visit:
https://login.tailscale.com/a/1234567890abcdef
```

Copy link này, mở trên trình duyệt máy bạn, đăng nhập cùng tài khoản đã tạo ở bước 1.

Sau khi xác thực xong, server sẽ tự động hiển thị trong dashboard Tailscale:
👉 https://login.tailscale.com/admin/machines

## 🔍 3. Kiểm tra kết nối
Xem danh sách thiết bị

Trên cả máy local và server:

tailscale status


Kết quả ví dụ:
```bash
100.101.102.103   ubuntu-server   linux   active; relay "fra"
100.104.105.106   my-laptop       windows active; direct
```
Ping thử

Từ máy local:

```bash
ping 100.101.102.103
```

## 🔑 4. SSH qua Tailscale

SSH bằng IP nội bộ Tailscale:
```bash
ssh ubuntu@100.101.102.103
```

⚠️ Yêu cầu server đã bật SSH service (sudo systemctl enable --now ssh).

Dùng .pem file (nếu bạn có key riêng)
```bash

ssh -i mykey.pem ubuntu@100.101.102.103
```

Lưu ý:

File .pem này chỉ là cách xác thực SSH, Tailscale chỉ lo phần mạng nội bộ.

Bạn có thể dùng key .pem song song với Tailscale để đảm bảo an toàn.

🧰 6. Một số lệnh hữu ích
Mục đích	Lệnh
Kiểm tra IP nội bộ Tailscale	tailscale ip -4
Kiểm tra trạng thái	tailscale status
Ngắt kết nối	sudo tailscale down
Cập nhật Tailscale	sudo apt update && sudo apt install tailscale -y
Chạy tự động khi reboot	sudo systemctl enable tailscaled

🚀 7. Mở rộng (nếu cần)

- Kết nối nhiều server ⇒ cài Tailscale cho tất cả.

- Chia sẻ VPN cho người khác ⇒ vào dashboard → “Share node”.

- Chạy dịch vụ qua Tailscale IP (ví dụ: API, DB) ⇒ dùng IP nội bộ thay vì IP công khai.