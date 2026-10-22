def parse_event(line):
    parts = line.split(maxsplit=2)

    if len(parts) < 2:
        raise ValueError("Недостаточно данных в строке")

    if len(parts) == 2:
        parts.append("")

    time, level, message = parts

    allowed_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}

    if level not in allowed_levels:
        if level == "W":
            level = "WARNING"
        else:
            raise ValueError("Неизвестный уровень логирования")

    return {
        "time": time,
        "level": level,
        "message": message
    }

def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts


def top_errors(lines, n):
    error_counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:

            pass


    sorted_errors = sorted(
        error_counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    result = [[msg, count] for msg, count in sorted_errors[:n]]
    return result


def format_report(counts, errors):
    report = []

    report.append("Отчёт по журналу")
    report.append("")
    for level in sorted(counts.keys()):
        report.append(f"{level}: {counts[level]}")

    report.append("")
    report.append("Частые ошибки:")


    for msg, count in errors:
        report.append(f"- {msg} — {count}")


    return "\n".join(report) + "\n"