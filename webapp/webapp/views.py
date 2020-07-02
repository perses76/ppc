from django.http import JsonResponse
from django.db import connection


def kpi1(request):
    sql = "SELECT interval_start_timestamp, interval_end_timestamp, service_id, total_bytes, `interval` FROM kpi1 WHERE 1=1 "
    sql_args = []

    if 'start_from' in request.GET:
        sql += "AND interval_start_timestamp >= %s "
        sql_args.append(request.GET["start_from"])
    if 'end_to' in request.GET:
        sql += "AND interval_end_timestamp < %s "
        sql_args.append(request.GET["end_to"])
    limit = 1000
    if 'limit' in request.GET:
        limit = int(request.GET["limit"])
    sql += f"LIMIT {limit}"

    with connection.cursor() as cur:
        cur.execute(sql, sql_args)
        rows = dictfetchall(cur)
    return JsonResponse(rows, safe=False)


def kpi2(request):
    sql = "SELECT interval_start_timestamp, interval_end_timestamp, cell_id, number_of_unique_users, `interval` FROM kpi2 WHERE 1=1 "
    sql_args = []

    if 'start_from' in request.GET:
        sql += "AND interval_start_timestamp >= %s "
        sql_args.append(request.GET["start_from"])
    if 'end_to' in request.GET:
        sql += "AND interval_end_timestamp < %s "
        sql_args.append(request.GET["end_to"])
    limit = 1000
    if 'limit' in request.GET:
        limit = int(request.GET["limit"])
    sql += f"LIMIT {limit}"

    with connection.cursor() as cur:
        cur.execute(sql, sql_args)
        rows = dictfetchall(cur)
    return JsonResponse(rows, safe=False)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
