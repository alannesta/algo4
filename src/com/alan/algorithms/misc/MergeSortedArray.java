package com.alan.algorithms.misc;


/*
https://leetcode.com/problems/merge-sorted-array/description/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

*/

public class MergeSortedArray {

    public static void main(String[] args) {
        int[] nums1 = new int[]{1, 2, 3, 0, 0, 0};
        int[] nums2 = new int[]{2, 5, 6};

        int m = 3, n = 3;
        int i = m + n - 1;
        int j = m - 1;
        int k = n - 1;

        while (i >= 0) {
            if (j >= 0 && k >= 0) {
                if (nums1[j] > nums2[k]) {
                    nums1[i] = nums1[j];
                    j--;
                } else {
                    nums1[i] = nums2[k];
                    k--;
                }
            } else if (k >= 0) {
                nums1[i] = nums2[k];
                k--;
            } else if (j >= 0) {
                nums1[i] = nums1[j];
                j--;
            }
            i--;
        }

        for (int w : nums1) {
            System.out.println(w);
        }

    }
}
