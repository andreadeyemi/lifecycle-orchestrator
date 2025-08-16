import csv
from datetime import datetime

def load_onboarding_data(csv_path):
    with open(csv_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def calculate_days_since_start(start_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    return (datetime.today() - start).days

def summarize_onboarding(data):
    summary = {}
    for row in data:
        stage = row["Stage"]
        summary[stage] = summary.get(stage, 0) + 1
    return summary

if __name__ == "__main__":
    customers = load_onboarding_data("sample_data/new_customers.csv")
    print("🧾 Onboarding Summary:\n")
    summary = summarize_onboarding(customers)
    for stage, count in summary.items():
        print(f"{stage}: {
