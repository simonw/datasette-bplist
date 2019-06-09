import json

from datasette import hookimpl
from bpylist import bplist

import jinja2


@hookimpl
def prepare_connection(conn):
    conn.create_function("bplist_to_json", 1, bplist_to_json)


def bplist_to_json(value):
    try:
        return json.dumps(bplist.parse(value), default=repr)
    except Exception as ex:
        return json.dumps({"error": str(ex)})


@hookimpl
def render_cell(value):
    if not isinstance(value, (bytes, str)):
        return None

    if (isinstance(value, bytes) and value.startswith(b"bplist00")) or (
        isinstance(value, str) and value.startswith("bplist00")
    ):
        try:
            parsed = bplist.parse(value)
        except Exception:
            return None
        return jinja2.Markup(
            '<pre style="white-space: pre-wrap">{data}</pre>'.format(
                data=jinja2.escape(json.dumps(parsed, default=repr, indent=4))
            )
        )

    return None
