import os
from datetime import datetime, timezone
from pathlib import Path


def get_utc_timestamp() -> float:
    return datetime.now(timezone.utc).timestamp()


def generate_junit_flags() -> list[str]:
    if not (junitxml_base_dir := os.getenv("PDRN_JUNIT_BASE")):
        return []

    junitxml_file = Path(junitxml_base_dir) / f"{get_utc_timestamp()}.xml"

    if prefix := os.getenv("PDRN_JUNIT_PREFIX"):
        junitxml_file = junitxml_file.with_name(f"{prefix}{junitxml_file.name}")

    return [f"--junit-xml={junitxml_file.as_posix()}"]


def generate_coverage_flags() -> list[str]:
    if not (cc_package_name := os.getenv("PDRN_COV_NAME")):
        return []

    return [
        f"--cov={cc_package_name}",
        "--cov-append",
        "--cov-report=html:coverage-html",
        "--cov-report=json:coverage.json",
    ]


def pytest_load_initial_conftests(_early_config, args: list[str], _parser):
    new_args: list[str] = []
    new_args.extend(generate_junit_flags())
    new_args.extend(generate_coverage_flags())
    args[:] = [*args, *new_args]
