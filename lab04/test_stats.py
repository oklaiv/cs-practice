import pytest

from stats import (
    parse_record,
    read_valid,
    average_by_city,
    warmest_city,
)


def test_parse_record_ok():
    rec = parse_record("Азов;24.5;2026-07-01")
    assert rec == {"city": "Азов", "temperature": 24.5, "date": "2026-07-01"}


def test_parse_record_bad_fields():
    with pytest.raises(ValueError):
        parse_record("мусор")


def test_parse_record_bad_temp():
    with pytest.raises(ValueError):
        parse_record("Азов;н/д;2026-07-01")


def test_read_valid_skips_blank_and_bad():
    lines = ["Азов;24.5;2026-07-01", "", "мусор", "Таганрог;30;2026-07-01"]
    assert len(read_valid(lines)) == 2


def test_average_by_city():
    records = read_valid([
        "Азов;24.5;2026-07-01",
        "Азов;25.5;2026-07-02",
        "Таганрог;30;2026-07-01",
    ])
    assert average_by_city(records) == {"Азов": 25.0, "Таганрог": 30.0}


def test_warmest_city():
    records = read_valid([
        "Азов;24.5;2026-07-01",
        "Азов;25.5;2026-07-02",
        "Таганрог;30;2026-07-01",
    ])
    assert warmest_city(records) == "Таганрог"


def test_warmest_city_tie_alphabetical():
    records = read_valid([
        "Б;10;2026-07-01",
        "А;10;2026-07-01",
    ])
    assert warmest_city(records) == "А"