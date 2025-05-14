# 🛠️ MLOps - Machine Learning Operations

Across industries, DevOps and DataOps have been widely adopted as methodologies to improve quality and reduce the time to market of software engineering and data initatives. With the rapid growth in Machine Learning (ML) Systems, similarity approaches need to be developed in the context of ML enginerring, which handle the unique complexities of the practical applications of ML. This is the domain of MLOps.

## ✅ What is MLOps?

**MLOps (Machine Learning Operations)** is **set of standardized processes and technology** capabilities for building, deploying and operationalizing ML systems **rapidly** and **reliable**.

**MLOps practices** can result in the following benifits over systems that do not follow **MLOps practices**.
    - Shorter development cycles, shorter time to market
    - Better collaboration between teams
    - Increased reliability, performance, scalability and security of ML systems
    - Streamlined operational and governance processes
    - Increased return on investment of ML systems

# 📘 Key words abd Definitions in MLOps

| **Key words**                        | **Full Text**                                       | **Định nghĩa** |
|-------------------------------------|-----------------------------------------------------|----------------|
| **Mlops**                            | Machine Learning Operations                         | Là một phương pháp hoặc tập hợp các thực tiễn nhằm tự động hóa và cải thiện toàn bộ vòng đời của một mô hình học máy, từ giai đoạn phát triển, triển khai đến bảo trì và giám sát. MLOps kết hợp các nguyên tắc của DevOps, Data Engineering, và Machine Learning để tối ưu hóa việc quản lý mô hình trong môi trường production. |
| **CI/CD**                            | Continuous Integration / Continuous Deployment (Delivery) | Là một tập hợp các thực tiễn và quy trình trong phát triển phần mềm nhằm tự động hóa và cải thiện việc xây dựng, kiểm thử, và triển khai ứng dụng một cách liên tục. |
| **Reproducibility**                 | Reproducibility                                     | Là khả năng giả lập cũng như khả năng tái lập một kết quả hay một lần thử nghiệm. Đây là một yêu cầu thường thấy khi phát triển một hệ thống ML, đảm bảo việc chạy suy diễn mô hình (model inference) ở production ổn định và debug quá trình phát triển model hiệu quả hơn. |
| **Versioning code, data, model**   | Versioning code, data, model                        | Là nguyên tắc đảm bảo mã nguồn (code), dữ liệu (data) và mô hình (model) được quản lý theo các phiên bản (versions). Điều này giúp dễ dàng truy vết, phát triển và đánh giá mô hình tương ứng với dữ liệu và mã nguồn cụ thể. |
| **Continuous ML training & evaluation** | Continuous Machine Learning training & evaluation | Là quy trình trong MLOps nhằm đảm bảo mô hình học máy được cải thiện và duy trì hiệu suất ổn định theo thời gian bằng cách liên tục cập nhật dữ liệu, huấn luyện lại, và đánh giá hiệu quả của mô hình. |
| **Continuous monitoring**           | Continuous monitoring                               | Là bộ các nguyên tắc đảm bảo việc theo dõi liên tục các thông số liên quan tới dữ liệu, mô hình, hạ tầng (infrastructure) để phát hiện và giải quyết lỗi kịp thời. Ví dụ: thống kê dữ liệu production, hiệu suất mô hình, số lượng request, thời gian xử lý request,... |
| **Feedback loops**                  | Feedback loops                                      | Là các vòng phản hồi giúp cải thiện liên tục chất lượng và hiệu suất mô hình bằng cách sử dụng dữ liệu và phản hồi từ môi trường sản xuất hoặc người dùng. |
| **POC**                              | Proof of Concept                                    | Là bằng chứng khái niệm hoặc minh chứng về tính khả thi của một ý tưởng, sản phẩm hoặc công nghệ. Mục tiêu là chứng minh giải pháp có thể hoạt động thực tế trước khi đầu tư triển khai quy mô lớn. |
| **Model Lifecycle**                 | Model Lifecycle                                     | Là quy trình toàn diện để quản lý các giai đoạn trong vòng đời của một mô hình học máy, từ khâu ý tưởng, phát triển, triển khai, vận hành đến khi ngừng sử dụng. Mục tiêu là đảm bảo hiệu quả, tính nhất quán và khả năng mở rộng. |

---
## MLOps lifecycle
The **MLOps lifecycle** encompasses seven integrated and iterative processes

[The MLOps lifecycle](./images/a1758973-73cb-4f12-9ba9-21beca30e9aa.jpg)

The processes can consist of the following:
    • **ML development** concerns experimenting and developing a robust and reproducible model training procedure (training pipeline code), which consists of multiple tasks from data preparation and transformation to model training and evaluation.
    • **Training operationalization** concerns automating the process of packaging, testing, and deploying repeatable and reliable training pipelines.
    • **Continuous training** concerns repeatedly executing the training pipeline in response to new data or to code
    changes, or on a schedule, potentially with new training settings.
    • **Model deployment** concerns packaging, testing, and deploying a model to a serving environment for online experimentation and production serving.
    • **Prediction serving** is about serving the model that is deployed in production for inference.
    • **Continuous monitoring** is about monitoring the effectiveness and efficiency of a deployed model.
    • **Data and model management** is a central, cross-cutting function for governing ML artifacts to support auditability, traceability, and compliance. Data and model management can also promote shareability, reusability,
    and discoverability of ML assets.

---

## 🧩 Main MLOps Components 

Dưới đây là các thành phần trong quy trình MLOps và các công nghệ được sử dụng trong từng phần:

[Core MLOps technical](./images/202999a3-bdf6-459b-a5c5-866bd20cccc0.jpg)

---

### 1. Experimentation 

---

### 2. Data Preprocessing

---

### 3. Model Training

---

### 4. Model evaluation

---

### 5. Model serving

---

### 6. Online experimentation

---

### 7. Model monitoring

---

### 8. ML pipelines

---

### 9. Dataset and feature repository

---

### 10. ML metadata and artifact tracking

--

