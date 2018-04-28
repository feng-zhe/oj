def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_len = len(numbers)
        # try to find first element bigger than target in reverse order
        # but this element may be still when all are smaller
        for max_index in range(0, num_len):
            if numbers[max_index] > target:
                break
        print(max_index)
        for j in range(max_index, 0, -1):    # number[i] is smaller one
            for i in range(j-1, -1, -1):
                added = numbers[i] + numbers[j]
                if target == added:
                    return [i+1, j+1]
                elif target > added:
                    break

if __name__ == '__main__':
    print(twoSum([-1,0],-1))
