import csv
from collections import defaultdict

def load_feedback(path):
    with open(path, 'r') as f:
        return list(csv.DictReader(f))

def summarize_feedback(feedback_rows):
    summary = defaultdict(list)
    for row in feedback_rows:
        area = row["product_area"]
        summary[area].append(row["feedback"])
    return summary

def generate_digest(summary):
    print("🧠 Weekly Feedback Digest\n────────────────────────────")
    for area, comments in summary.items():
        print(f"\n📌 {area} ({len(comments)} mentions)")
        for i, comment in enumerate(comments[:3], 1):
            print(f"  {i}. {comment}")
        if len(comments) > 3:
            print(f"  ...and {len(comments) - 3} more")

if __name__ == "__main__":
    feedback = load_feedback("sample_data/client_feedback.csv")
    summary = summarize_feedback(feedback)
    generate_digest(summary)
