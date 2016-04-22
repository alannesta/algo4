package com.alan.algorithms.chap2;

import edu.princeton.cs.algs4.StdOut;

public class BinaryHeap {

	private int[] arr;
	private int count = 0;

	public BinaryHeap(int size) {
		arr = new int[size + 1];
	}

	public void insert(int value) {
		if (count == arr.length - 1) {
			delMax();
		}
		arr[++count] = value;
		swim(count);
	}

	public int delMax() {
		int result = arr[1];
		arr[1] = arr[count - 1];
		count--;
		sink(1);
		return result;
	}

	// bottom up
	private void swim(int index) {
		while (arr[index] > arr[index / 2] && index > 1) {
			swap(index, index / 2);
			index = index / 2;
		}
	}

	// top down
	private void sink(int index) {
		while ((2 * index) <= count && (arr[index] < arr[index * 2] || arr[index] < arr[index * 2 + 1])) {
			if (arr[index] < arr[index * 2]) {
				if (arr[index*2] < arr[index*2+1]) {
					swap(index, index * 2 + 1);
					index = 2 * index + 1;
				}else {
					swap(index, index * 2);
					index = index * 2;
				}
			} else {
				swap(index, index * 2 + 1);
				index = 2 * index + 1;
			}
		}
	}

	// heapify
	private void sink(int[] arr, int index, int count) {
		while ((2 * index + 1) < count && (arr[index] < arr[index * 2] || arr[index] < arr[index * 2 + 1])) {
			if (arr[index] < arr[index * 2]) {
				if (arr[index*2] < arr[index*2+1]) {
					swap(index, index * 2 + 1);
					index = 2 * index + 1;
				}else {
					swap(index, index * 2);
					index = index * 2;
				}
			} else {
				swap(index, index * 2 + 1);
				index = 2 * index + 1;
			}
		}
	}

	private void swap(int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	private void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	/**
	 * build a heap out of an array
	 * @param arr
	 */
	public void buildHeap(int[] arr) {
		int N = arr.length-1;
		for (int i = N/2; i > 0; i--) {
			sink(arr, i, N);
		}
	}

	public void heapSort(int[] arr) {
		buildHeap(arr);
		int N = arr.length-1;
		for (int i = N-1; i > 0; i--) {
			swap(arr, i, 1);
			sink(arr, 1, --N);
		}
	}

	public static void main(String[] args) {
//		BinaryHeap bh = new BinaryHeap(15);
//		for (int i = 0; i < 10; i++) {
//			bh.insert(i);
//		}
//		StdOut.println(bh.delMax());
//		StdOut.println(bh.delMax());
//		StdOut.println(bh.delMax());
//		StdOut.println(bh.delMax());

		BinaryHeap bh = new BinaryHeap(15);
		int[] sortable = {0, 6,8,10,11,22, 1, 4, 7};
		bh.heapSort(sortable);
		for (int i : sortable) {
			StdOut.print(i + ",");
		}
	}
}
