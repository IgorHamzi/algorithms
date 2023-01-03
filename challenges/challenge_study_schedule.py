def study_schedule(permanence_period, target_time):
    counter = 0

    if target_time is None:
        return None
    else:
        try:
            for i in permanence_period:
                for j in range(i[0], i[1]+1):
                    if j == target_time: 
                        counter += 1
            return counter
        except:
            return None



# if __name__ == '__main__':
#    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
#    target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
#    study_schedule(permanence_period, target_time)
