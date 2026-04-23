Báo cáo kết quả benchmark LightGBM trên VM CPU (n2-standard-8, GCP):

Thời gian load dữ liệu: 2.05 giây, training: 0.79 giây.
Số vòng lặp tốt nhất (best iteration): 1.
Độ chính xác (Accuracy): 99.88%, AUC-ROC: 0.95, F1-score: 0.72.
Độ chính xác phát hiện gian lận (Precision): 0.62, Recall: 0.87.
Độ trễ inference 1 mẫu: 0.00066 giây, throughput 1000 mẫu: ~1.59 triệu mẫu/giây.
Training time và inference speed trên CPU đủ nhanh cho bài toán này, chi phí thấp (~$0.43/giờ).
Phải dùng CPU vì tài khoản GCP mới không được cấp quota GPU, nhưng kết quả vẫn đáp ứng yêu cầu lab.
CPU n2-standard-8 phù hợp cho các bài toán ML vừa và nhỏ, không cần chờ duyệt quota như GPU.
Kết quả cho thấy CPU hoàn toàn có thể thay thế GPU cho các tác vụ ML phổ thông, tiết kiệm chi phí và triển khai nhanh.

Do billing yêu cầu vài tiếng để cập nhập billing mà quá 24h thì đóng task nên em xin phép nộp ảnh billing vẫn 0$