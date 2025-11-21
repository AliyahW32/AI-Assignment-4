from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []

    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")

    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")

    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")

    if input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")

    if input("Are you doing creative work (video/photo editing)? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    
    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    
    if input("Do you plan on traveling frequently with your laptop? (y/n): ").lower().startswith("y"):
        facts.append("frequent_travel")


    return facts


def main():
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)

    user_facts = collect_initial_facts()
    engine.assert_facts(user_facts)

    engine.run()
    result = engine.conclusions()

    if result["recommendations"]:
        print("> Recommendation:", result["recommendations"][0])
    else:
        print("> Recommendation: (none)")

    if result["trace"]:
        print("> Explanation: derived from rule '" + result["trace"][0]["rule"] + "'")
    else:
        print("> Explanation: no rule fired")


if __name__ == "__main__":
    main()