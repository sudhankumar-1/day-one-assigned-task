import csv

# The rule-based workflow uses predefined rules to parse the query and extract data from the CSV.
def run_rule_based_workflow(query):
    print("--- Rule-Based Workflow ---")
    print(f"User Query: {query}")
    
    # Predefined rules for parsing the query
    query_lower = query.lower()
    
    if "how much" in query_lower and "spend" in query_lower:
        if "food" in query_lower:
            target_category = "Food"
        elif "transport" in query_lower:
            target_category = "Transport"
        elif "entertainment" in query_lower:
            target_category = "Entertainment"
        else:
            print("Response: I can only calculate expenses for Food, Transport, or Entertainment.")
            return

        total_spent = 0.0
        try:
            with open("expenses.csv", mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Category"].lower() == target_category.lower():
                        total_spent += float(row["Amount"])
            print(f"Response: Based on your records, you spent ${total_spent:.2f} on {target_category}.")
        except FileNotFoundError:
            print("Response: I cannot find the expenses data.")
    else:
        print("Response: I am only programmed to calculate how much you spent on specific categories.")

if __name__ == "__main__":
    query = "How much did I spend on food this month according to my expenses?"
    run_rule_based_workflow(query)
