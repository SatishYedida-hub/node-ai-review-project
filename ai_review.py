import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

with open("changes.diff", "r") as f:
    code_changes = f.read()

prompt = f"""
You are a senior Node.js code reviewer.

Review the following code and provide:
1. Bugs
2. Security issues
3. Best practices

Code:
{code_changes}
"""

response = client.invoke_model(
    modelId="anthropic.claude-v2",
    body=json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 300
    })
)

result = json.loads(response['body'].read())

print("\n===== AI CODE REVIEW =====\n")
print(result)
