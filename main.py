import time
import json

def process_claim(claim_id):
    print(f"Processing claim {claim_id}...")

    # Simulate document extraction
    time.sleep(1)

    # Simulated AI response
    data = {
        "id": claim_id,
        "status": "processed",
        "type": "new_claim",
        "policy_found": True
    }

    print("Processed:", json.dumps(data, indent=2))
    return data


if __name__ == "__main__":
    for i in range(1, 6):
        process_claim(i)
