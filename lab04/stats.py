
def parse_record(line: str) -> dict:
    parts = line.split(';')


    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}: {line!r}")


    city, temp_raw, date = (p.strip() for p in parts)


    if not city or not date:
        raise ValueError(f"Пустой город или дата: {line!r}")


    try:
        temperature = float(temp_raw.replace(',', '.'))
    except ValueError as exc:
        raise ValueError(f"Температура не число: {temp_raw!r}") from exc


    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temperature"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:

    averages = average_by_city(records)
    if not averages:
        raise ValueError("Нет данных для определения самого тёплого города")
    return min(averages, key=lambda c: (-averages[c], c))