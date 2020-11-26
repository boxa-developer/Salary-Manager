from django.db import connection


def select_clause(query_str):
    with connection.cursor() as cursor:
        cursor.execute(
            query_str
        )
        rows = cursor.fetchall()
    return rows


def insert_clause(query_str):
    with connection.cursor() as cursor:
        cursor.execute(
            query_str
        )


def update_clause(query_str):
    with connection.cursor() as cursor:
        cursor.execute(
            query_str
        )


def delete_clause(query_str):
    with connection.cursor() as cursor:
        cursor.execute(
            query_str
        )
