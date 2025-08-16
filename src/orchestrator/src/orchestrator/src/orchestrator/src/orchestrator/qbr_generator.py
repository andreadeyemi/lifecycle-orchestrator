import csv
from datetime import datetime

TEMPLATE = """
🔹 QBR Summary for {customer_name} ({customer_id})
────────────────────────────────────────────
• Logins this quarter: {login_count}
• Features used: {feature_adoption}
• Support tickets: {support_tickets}
• Active days: {days_active}

🧠 Observations:
{insights}

📈 Next Steps:
- Recommend {action}

Generated on {date}
"""

def load_data(path):
    with open(path, 'r') as f:
        return list(csv.DictReader(f))

def generate_qbr(row):
    insights = "Usage is steady, but support ticket volume is high."
    action = "deep dive with TAM + feature retraining"
    return TEMPLATE.format(
        customer_name=row["customer_name"],
        customer_id=row["customer_id"],
        login_count=row["login_count"],
        feature_adoption=row["feature_adoption"],
        support_tickets=row["support_tickets"],
        days_active=row["days_active"],
        insights=insights,
        action=action,
        date=datetime.now().strftime("%Y-%m-%d")
    )

if __name__ == "__main__":
    data = load_data("sample_data/usage_metrics.csv")
    for row in data:
        print(generate_qbr(row))
        print("─" * 40)
