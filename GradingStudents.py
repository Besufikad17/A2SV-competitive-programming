def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade < 38:
            res.append(grade)
        else:
            m = int(grade / 5)
            g = (m + 1) * 5
            if g - grade < 3:
                res.append(g)
            else:
                res.append(grade)
    return res
        
        