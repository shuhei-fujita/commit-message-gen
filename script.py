import subprocess
import openai
from dotenv import load_dotenv
import os
import re

load_dotenv()

def analyze_diff(diff_output):
    file_changes = re.findall(r"diff --git a/(.+) b/(.+)", diff_output)
    added_lines = len(re.findall(r"^\+", diff_output, re.MULTILINE))
    deleted_lines = len(re.findall(r"^-", diff_output, re.MULTILINE))
    return {
        "file_changes": file_changes,
        "added_lines": added_lines,
        "deleted_lines": deleted_lines
    }

def generate_commit_message():
    diff_output = subprocess.getoutput("git diff --cached")
    analysis = analyze_diff(diff_output)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Generate a commit message based on the following analysis: {analysis}"
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=50
    )
    commit_message = response.choices[0].text.strip()
    return commit_message

# ブロックは不要です
# Pythonスクリプトが直接実行された場合にのみ実行されるコードを定義するために使用されます
# __name__ == "__main__" 

commit_message = generate_commit_message()
print(commit_message)
