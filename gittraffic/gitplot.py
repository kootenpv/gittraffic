from collections import Counter
import json
import matplotlib


def plot_package(js, key):
    totals = Counter()
    for x in js[key]:
        if x[0][:10] not in totals:
            totals[x[0][:10]] = 0
        totals[x[0][:10]] += int(x[-1])
    matplotlib.pyplot.plot([totals[x] for x in sorted(totals)], label=key)
    matplotlib.pyplot.legend(loc='best')


def plot_all(gittraffic_path='gittraffic.json'):
    with open(gittraffic_path) as f:
        j = json.load(f)

    for k in j:
        plot_package(j, k)


def most_common_source(js, key):
    totals = Counter()
    for x in js[key]:
        if x[1] not in totals:
            totals[x[1]] = 0
        totals[x[1]] += int(x[-1])
    # has to still be divided by amount of unique days
    print(totals.most_common())
