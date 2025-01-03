import os
from datetime import datetime, timezone
from pathlib import Path


def get_utc_timestamp() -> float:
    return datetime.now(timezone.utc).timestamp()


def pytest_load_initial_conftests(_early_config, args: list[str], _parser):
    new_args: list[str] = []

    # if PDRN_JUNIT_BASE is defined, prepare new --junit-xml flag
    if junitxml_base_dir := os.getenv("PDRN_JUNIT_BASE"):
        junitxml_file = Path(junitxml_base_dir) / f"{get_utc_timestamp()}.xml"
        if prefix := os.getenv("PDRN_JUNIT_PREFIX"):
            junitxml_file = junitxml_file.with_name(f"{prefix}{junitxml_file.name}")
        new_args.append(f"--junit-xml={junitxml_file.as_posix()}")

    # if PDRN_COV_NAME is defined, prepare code coverage flags
    if cc_package_name := os.getenv("PDRN_COV_NAME"):
        new_args.extend(
            [
                f"--cov={cc_package_name}",
                "--cov-append",
                "--cov-report=html:coverage-html",
                "--cov-report=json:coverage.json",
            ]
        )

    args[:] = [*args, *new_args]
