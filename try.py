from src.datasets.load import load_dataset

builder = load_dataset("open-llm-leaderboard/results", "default", split="test", trust_remote_code=True)

# print the dataset info
print(builder)
