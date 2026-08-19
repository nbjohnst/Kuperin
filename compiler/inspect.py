import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
EXAMPLES_ROOT = PROJECT_ROOT / "examples"


def find_by_id(object_id):
    for path in EXAMPLES_ROOT.rglob("*.json"):
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if data.get("id") == object_id:
            return data, path

    return None, None


def display_reference(label, object_id):
    data, _ = find_by_id(object_id)

    print(f"\n{label}: {object_id}")

    if data is None:
        print("  [reference not found]")
        return

    if "name" in data:
        print(f"  {data['name']}")

    if "summary" in data:
        print(f"  {data['summary']}")


def inspect_belief(belief):
    print(f"\n{belief['id']}")
    print("=" * len(belief["id"]))

    display_reference("Holder", belief["holder"])

    for object_id in belief.get("about", []):
        display_reference("About", object_id)

    print("\nClaim:")
    print(f"  {belief['content']}")

    print(f"\nState: {belief['state']}")

    if belief.get("confidence") is not None:
        print(f"Confidence: {belief['confidence']:.2f}")

    print("\nSupporting evidence:")

    for event_id in belief.get("supported_by", []):
        display_reference("Supports", event_id)

    print("\nChallenging evidence:")

    for event_id in belief.get("challenged_by", []):
        display_reference("Challenges", event_id)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 compiler/inspect.py <ID>")
        sys.exit(1)

    object_id = sys.argv[1]
    data, path = find_by_id(object_id)

    if data is None:
        print(f"Object not found: {object_id}")
        sys.exit(1)

    if object_id.startswith("BELIEF-"):
        inspect_belief(data)
    else:
        print(f"\nFound: {object_id}")
        print(f"Source: {path.relative_to(PROJECT_ROOT)}")
        print()
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()