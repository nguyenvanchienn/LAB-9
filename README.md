# LAB9 - Selenium Automation Testing

## Giới thiệu
Repository này chứa bài thực hành về công cụ kiểm thử tự động Selenium. 
Website được chọn để kiểm thử là trang web bán hàng demo: [SauceDemo](https://www.saucedemo.com/)

## Các Test Case đã thực hiện
1. **Test Valid Login (`test_valid_login`)**: 
   - Kịch bản: Điền đúng tài khoản `standard_user` và mật khẩu `secret_sauce`.
   - Kết quả mong muốn: Đăng nhập thành công, chuyển hướng đến trang chứa sản phẩm (inventory.html) và hiển thị tiêu đề "Products".
   
2. **Test Invalid Login (`test_invalid_login`)**: 
   - Kịch bản: Điền tài khoản bị khóa `locked_out_user` và mật khẩu `secret_sauce`.
   - Kết quả mong muốn: Đăng nhập thất bại, hệ thống hiển thị thông báo lỗi "Epic sadface: Sorry, this user has been locked out."

3. **Test Add to Cart (`test_add_to_cart`)**:
   - Kịch bản: Đăng nhập thành công, click nút "Add to cart" trên sản phẩm "Sauce Labs Backpack".
   - Kết quả mong muốn: Biểu tượng giỏ hàng hiển thị số 1. Khi truy cập vào giỏ hàng, sản phẩm "Sauce Labs Backpack" hiển thị đúng ở bên trong.

## Cài đặt và Chạy thử nghiệm

### Yêu cầu
- Python 3.x
- Trình duyệt Google Chrome (hoặc đổi thành Firefox/Edge trong code nếu muốn).

### Các bước thực hiện
1. Clone repository về máy.
2. Tạo môi trường ảo (khuyến nghị) và kích hoạt nó.
3. Cài đặt các thư viện yêu cầu:
   ```bash
   pip install -r requirements.txt
   ```
4. Chạy các test case bằng lệnh `pytest`:
   ```bash
   pytest tests/test_saucedemo.py -v
   ```
   *Lưu ý: Phiên bản Selenium mới (>= 4.6.0) sẽ tự động quản lý WebDriver nên bạn không cần cài đặt ChromeDriver thủ công.*
