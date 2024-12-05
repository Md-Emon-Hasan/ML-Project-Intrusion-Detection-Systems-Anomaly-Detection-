# 🚨 Network Intruision Detection System

![Screenshot 2024-12-05 at 20-27-58 Anomaly Detection](https://github.com/user-attachments/assets/d79efb1f-9d6f-4470-af40-6005423731c4)

## Table of Contents
1. [Problem Statement](#problem-statement)  
2. [Objective](#objective)  
3. [Technologies Used](#technologies-used)  
4. [System Architecture](#system-architecture)  
5. [Model Design and Training](#model-design-and-training)  
6. [Performance Metrics](#Performance-Metrics)  
7. [Conclusion](#conclusion)  
8. [Future Work](#Future-Work)  
9. [References](#References)  
10. [Contact Information](#Contact-Information)  

---

## 1. Problem Statement

Network security has become a critical concern due to the increased usage of computer networks and applications, which has led to a rise in cyberattacks. Intrusion Detection Systems (IDS) are designed to detect and identify malicious activities within a network. These systems play a pivotal role in protecting network infrastructures from attacks such as unauthorized access, malware, and denial-of-service (DoS) attacks. The aim of this project is to build a machine learning-based IDS using a Support Vector Machine (SVM) classifier that can identify potential attacks in network traffic. This model will be trained on a publicly available dataset and deployed to classify whether a given network packet represents a benign or malicious activity.

---

## 2. Objective

The primary objective of this project is to develop a machine learning-based **Intrusion Detection System (IDS)** that can:
1. **Identify malicious activities** within network traffic by classifying packets as either **benign** or **malicious** (attack).
2. Provide an efficient, **scalable solution** for real-time intrusion detection.
3. Leverage **ensemble learning** and **hybrid models** to improve the accuracy and robustness of the system.
4. Be **deployed in real-world network environments**, capable of detecting various types of network attacks.

---

## 3. Technologies Used

| **Category**            | **Technology**                  | **Purpose**                          |
|-------------------------|----------------------------------|--------------------------------------|
| **Programming Language** | Python                          | Core implementation                  |
| **Machine Learning**     | Scikit-learn, TensorFlow         | Model development and training       |
| **Web Framework**        | Flask                           | Backend and API                      |
| **Data Processing**      | Pandas, NumPy                   | Dataset manipulation and preprocessing|
| **Model Evaluation**     | Scikit-learn metrics            | Performance evaluation               |
| **Deployment**           | Docker                     | Containerization and cloud hosting   |
| **Frontend**             | HTML, CSS, Bootstrap            | User interface design (optional)     |

---

## 4. System Architecture

The architecture of the Intrusion Detection System consists of three main components:

1. **Frontend (User Interface)**:  
   - Built using **HTML**, **CSS**, and **Bootstrap** to provide a responsive, user-friendly interface.
   - Allows users to interact with the system and input network traffic data for classification (optional).

2. **Backend (Flask Application)**:  
   - **Flask** serves the machine learning model and handles incoming network traffic data.
   - The model performs classification, identifying whether the data represents benign or malicious activity.

3. **Model**:  
   - A **Logistic Regression** classifier combined with hybrid ensemble learning techniques.
   - The model is trained on historical network traffic data and deployed for real-time prediction.

**Architecture Diagram**:  
```
[User Input] -> [Frontend (Flask)] -> [Preprocessing] -> [Model Inference] -> [Result Display]
```

---

## 5. Model Design and Training

#### **Model Architecture**:
- **Logistic Regression**: The primary classifier for detecting malicious traffic.
- **Hybrid Ensemble Learning**: Combination of multiple models, such as Decision Trees, and KNN to improve performance.

#### **Training Data Split**:
| **Dataset Split** | **Percentage** |
|-------------------|----------------|
| Training          | 75%            |
| Testing           | 25%            |

The model is trained using **Scikit-learn** with performance metrics evaluated through confusion matrix and classification report.

---

## 6. Performance Metrics

The model's performance is evaluated using various metrics to ensure reliability and robustness:

| **Metric**            | **Value**                           |
|------------------------|-------------------------------------|
| **Accuracy**           | 0.9947                              |
| **Confusion Matrix**   | [[2918, 11], [22, 3347]]            |
| **Precision (Class 0)**| 0.99                                |
| **Recall (Class 0)**   | 1.00                                |
| **F1-Score (Class 0)** | 0.99                                |
| **Precision (Class 1)**| 1.00                                |
| **Recall (Class 1)**   | 0.99                                |
| **F1-Score (Class 1)** | 1.00                                |
| **Support**            | [2929 (Class 0), 3369 (Class 1)]    |

#### **Classification Report on Test Data**:
```plaintext
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      2929
           1       1.00      0.99      1.00      3369

    accuracy                           0.99      6298
   macro avg       0.99      0.99      0.99      6298
weighted avg       0.99      0.99      0.99      6298
```

#### **Confusion Matrix**:
```plaintext
[[2918   11]
 [  22 3347]]
 
```

The high **accuracy** (99.47%) and strong **precision**, **recall**, and **F1-scores** for both classes demonstrate the model's ability to effectively detect and classify malicious network traffic with minimal false positives and false negatives.

```python
test_accuracy = metrics.accuracy_score(Y_test, test_predictions)
test_classification_report = metrics.classification_report(Y_test, test_predictions)
```

---

## 7. Conclusion

The project demonstrates the effectiveness of machine learning models in detecting network intrusions. Through the use of **LogisticRegression** and **ensemble techniques**, the IDS can accurately classify malicious network traffic. The system can be expanded and optimized for real-world network environments and incorporated into enterprise-level security infrastructures.

---

## 8. Future Work

Future improvements to this system may include:
1. **Real-Time Deployment**: Implementing the model in a real-time IDS for continuous monitoring.
2. **Additional Features**: Including more network-specific features (e.g., packet size, connection duration) for better prediction accuracy.
3. **Hyperparameter Tuning**: Implementing grid search or random search for optimized model performance.

---

## 9. References

- Kaggle: [Network Intrusion Detection Dataset](https://www.kaggle.com/datasets/)
- Scikit-learn Documentation: [https://scikit-learn.org/](https://scikit-learn.org/)
- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- TensorFlow Documentation: [https://www.tensorflow.org/](https://www.tensorflow.org/)

---

## 10. Contact Information
- **Email:** [iconicemon01@gmail.com](mailto:iconicemon01@gmail.com)  
- **WhatsApp:** [+8801834363533](https://wa.me/8801834363533)  
- **GitHub:** [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)  
- **LinkedIn:** [Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan)  
- **Facebook:** [Md Emon Hasan](https://www.facebook.com/mdemon.hasan2001/)  

---
