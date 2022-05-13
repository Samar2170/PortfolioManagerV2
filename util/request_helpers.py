def unwrap_query_dict(qdict):
    return {k: v[0] if len(v) == 1 else v for k, v in qdict.lists()}