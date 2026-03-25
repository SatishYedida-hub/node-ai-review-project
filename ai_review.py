import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")

with open("changes.diff", "r") as f:
    code_changes = f.read()

prompt = f"""
Human: You are a senior Node.js reviewer.

Analyze the following code and provide:
1. Security issues
2. Bugs
3. Best practices

Code:
{code_changes}

Assistant:
"""

response = client.invoke_model(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    body=json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 300
    })
)

result = json.loads(response['body'].read())

print("\n===== AI CODE REVIEW =====\n")
print(result)
