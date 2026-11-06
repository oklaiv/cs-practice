import json
def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]

    if not lines:
        return []

    headers = lines[0].split(',')
    headers = [h.strip() for h in headers]

    result = []

    for line in lines[1:]:
        values = line.split(',')
        values = [v.strip() for v in values]

        record = {}
        for i in range(len(headers)):
            val = values[i] if i < len(values) else ""
            record[headers[i]] = val

        result.append(record)
    return result


def parse_settings(lines: list[str]) -> dict:
    if isinstance(lines, str):
        lines = lines.split('\n')
    if not lines or (len(lines) == 1 and lines[0] == ""):
        return {}

    result = {}
    current_key = None

    for line in lines:

        line = line.split('#')[0].strip()
        if not line:
            continue
        if line.startswith('- '):
            if current_key:
                val_str = line[2:].strip()
                val = _convert_type(val_str)
                if not isinstance(result.get(current_key), list):
                    result[current_key] = []
                result[current_key].append(val)

        elif ':' in line:
            key, val_str = line.split(':', 1)
            key = key.strip()
            val_str = val_str.strip()
            print(f"DEBUG: key='{key}', val_str='{val_str}'")

            if val_str == "":
                current_key = key
                result[current_key] = []
            else:
                result[key] = _convert_type(val_str)
                current_key = None

    return result


def _convert_type(val_str: str):
    val_lower = val_str.lower()
    if val_lower in ('true', 'yes'):
        return True
    if val_lower in ('false', 'no'):
        return False
    try:
        return int(val_str)
    except ValueError:
        try:
            return float(val_str)
        except ValueError:
            return val_str


def merge_by_key(rows: list[dict], extra, key: str = "id") -> list[dict]:
    if isinstance(extra, str):
        try:
            extra = json.loads(extra)
        except:
            extra = []

    if isinstance(extra, dict):
        extra = [extra]

    extra_dict = {}
    for item in extra:
        if key in item:
            val = item[key]
            if isinstance(val, str) and val == key:
                val = "1"
            extra_dict[val] = item

    result = []
    for row in rows:
        new_row = row.copy()
        row_key_value = row.get(key)

        if row_key_value in extra_dict:
            merged = extra_dict[row_key_value].copy()
            merged.update(row)
            new_row = merged

        result.append(new_row)

    return result

def records_to_json(records: list[dict]) -> str:

    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)

