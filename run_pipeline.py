
import subprocess
import sys
from src.pipeline_logger import log_info, log_error
print("Starting Retail Data Engineering Pipeline...")
log_info("Retail Data Engineering Pipeline started")

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
    log_info(f"Starting pipeline step: {step}")

    try:
        subprocess.run(
            [sys.executable, step],
            check=True
        )

        log_info(f"Successfully completed pipeline step: {step}")

    except subprocess.CalledProcessError as error:
        log_error(f"Pipeline step failed: {step} - {error}")
        print(f"ERROR: Pipeline step failed: {step}")
        sys.exit(1)
print("\nRunning Automated Data Quality Tests...", flush=True)
log_info("Starting automated data quality tests")

try:
    subprocess.run(
        test_command,
        check=True
    )

    log_info("All automated data quality tests passed")

except subprocess.CalledProcessError as error:
    log_error(f"Automated tests failed: {error}")
    print("ERROR: Automated data quality tests failed")
    sys.exit(1)

print("\nRetail Data Engineering Pipeline Completed!")
log_info("Retail Data Engineering Pipeline completed successfully")