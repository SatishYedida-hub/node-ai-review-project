import os
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read code changes
with open("changes.diff", "r") as f:
    code_changes = f.read()

prompt = f"""
You are a senior Node.js code reviewer.

Analyze the following code and provide:
1. Security issues
2. Bugs
3. Best practices

Code:
{code_changes}
"""

# Call GPT model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\n===== AI CODE REVIEW =====\n")
print(response.choices[0].message.content)
