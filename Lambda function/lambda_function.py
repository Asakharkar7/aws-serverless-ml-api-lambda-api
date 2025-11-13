import json
import math
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ----- "Model" section (hardcoded logistic regression for demo) -----
# y = sigmoid(b0 + b1*x1 + b2*x2 + b3*x3)
COEFFS = {
    "b0": -2.15,   # intercept
    "b1":  0.85,   # weight for feature_1  (e.g., amount)
    "b2": -0.40,   # weight for feature_2  (e.g., days_since_last_txn)
    "b3":  1.25    # weight for feature_3  (e.g., is_priority_customer)
}
FEATURE_NAMES = ["feature_1", "feature_2", "feature_3"]

def sigmoid(z: float) -> float:
    # Stable sigmoid
    if z >= 0:
        ez = math.exp(-z)
        return 1 / (1 + ez)
    else:
        ez = math.exp(z)
        return ez / (1 + ez)

def score(features: dict) -> float:
    # Extract features with defaults (robust to missing)
    f1 = float(features.get("feature_1", 0.0))
    f2 = float(features.get("feature_2", 0.0))
    f3 = float(features.get("feature_3", 0.0))
    z = COEFFS["b0"] + COEFFS["b1"]*f1 + COEFFS["b2"]*f2 + COEFFS["b3"]*f3
    return sigmoid(z)

def make_response(status_code: int, body: dict, cors: bool = True) -> dict:
    headers = {"Content-Type": "application/json"}
    if cors:
        headers.update({
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Access-Control-Allow-Methods": "OPTIONS,POST"
        })
    return {
        "statusCode": status_code,
        "headers": headers,
        "body": json.dumps(body)
    }

def lambda_handler(event, context):
    logger.info("Event: %s", json.dumps(event)[:2000])

    # Handle preflight CORS
    if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
        return make_response(200, {"message": "OK"})

    # Parse JSON body
    try:
        body = event.get("body")
        if body is None:
            raise ValueError("Missing request body.")
        if event.get("isBase64Encoded"):
            body = base64.b64decode(body).decode("utf-8")
        payload = json.loads(body)
    except Exception as e:
        logger.exception("Bad request body")
        return make_response(400, {"error": f"Invalid JSON body: {str(e)}"})

    # Validate required keys
    missing = [k for k in FEATURE_NAMES if k not in payload]
    if missing:
        return make_response(400, {
            "error": "Missing required features",
            "required_features": FEATURE_NAMES,
            "missing": missing
        })

    # Compute score and class
    try:
        prob = score(payload)
        label = int(prob >= 0.5)
        result = {
            "probability": round(prob, 4),
            "label": label,
            "threshold": 0.5,
            "model_version": "v1.0",
            "features_used": {k: payload[k] for k in FEATURE_NAMES}
        }
        return make_response(200, {"prediction": result})
    except Exception as e:
        logger.exception("Scoring failure")
        return make_response(500, {"error": f"Scoring error: {str(e)}"})
