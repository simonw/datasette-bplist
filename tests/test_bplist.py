from datasette_bplist import prepare_connection, render_cell
import sqlite3


hello_world_in_bplist = (
    b"bplist00\xd1\x00\x01\x00\x02UhelloUworld\x08\r\x13\x00\x00"
    b"\x00\x00\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19"
)


def test_render_cell():
    assert None == render_cell("hello")
    expected = '<pre style="white-space: pre-wrap">{\n    &#34;hello&#34;: &#34;world&#34;\n}</pre>'
    assert expected == render_cell(hello_world_in_bplist)


def test_custom_sql_function():
    conn = sqlite3.connect(":memory:")
    prepare_connection(conn)
    sql = "select bplist_to_json(?)"
    result = conn.execute(sql, (hello_world_in_bplist,)).fetchone()[0]
    assert '{"hello": "world"}' == result
