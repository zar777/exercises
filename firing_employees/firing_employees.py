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
            else:
                profit_partial += salary_emplo
                if profit_partial > 0:
                    profit += salary_emplo
        return profit


if __name__ == '__main__':
    m = [0,1,2,1,2,3,4,2,3]
    s = [5,3,6,8,4,2,4,6,7]
    p = [2,5,7,8,5,3,5,7,9]
    firing = FiringEmployees()
    print firing.fire(m,s,p)
