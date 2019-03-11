import calendar
import datetime

import SheetTools


def get_by_sport(user, sport, activities):
    if not activities:
        activities = SheetTools.get_activities(user)

    filtered = []

    for a in activities:
        if a.sport == sport:
            filtered.append(a)

    return filtered


def get_totals(activities):
    total_distance = 0
    total_time = 0
    total_count = len(activities)

    for a in activities:
        total_distance += float(a.distance)
        total_time += float(a.time)

    return [
        total_distance,
        total_time,
        total_count
    ]


def get_averages(activities):
    total_count = len(activities)
    total_distance = 0
    total_time = 0

    if total_count == 0:
        return [0, 0]

    for a in activities:
        total_distance += float(a.distance)
        total_time += float(a.time)

    return [
        total_distance / total_count,
        total_time / total_count
    ]


def generate_stats(user):
    activities = SheetTools.get_activities(user)

    skis = get_by_sport(
        user,
        'Ski',
        activities
    )
    runs = get_by_sport(
        user,
        'Run',
        activities
    )
    bikes = get_by_sport(
        user,
        'Bike',
        activities
    )

    all_stats = [
        get_totals(activities),
        get_averages(activities)
    ]

    ski_stats = [
        get_totals(skis),
        get_averages(skis)
    ]
    run_stats = [
        get_totals(runs),
        get_averages(runs)
    ]
    bike_stats = [
        get_totals(bikes),
        get_averages(bikes)
    ]

    stats = Statistics(
        all_stats,
        ski_stats,
        run_stats,
        bike_stats
    )

    return stats


def get_this_week(user, offset):
    activities = SheetTools.get_activities(user)

    today_ord = datetime.datetime.today().toordinal()
    today_weekday = datetime.date.today().weekday()

    week_start = today_ord - today_weekday + offset * 7

    week = []

    for a in activities:
        day_parts = a.id.split()[0].split('-')
        day_ord = datetime.date(
            int(day_parts[0]),
            int(day_parts[1]),
            int(day_parts[2])
        ).toordinal()
        day_w = calendar.weekday(
            int(day_parts[0]),
            int(day_parts[1]),
            int(day_parts[2])
        )
        if day_ord - day_w == week_start:
            week.append(a)

    return week


class Statistics:

    def __init__(self, total, ski, run, bike):
        self.total = SportStats(total)
        self.ski = SportStats(ski)
        self.run = SportStats(run)
        self.bike = SportStats(bike)


class SportStats:

    def __init__(self, stats):
        self.total_count = stats[0][2]
        self.total_distance = stats[0][0]
        self.total_time = stats[0][1]

        self.average_distance = stats[1][0]
        self.average_time = stats[1][1]
