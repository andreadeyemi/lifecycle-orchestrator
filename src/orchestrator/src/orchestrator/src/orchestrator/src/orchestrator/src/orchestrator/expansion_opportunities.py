import csv

EXPANSION_THRESHOLD = {
    "login_count": 50,
    "feature_adoption": 3,
    "support_tickets": 0
}

def load_data(path):
    with open(path, 'r') as f:
        return list(csv.DictReader(f))

def identify_expansion_opportunities(data):
    opportunities = []
    for row in data:
        if (
            int(row["login_count"]) >= EXPANSION_THRESHOLD["login_count"] and
            int(row["feature_adoption"]) >= EXPANSION_THRESHOLD["feature_adoption"] and
            int(row["support_tickets"]) <= EXPANSION_THRESHOLD["support_tickets"]
        ):
            opportunities.append({
                "customer_id": row["customer_id"],
                "customer_name": row["customer_name"],
                "logins": row["login_count"],
                "features": row["feature_adoption"]
            })
    return opportunities

if __name__ == "__main__":
    data = load_data("sample_data/usage_metrics.csv")
    leads = identify_expansion_opportunities(data)
    
    print("🚀 Expansion-Ready Accounts")
    print("────────────────────────────")
    for lead in leads:
        print(f"{lead['customer_name']} (ID: {lead['customer_id']}) — {lead['logins']} logins, {lead['features']} features used")
