import json


def pp_json(json_thing, sort=False, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError
