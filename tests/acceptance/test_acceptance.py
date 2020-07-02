"""Test full process."""

import mysql.connector
import os
from ppc import main
import csv
from .. import settings


def test_success():
    reset_db()
    data_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "data")
    )
    main.run(folder=data_folder, db_config=settings.DB_CONFIG)
    assert_kpi1(
        "5min",
        [
            (1488355200000, 1488355500000, 1, 16100),
            (1488355200000, 1488355500000, 3, 11500),
            (1488355200000, 1488355500000, 2, 9260),
        ],
    )
    assert_kpi1(
        "1H",
        [
            (1488355200000, 1488355500000, 1, 16100),
            (1488355200000, 1488355500000, 3, 11500),
            (1488355200000, 1488355500000, 2, 9260),
        ],
    )

    assert_kpi2(
        "5min",
        [
            (1488355200000, 1488355500000, 1001, 4),
            (1488355200000, 1488355500000, 5005, 3),
            (1488355200000, 1488355500000, 1000, 3),
        ],
    )

    assert_kpi2(
        "1H",
        [
            (1488355200000, 1488355500000, 1001, 4),
            (1488355200000, 1488355500000, 5005, 3),
            (1488355200000, 1488355500000, 1000, 3),
        ],
    )


def assert_kpi1(interval, expected):
    rows = fetch_all(
        "SELECT interval_start_timestamp, interval_end_timestamp, service_id, total_bytes FROM kpi1 WHERE `interval` = %s",
        interval
    )
    assert rows == expected


def assert_kpi2(interval, expected):
    rows = fetch_all(
        "SELECT interval_start_timestamp, interval_end_timestamp, cell_id, number_of_unique_users FROM kpi2 WHERE `interval` = %s",
        interval
    )
    assert rows == expected


def reset_db():
    create_kpi_table_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "db", "create_kpi_tables.sql")
    )
    with open(create_kpi_table_file) as f:
        sql = f.read()
        execute_sql(sql)


def fetch_all(sql, *args):
    cn = mysql.connector.connect(**settings.DB_CONFIG)
    cur = cn.cursor()
    cur.execute(sql, args)
    rows = cur.fetchall()
    cur.close()
    cn.close()
    return rows

def execute_sql(sql, *args):
    cn = mysql.connector.connect(**settings.DB_CONFIG)
    cur = cn.cursor()
    cur.execute(sql, args)
    cur.close()
    cn.close()
