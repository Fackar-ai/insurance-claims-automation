import time
import json
import random

def extract_documents(claim_id):
    print(f"[{claim_id}] Extracting documents...")
    time.sleep(1)
    return ["doc1.pdf", "doc2.pdf"]

def process_with_ai(documents):
    print("Processing with AI...")
    time.sleep(1)

    return {
        "document_type": random.choice(["hospitalization", "death", "injury"]),
        "valid": True,
        "amount": random.randint(1000, 5000)
    }

def validate_claim(data):
    print("Validating claim...")
    time.sleep(1)

    return {
        "is_new": random.choice([True, False]),
        "policy_found": True
    }

def process_claim(claim_id):
    docs = extract_documents(claim_id)
    ai_data = process_with_ai(docs)
    validation = validate_claim(ai_data)

    result = {
        "claim_id": claim_id,
        "documents": docs,
        "ai_data": ai_data,
        "validation": validation
    }

    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    for i in range(1, 4):
        process_claim(i)
