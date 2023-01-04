#def study_schedule(permanence_period, target_time):
#    students = 0
#
#    if target_time and permanence_period is None or type(permanence_period) != list:
#        return None
#    else:
#        for i in permanence_period:
#            if i is None: return None
#            if i[0] is None or i[1] is None: return None
#            if type(i[0]) != int or type(i[1]) != int: return None
#            for j in range(i[0], i[1]+1):
#                if j == target_time:
#                    students += 1
#        return students
