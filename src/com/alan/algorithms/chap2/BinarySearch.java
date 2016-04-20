package com.alan.algorithms.chap2;

import edu.princeton.cs.algs4.StdOut;

public class BinarySearch {
	// could also be done in a while loop version
	public static <T extends Comparable<T>> int search(T[] arr, T value, int low, int high) {
		int index = -1;
		if ((high - low) > -1) {
			int mid = (int) Math.floor((high + low) / 2);	// Java actually did this by default...
			if (arr[mid].compareTo(value) > 0) {
				high = mid - 1;		// here if you use high = mid or low = mid, could casue infinite loop---> Stackoverflow
				index = search(arr, value, low, high);
			} else if (arr[mid].compareTo(value) < 0) {
				low = mid + 1;
				index =search(arr, value, low, high);
			} else {
				index = mid;
			}
		}
		return index;
	}

	public static void main(String[] args) {
		Integer[] arr = {1, 2, 5, 6, 8, 13, 22, 26, 33, 45};
		StdOut.println(search(arr, 33, 0, 8));
	}
}
