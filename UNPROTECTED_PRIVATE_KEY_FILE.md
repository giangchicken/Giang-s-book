# Fix lỗi "Bad permissions" khi dùng SSH với file `.pem` trên Windows

Khi dùng SSH trên Windows với key `.pem`, bạn có thể gặp lỗi:
```bash
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @ WARNING: UNPROTECTED PRIVATE KEY FILE! @
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Permissions for 'ai-key.pem' are too open.
    It is required that your private key files are NOT accessible by others.
    This private key will be ignored.
    Load key "ai-key.pem": bad permissions
```

---

## Nguyên nhân
File `.pem` đang được gán quyền cho nhiều user/group khác ngoài **SYSTEM**, **Administrators** và **user hiện tại**.  
SSH yêu cầu file private key chỉ có quyền đọc cho **chính bạn**.

---

## Cách khắc phục

### 1. Mở PowerShell dưới quyền **Administrator**
- Ấn **Start**, gõ `PowerShell`, chọn **Run as Administrator**.

### 2. Chạy lệnh chỉnh quyền
Thay đường dẫn bằng vị trí file `.pem` của bạn:

```powershell
# Xóa quyền thừa kế
icacls "D:\FIS\GPU\ai-key.pem" /inheritance:r

# Xóa quyền của các group thừa
icacls "D:\FIS\GPU\ai-key.pem" /remove:g "Authenticated Users" "Users"

# Chỉ cho phép user hiện tại đọc file
icacls "D:\FIS\GPU\ai-key.pem" /grant:r "$($env:USERNAME):(R)"
```

### 3. Kiểm tra lại quyền
```powershell
icacls "D:\FIS\GPU\ai-key.pem"
```

### 4. Kết nối lại SSH
```bash
ssh -i D:\FIS\GPU\ai-key.pem ubuntu@<server-ip>
```

Ghi chú

- Nếu bạn copy .pem sang chỗ khác, hãy chạy lại lệnh trên để set quyền.

- Tránh lưu .pem trong thư mục chia sẻ chung (Public, Downloads).
