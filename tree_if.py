from collections import OrderedDict
import pprint


def countAPI(calls):
    r = OrderedDict()
    for call in calls:
        p, s, m = tuple(call.split('/')[1:])
        try:
            r[p][s][m] += 1
        except KeyError as e:
            e = e.args[0]
            if str(e) == p:
                r[p] = OrderedDict()
                r[p][s] = OrderedDict()
                r[p][s][m] = 1
            elif str(e) == s:
                r[p][s] = OrderedDict()
                r[p][s][m] = 1
            else:
                r[p][s][m] = 1

    pprint.pprint(r)


calls = [
    "/project1/subproject1/method1",
    "/project2/subproject1/method1",
    "/project1/subproject1/method1",
    "/project1/subproject2/method1",
    "/project1/subproject1/method2",
    "/project1/subproject2/method1",
    "/project2/subproject1/method1",
    "/project1/subproject2/method1"
]

countAPI(calls)
