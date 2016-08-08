class FiringEmployees(object):
    def fire(self, manager, salary, productivity):
        profit = 0
        profit_partial = 0
        for index in xrange(0, len(manager)):
            salary_emplo = productivity[index] - salary[index]
            if index < len(manager)-1:
                profit += salary_emplo
                profit_partial += salary_emplo
                if manager[index] >= manager[index + 1] and profit_partial < 0:
                    profit -= profit_partial
                    profit_partial = 0
                if manager[index] == manager[index + 1]:
                    profit_partial = 0
                    if not (index < len(manager)-3 and manager[index+1] < manager[index + 2]):
                       break
            else:
                if salary_emplo > 0:
                    profit += salary_emplo
        return profit


if __name__ == '__main__':
    m = [0,0,1,1,2,2]
    s = [1,1,1,2,2,2]
    p = [2,2,2,1,1,1]
    firing = FiringEmployees()
    print firing.fire(m,s,p)
