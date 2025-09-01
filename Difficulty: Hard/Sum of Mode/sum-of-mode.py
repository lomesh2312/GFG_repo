from collections import defaultdict

class Solution:
    def sumOfModes(self, arr, k):
        if k == 0 or not arr:
            return 0

        freq = defaultdict(int)         # Frequency of each element in the current window
        count_map = defaultdict(set)    # Map from frequency -> set of numbers with that frequency
        max_freq = 0
        result = 0

        # Initialize the first window
        for i in range(k):
            num = arr[i]
            old_count = freq[num]
            freq[num] += 1
            if old_count > 0:
                count_map[old_count].remove(num)
                if not count_map[old_count]:
                    del count_map[old_count]
            count_map[freq[num]].add(num)
            max_freq = max(max_freq, freq[num])

        result += min(count_map[max_freq])

        # Slide the window
        for i in range(k, len(arr)):
            out_num = arr[i - k]
            old_count = freq[out_num]
            freq[out_num] -= 1

            count_map[old_count].remove(out_num)
            if not count_map[old_count]:
                del count_map[old_count]
            if freq[out_num] > 0:
                count_map[freq[out_num]].add(out_num)

            in_num = arr[i]
            old_count = freq[in_num]
            freq[in_num] += 1
            if old_count > 0:
                count_map[old_count].remove(in_num)
                if not count_map[old_count]:
                    del count_map[old_count]
            count_map[freq[in_num]].add(in_num)

            # Update max_freq
            if freq[in_num] > max_freq:
                max_freq = freq[in_num]
            elif max_freq not in count_map:
                max_freq -= 1

            result += min(count_map[max_freq])

        return result
