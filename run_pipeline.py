
import subprocess
import sys

print("Starting Retail Data Engineering Pipeline...")


steps = [
    "src/data_validation.py",
    "src/data_cleaning.py",
    "src/load_to_sql.py",
    "src/run_sql_analysis.py"
]

# Run automated tests after the pipeline
test_command = [
    sys.executable,
    "-m",
    "unittest",
    "discover",
    "-s",
    "tests",
    "-p",
    "test_*.py",
    "-v"
]


for step in steps:
    print(f"\nRunning: {step}", flush=True)

    subprocess.run(
        [sys.executable, step],
        check=True
    )

print("\nRunning Automated Data Quality Tests...", flush=True)

subprocess.run(
    test_command,
    check=True
)
print("\nRetail Data Engineering Pipeline Completed!")
