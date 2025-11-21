from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""


class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        for cond in rule.antecedents:
            if cond not in self.facts:
                return False

        if rule.consequent in self.facts:
            return False

        return True

    def run(self) -> None:
        while True:
            fireable = [r for r in self.rules if self.can_fire(r)]

            if not fireable:
                break

            fireable.sort(key=lambda r: r.priority, reverse=True)
            rule = fireable[0]

            self.facts.add(rule.consequent)

            self.trace.append({
                "rule": rule.name,
                "added_fact": rule.consequent,
                "antecedents": rule.antecedents
            })

    def conclusions(self) -> Dict[str, List[str]]:
        recommendations = []
        specs = []

        for fact in self.facts:
            if fact.startswith("recommend:"):
                recommendations.append(fact.split(":", 1)[1])
            elif fact.startswith("spec:"):
                specs.append(fact.split(":", 1)[1])

        return {
            "recommendations": recommendations,
            "specs": specs,
            "trace": self.trace,
            "all_facts": list(self.facts)
        }
