
# 🤖 Serverless Machine Learning Prediction API  
AWS Lambda + API Gateway + scikit-learn

A real-time ML prediction API deployed on AWS Lambda and exposed using API Gateway.  
This project demonstrates how companies deploy inference endpoints without EC2, Docker, or servers — 100% serverless.

---

## 🚀 Architecture Overview

<img width="1536" height="1024" alt="Architecture" src="https://github.com/user-attachments/assets/a7f9e79e-a3b0-46c2-a9b5-2740c02c48e0" />



---

🛠️ Technologies Used

AWS Lambda — Python serverless compute

AWS API Gateway — REST endpoint + routing

scikit-learn — ML model training & inference

AWS Lambda Layer — packaged sklearn dependencies

IAM — secure execution roles

CloudWatch Logs — monitoring, debugging, observability

---

🧠 What the Lambda Does

✔ Accepts POST requests with JSON

✔ Validates & parses features

✔ Loads scikit-learn model from local file or Lambda Layer

✔ Runs prediction logic

✔ Returns label + probability + metadata

✔ Publishes logs to CloudWatch


---

## 📥 Example Request (POST /predict)

json
{
  "feature_1": 10,
  
  "feature_2": 3,
  
  "feature_3": 1
}

## 📤 Example Response

{
  "prediction": {
    "probability": 0.9983,
    "label": 1,
    "threshold": 0.5,
    "model_version": "v1.0",
    "features_used": {
      "feature_1": 10,
      "feature_2": 3,
      "feature_3": 1
    }
  }
}

⚙️ Deployment Steps (Summary)

1️⃣ Create Lambda function
2️⃣ Upload code + model
3️⃣ (Optional) Attach Lambda Layer for sklearn
4️⃣ Create API Gateway → POST /predict route
5️⃣ Enable CORS
6️⃣ Deploy API stage (prod, $default)
7️⃣ Test via Thunder Client / Postman

🎯 Key Highlights

Fully serverless — no EC2, no Docker needed

Fast response time (≈100–300 ms)

Reusable Lambda Layer for sklearn

Works on AWS Free Tier

Perfect interview project for ML/AI/Data Engineering

📌 Use Cases

Real-time prediction APIs

Lightweight ML inference microservices

Low-latency scoring endpoints

Education & portfolio cloud projects

