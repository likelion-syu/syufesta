def query_expand(rows , cursor):
    _expanded_rows = []

    for row in rows:
        _expanded_row = {}
        for idx , desc in enumerate(cursor.description):
            _expanded_row[desc[0]] = row[idx]
        _expanded_rows.append(_expanded_row)

    return _expanded_rows