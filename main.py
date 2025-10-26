import argparse
from modules import system_check, network_check, file_check, report


def main():
    parse = argparse.ArgumentParser(description="Cyber Hygeiene Checklist Tool")
    parse.add_argument("--output", help= "Save report to JSON file", default="reports/report.json")
    args = parse.parse_args()


    print("\n🧹 Running Cyber Hygiene Checks...\n")


    results = {}
    results['system'] = system_check.run()
    results['network'] = network_check.run()
    results['files'] = file_check.run()

    report.generate(results, args.output)
    print(f"\n✅ Report saved to {args.output}")
if __name__ == "__main__":
    main()