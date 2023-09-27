import yaml
from pprint import pprint


def showit(filename):
    with open(filename, "r") as f:
        result = yaml.safe_load(f)
        pprint(result, indent=2, sort_dicts=False)


def showthem(filename):
    with open(filename, "r") as f:
        result = yaml.safe_load_all(f)
        for doc in result:
            print(doc)
            pprint(result[doc], indent=2, sort_dicts=False)
