"""
https://leetcode.com/problems/restore-ip-addresses/
"""
from typing import List


class Solution:
    def __init__(self):
        self.valid_ips = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.traverse(s, segment=4, cur_path=[])
        return self.valid_ips

    def traverse(self, ip_str, segment, cur_path):
        # check if string length is valid
        if len(ip_str) > segment * 3 or len(ip_str) < segment:
            return

        if segment == 1:
            if self.is_valid_segment(ip_str):
                cur_path.append(ip_str)
                self.valid_ips.append('.'.join(cur_path))
                # !!! important: backtrack here
                cur_path.pop()

            return

        for i in range(3):
            chars = ip_str[0: i + 1]  # python string slice do not have idx out of range issue
            if self.is_valid_segment(chars):
                cur_path.append(chars)
                self.traverse(ip_str[i + 1:], segment - 1, cur_path)
                cur_path.pop()

    def is_valid_segment(self, ip_str):
        if len(ip_str) > 3:
            return False
        if ip_str == '0':
            return True
        if ip_str.startswith('0'):
            return False

        if int(ip_str) > 255:
            return False

        return True


test = "25525511135"

print(Solution().restoreIpAddresses(test))
