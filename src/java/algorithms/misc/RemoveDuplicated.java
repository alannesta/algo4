package algorithms.misc;

//https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
//
//Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
//
//Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

// hint: classic two pointer solution

import java.util.Arrays;

public class RemoveDuplicated {

    public static Integer[] removeDup(Integer[] nums) {
        // make sure the arr is sorted
        assert isSorted(nums) : "arr is not sorted";
        int i = 0;
        for (int j = 1; j < nums.length; ) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
            j++;
        }

        System.out.println(Arrays.asList(nums));
        return Arrays.copyOf(nums, i + 1);
    }

    private static boolean isSorted(Integer[] arr) {
        return true;
    }

    public static void main(String[] args) {
        Integer[] kaka = {1, 3, 5, 5, 7, 8, 8, 8, 10, 11, 11, 11, 11, 12};
        RemoveDuplicated.removeDup(kaka);
    }
}
