What is EC2?

EC2 **viết tắt của: Amazon Elastic Compute Cloud** là một service cung cấp tài nguyên server ảo theo yêu cầu.

![#](https://docs.aws.amazon.com/images/AWSEC2/latest/UserGuide/images/ec2-instances.png)

| EC2  | PC/Laptop |
|------|-----------|
| RAM  |    RAM    |
| CPU  |    CPU    |
| GPU  |    GPU    |
| EBS Volume(s)  |    SSD, HDD, USB    |
| VPC/Subnet  |    LAN    |
| Snapshot  |    Ghost    |

EC2 thuộc về layer nào?
- EC2 là một máy chủ ảo chạy trên Hypervisor của AWS.
- Người dùng chỉ có thể quản lý EC2 từ tầng OS trở lên của 1 EC2 Instance.
- EC2 instance hoạt động như 1 máy chủ độc lập và không thể access nếu như không có quyền.

Một số khái niệm cơ bản của EC2
- AMI: **Amazon Machine Image**. Giống như 1 file ISO/Ghost chứa toàn bộ thông tin của hệ điều hành. EC2 được khởi động lên từ 1 AMU tương tự như việc cài Win lần đầu cho PC/Laptop.
- EBS (Elastic Block Storage) Volume: Ổ cứng ảo được cấp phát bởi Amazon. Chỉ có thể đọc được dữ liệu khi được gắn vào 1 Instance.
- Snapshot: Ảnh chụp của 1 EBS Volume tại 1 thời điểm. Có thể sử dụng để phục hồi dữ liệu khi có sự cố.
- Instance: 1 máy chủ ảo được cấp phát tài nguyên CPU, RAM, GPU,... tùy theo dòng instance mà sẽ có một số giới hạn nhất định.
- Key pairs: Khóa bảo mật, AWS lưu trữ public key và chúng ta lưu trữ private key.
- Security groups: Vitual Firewall cho phép chúng ta chỉ định các protocols, ports và dải IP mà chúng ta có thể tiếp cận bằng Instance hoặc tiếp cận đến Instance.
- VPC: **Virtual private cloud** là một mạng ảo có logic riêng biệt và an toàn dành riêng bên trong hạ tầng cloud.

![#](https://cdn.prod.website-files.com/63403546259748be2de2e194/650ab55d4e1aa07a9bc26220_f_nXQKWGtk-uNGiWq0v4I0_CJUSxbWs-k3GeejybrBbbEmHm7B6ok-AodZYHgu6D9-ZslcDxkr6bpsrgbR8pYwQyaAUnB-fOHWhVdh3j3l_YHlJobUPP7z84X2kQsh528juycfggQUGSaTkonTB5zRg.gif)


EC2 Use Cases

- **Hosting environments**: Một trong những ứng dụng quan trọng nhất của EC2 là lưu trữ nhiều ứng dụng, phần mềm và websites trên cloud. Users có thể lưu trữ trò chơi trên đó, bật/tắt khi cần và có khả năng scale nhanh chóng khi có nhiều clients.
- **Development and test environments**: Bởi vì có khả năng large scale mạnh mẽ, EC2 có thể dùng để phát triển và thử nghiệm trên quy mô lớn.
- **Backup and disaster recovery**: Các công tu có thẻ tận dụng EC2 như một phương tiện để thực hiện phục hồi sau thảm họa.

EC2 Pricing

EC2 Instance tính tiền dựa trên thời gian chạy và kích thước của instance. 


---

Load Balance

Nếu hệ thống có nhiều hơn 1 thành phần, cần có 1 cơ chế để phân phối request từ cliet đến các thành phần ở backend => Sự ra đời của Load Balancer.
AWS cho phép dễ dàng setup load balancer tới nhiều target nằm ở các Avaibility Zone khác nhau.

**single point of failure**: Khi một sự cố xảy ra ở một thành phần nào đó có thể dẫn đến hệ thống bị dừng hoạt động, không thể phục vụ người dùng ta gọi đó là single point of failure.

---

Identity and Access Management (IAM)




