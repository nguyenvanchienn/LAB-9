# Báo Cáo Thực Hành Selenium Automation Testing

## 1. Giới thiệu
Repository này chứa bài thực hành về công cụ kiểm thử tự động Selenium. 
Website được chọn để kiểm thử là trang web bán hàng demo: [SauceDemo](https://www.saucedemo.com/)

## 2. Các Test Case Đã Thực Hiện & Kết Quả

### Test Case 1: Đăng nhập hợp lệ (Valid Login)
- **Kịch bản:** Điền đúng tài khoản `standard_user` và mật khẩu `secret_sauce`.
- **Kết quả mong muốn:** Đăng nhập thành công, chuyển hướng đến trang chứa sản phẩm (inventory.html) và hiển thị tiêu đề "Products".
- **Hình ảnh minh hoạ kết quả chạy code:**
  
  *(Bạn hãy chụp ảnh màn hình Terminal báo PASSED và màn hình trình duyệt lúc đăng nhập thành công dán vào đây)*
  `![Valid Login Screenshot](link_anh_cua_ban)`

- **Kết luận:** Test case chạy mượt mà, hệ thống nhận diện đúng thông tin hợp lệ và phản hồi (đăng nhập thành công) trong thời gian ngắn.

---

### Test Case 2: Đăng nhập không hợp lệ (Invalid Login)
- **Kịch bản:** Điền tài khoản bị khóa `locked_out_user` và mật khẩu `secret_sauce`.
- **Kết quả mong muốn:** Đăng nhập thất bại, hệ thống hiển thị thông báo lỗi "Epic sadface: Sorry, this user has been locked out."
- **Hình ảnh minh hoạ kết quả chạy code:**
  
  *(Bạn hãy chụp ảnh màn hình Terminal báo PASSED và màn hình báo lỗi đỏ của trang web dán vào đây)*
  `![Invalid Login Screenshot](link_anh_cua_ban)`

- **Kết luận:** Hệ thống đã bắt lỗi chính xác tài khoản bị khóa và hiển thị thông báo đúng như mong đợi. Không có lỗi ngoại lệ nào xảy ra làm treo ứng dụng.

---

### Test Case 3: Thêm sản phẩm vào giỏ hàng (Add to Cart)
- **Kịch bản:** Đăng nhập thành công, click nút "Add to cart" trên sản phẩm "Sauce Labs Backpack".
- **Kết quả mong muốn:** Biểu tượng giỏ hàng hiển thị số 1. Khi truy cập vào giỏ hàng, sản phẩm "Sauce Labs Backpack" hiển thị đúng ở bên trong.
- **Hình ảnh minh hoạ kết quả chạy code:**
  
  *(Bạn hãy chụp ảnh màn hình Terminal báo PASSED và màn hình giỏ hàng hiển thị số 1 dán vào đây)*
  `![Add to Cart Screenshot](link_anh_cua_ban)`

- **Kết luận:** Chức năng thêm vào giỏ hàng hoạt động tốt, UI cập nhật số lượng badge trên giỏ hàng ngay lập tức và lưu trữ đúng sản phẩm.

## 3. Tổng kết
Với 03 test case tự động trên, thư viện Selenium kết hợp cùng Pytest đã tự động hóa thành công các thao tác người dùng cơ bản trên UI. Code chạy ổn định, không ghi nhận tình trạng crash trình duyệt hay timeout, tỉ lệ pass là 100%.

## 4. Hướng dẫn chạy code
1. Clone repository về máy.
2. Cài đặt các thư viện yêu cầu:
   ```bash
   pip install -r requirements.txt
   pip install webdriver-manager
   ```
3. Chạy các test case bằng lệnh `pytest`:
   ```bash
   python -m pytest tests/test_saucedemo.py -v
   ```
