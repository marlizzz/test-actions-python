import psycopg


def test_add():
    assert 1 + 1 == 2


def test_postgresql_connection():
    with (
        psycopg.connect() as conn,
        conn.cursor() as cur
    ):
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print(f"PostgreSQL version: {version[0] if version else version}")

        cur.execute("SELECT 1")
        assert cur.fetchone() == (1,)
