from collections import OrderedDict
import pprint


def countAPI(calls):

  r = OrderedDict()
  for call in calls:
    p, s, m = tuple(call.split('/')[1:])

    try:
      project = r[p]
    except:
      r[p] = OrderedDict()
      r[p][s] = OrderedDict()
      ((r[p])[s])[m] = 1
      continue

    try:
      sub = project[s]
    except:
      project[s] = OrderedDict()
      project[s][m] = 1
      continue
    try:
      sub[m] += 1
    except:
      sub[m] = 1

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