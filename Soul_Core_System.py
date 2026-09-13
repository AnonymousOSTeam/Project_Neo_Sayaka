import subprocess
import json
import sys

def query_soul_core(cost=0.0):
    try:
        result = subprocess.run(
            ["./Soul_Core_System", str(cost)],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout.strip())
    except Exception as e:
        print(f"[!] Core Link Failure: {e}")
        sys.exit(1)

def main():
    print("=== NEO_SAYAKA OPERATOR TERMINAL v1.0 ===")
    print("Type subroutine cost (e.g., 25, 50) or 'exit' to quit.\n")

    while True:
        # Get current state first
        status = query_soul_core(0.0)
        print(f"\n[CORE STATUS] State: {status['state']} | Integrity: {status['integrity']}% | Entropy: {status['entropy']}%")

        if status['state'] == "CRITICAL_CORRUPTION":
            print("[!] WARNING: Soul Gem corruption threshold breached! Initiate purification loop!")
        elif status['state'] == "OVERHEAT":
            print("[!] ALERT: System entropy critical. Cool down required.")

        user_input = input("Operator@Neo_Sayaka~$ ").strip()
        
        if user_input.lower() in ["exit", "quit"]:
            print("Disconnecting terminal link...")
            break

        try:
            cost = float(user_input)
            print(f"[*] Executing subroutine, drawing {cost} entropy...")
            query_soul_core(cost)
        except ValueError:
            print("[?] Unknown command syntax. Enter a numeric energy cost.")

if __name__ == "__main__":
    main()
