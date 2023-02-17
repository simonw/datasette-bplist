from datasette import hookimpl
import plistlib
import json
import markupsafe


@hookimpl
def prepare_connection(conn):
    conn.create_function("bplist_to_json", 1, bplist_to_json)


def bplist_to_json(value):
    if value:
        try:
            return json.dumps(plistlib.loads(value), default=repr)
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
            parsed = plistlib.loads(value)
        except Exception:
            return None
        return markupsafe.Markup(
            '<pre style="white-space: pre-wrap">{data}</pre>'.format(
                data=markupsafe.escape(json.dumps(parsed, default=repr, indent=4))
            )
        )

    return None

