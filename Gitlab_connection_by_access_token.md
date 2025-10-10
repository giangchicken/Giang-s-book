# 🚀 Hướng Dẫn Kết Nối GitLab Bằng Access Token

Tài liệu này hướng dẫn cách **clone**, **push**, **pull**, và **làm việc với branch cụ thể** từ GitLab bằng **Access Token** thay vì mật khẩu.  
Phù hợp khi bạn bị lỗi `HTTP Basic: Access denied` hoặc `403 Forbidden`.

---

## 🧩 1. Tạo Access Token trên GitLab

1. Truy cập: [https://gitlab.com/-/user_settings/personal_access_tokens](https://gitlab.com/-/user_settings/personal_access_tokens)
2. Chọn:
   - **Token name:** ví dụ `my-dev-token`
   - **Expiration date:** chọn thời hạn mong muốn
   - **Scopes:** ✅ tick **read_repository** và **write_repository**
3. Nhấn **Create personal access token**
4. Sao chép token hiển thị (ví dụ `glpat-xxxxxxxxxxxxxxxxxxxx`)

---

## 🧭 2. Clone Repository Bằng Token

### 🔹 Cú pháp chung:
```bash
git clone https://oauth2:<ACCESS_TOKEN>@gitlab.com/<username>/<repo>.git
```

## 🌿 3. Clone Theo Branch Cụ Thể

Nếu bạn chỉ muốn clone một branch nhất định (ví dụ `develop`):
```bash
    git clone -b develop https://oauth2:ACCESS_TOKEN@gitlab.com/giangchicken/biznext-chatbot.git
```

## 🪄 4. Thiết Lập Remote Cho Repo Đã Tồn Tại

Nếu bạn đã có sẵn project local và chỉ muốn kết nối với GitLab, chạy:

```bash
git remote remove origin
git remote add origin https://oauth2:<ACCESS_TOKEN>@gitlab.com/<username>/<repo>.git
git branch -M develop
git push -u origin develop
```

## 🧱 5. Tạo Và Push Branch Mới
Tạo branch mới từ branch hiện tại:
```bash
git checkout -b feature/ai-service
```

Push branch mới lên GitLab:
```bash
git push -u origin feature/ai-service
```

## 🧹 6. Một Số Lệnh Git Cơ Bản
Lệnh	Mô tả
git status	Kiểm tra trạng thái thay đổi
git add .	Thêm toàn bộ thay đổi
git commit -m "Ghi chú"	Tạo commit
git push	Đẩy code lên remote
git pull	Lấy code mới nhất về
git branch	Xem danh sách branch
git checkout <branch>	Chuyển sang branch khác
git reset --soft HEAD~1 Xóa lệnh commit


## ⚠️ 7. Lưu Ý Bảo Mật

Không commit token vào repo (nên lưu token trong file .env hoặc Git Credential Manager)

Token hết hạn → bạn cần tạo lại token mới

Có thể kiểm tra token bằng:
```bash
git ls-remote https://oauth2:<ACCESS_TOKEN>@gitlab.com/<username>/<repo>.git
```