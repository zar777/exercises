def solution(cut_cost, unit_price, lengths):
    max_profit = 0
    max_element = max(lengths)
    # verify if it's necessary iterate numbers from 1 to max number of list
    for l_piece in xrange(max_element, 1, -1):
        cuts_pieces = lengths[0]/l_piece + lengths[1]/l_piece + lengths[2]/l_piece
        profit_tmp = (cuts_pieces*l_piece*unit_price) - (cuts_pieces*cut_cost)
        if profit_tmp > max_profit:
            max_profit = profit_tmp
    return max_profit


if __name__ == '__main__':
    cut_cost = 1
    unit_price = 10
    lengths = [26, 103, 59]
    print solution(cut_cost, unit_price, lengths)