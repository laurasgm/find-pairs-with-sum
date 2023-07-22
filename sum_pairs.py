import argparse

def find_pairs_with_sum(list_nums, target_num):
    """
    Function to find pairs of numbers where the sum should be the target_num.
    :param list_nums: List[int]; List of numbers to find pairs from.
    :param target_num: int; The target sum.
    :return: List[tuple]; List with pairs that sum to the target_num.
    """
    nums_check = []

    result = []
    for num in list_nums:
        complement = target_num - num
        if complement in nums_check:
            result.append((num, complement))
        nums_check.append(num)

    return result


def __get_params():
    """
    Get params for script requirements
    """
    parser = argparse.ArgumentParser(description='Find pairs of integers that sum to a target value.')
    parser.add_argument('--input_list', type=int, nargs='+', help='List of integers separated by spaces.')
    parser.add_argument('--target', type=int, help='Target integer value.')

    return parser.parse_args()

if __name__ == "__main__":
    args = __get_params()
    input_list = args.input_list
    target = args.target
    pairs = find_pairs_with_sum(input_list, target)

    for pair in pairs:
        print("+", pair[0], ",", pair[1])