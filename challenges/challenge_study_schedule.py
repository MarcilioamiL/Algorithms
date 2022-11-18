def study_schedule(permanence_period, target_time):
    """
    # test manual schedule
    >>> study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 1)
    2

    :param permanence_period:
    :param target_time:
    :return:
    """
    users = 0
    try:
        for time_start, time_end in permanence_period:
            if time_start <= target_time <= time_end:
                users += 1
        return users
    except TypeError:
        return None
