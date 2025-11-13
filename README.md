```markdown
# 🤖 Serverless Machine Learning Prediction API  
AWS Lambda + API Gateway + scikit-learn

A real-time ML prediction API deployed on AWS Lambda and exposed using API Gateway.  
This project demonstrates how companies deploy inference endpoints without EC2, Docker, or servers — 100% serverless.

---

## 🚀 Architecture Overview



---

## 🧩 Components in This Repository

| Folder | Description |
|--------|-------------|
| `/lambda/` | Lambda code for prediction |
| `/model/` | Trained scikit-learn `.pkl` model |
| `/test_requests/` | Sample prediction JSON |
| `/architecture/ml_api_diagram.png` | Architecture diagram |
| `/layers/` | (Optional) zipped scikit-learn Lambda Layer |

---

## 🛠️ Technologies Used

- **AWS Lambda** — Python ML inference  
- **AWS API Gateway** — REST endpoint  
- **scikit-learn** — model training + inference  
- **IAM** — secure Lambda execution role  
- **CloudWatch** — logs + debugging  

---

## 🧠 What the Lambda Does

✔ Accepts POST requests with JSON  
✔ Parses feature inputs  
✔ Loads the ML model  
✔ Runs inference  
✔ Returns probabilistic + label output  

---

## 📥 Example Request (POST /predict)

```json
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

🎯 Key Highlights

Fully serverless — no EC2, no Docker needed

Fast response time (≈100–300 ms)

Reusable Lambda Layer for sklearn

Works on AWS Free Tier

Perfect interview project for ML/AI/Data Engineering

