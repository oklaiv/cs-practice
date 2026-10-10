"""Читает журнал со stdin и печатает отчёт."""

import sys

from stats import parse_record, read_valid, average_by_city, warmest_city


def count_skipped(lines: list[str]) -> int:
    """Сколько непустых строк оказались негодными."""
    skipped = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            parse_record(line)
        except ValueError:
            skipped += 1
    return skipped


def main() -> None:
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)
    print(len(records))
    print(count_skipped(lines))

    if not records:
        return

    avg = average_by_city(records)
    warm = warmest_city(records)
    print(f"{avg[warm]:.1f}")


if __name__ == "__main__":
    main()