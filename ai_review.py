import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

with open("changes.diff", "r") as f:
    code_changes = f.read()

prompt = f"""
You are a senior Node.js code reviewer.

Analyze the following code and provide:
1. Security issues
2. Bugs
2. Best practices

Code:
{code_changes}
"""

response = client.invoke_model(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 300
    })
)

result = json.loads(response['body'].read())

print("\n===== AI REVIEW =====\n")
print(result)
