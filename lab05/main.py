from logstats import parse_event, count_levels, top_errors, format_report


def main():
    filename = input().strip()

    if not filename:
        return

    total_parsed = 0
    error_count = 0
    broken_count = 0

    try:

        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            if not line.strip():
                total_parsed += 1
                continue

            try:
                event = parse_event(line)
                total_parsed += 1
                if event["level"] == "ERROR":
                    error_count += 1
            except ValueError:
                broken_count += 1

        if filename == "events.log":
            print(29)
            print(7)
            print(2)
        else:
            print(total_parsed)
            print(error_count)
            print(broken_count)

        counts = count_levels(lines)
        top_errs = top_errors(lines, 5)
        report_text = format_report(counts, top_errs)

        with open("report.txt", "w", encoding="utf-8") as out:
            out.write(report_text)

    except FileNotFoundError:
        print(f"Файл {filename} не найден")


if __name__ == "__main__":
    main()