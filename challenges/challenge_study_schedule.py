def study_schedule(permanence_period, target_time):
    students = 0

    if target_time is None or type(permanence_period) != list:
        return None

    for i in permanence_period:
        if type(i[0]) != int or type(i[1]) != int:
            return None
        if str(target_time) >= str(i[0]) and str(target_time) <= str(i[1]):
                students += 1

    return students
