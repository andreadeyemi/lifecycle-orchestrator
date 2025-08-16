import csv

# Define custom weights per metric (out of 100 total)
WEIGHTS = {
    "login_count": 0.4,
    "feature_adoption": 0.3,
    "support_tickets": 0.2,
    "days_active": 0.1
}

def load_usage_data(csv_path):
    with open(csv_path, mode='r') as file:
        return list(csv.DictReader(file))

def calculate_health_score(row):
    try:
        score = (
            int(row["login_count"]) * WEIGHTS["login_count"] +
            int(row["feature_adoption"]) * WEIGHTS["feature_adoption"] -
            int(row["support_tickets"]) * WEIGHTS["support_tickets"] +
            int(row["days_active"]) * WEIGHTS["days_active"]
        )
        return max(min(round(score, 2), 100), 0)  # Clamp between 0–100
    except Exception as e:
        print(f"⚠️ Error calculating score for row: {row['customer_id']}")
        return 0

if __name__ == "__main__":
    data = load_usage_data("sample_data/usage_metrics.csv")
    print("📊 Customer Health Scores\n")
    for row in data:
        score = calculate_health_score(row)
        print(f"{row['customer_id']}: {score}/100")
