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
				if (arr[index] < arr[index * 2 + 1] && arr[index*2] < arr[index*2+1]) {
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

	public static void main(String[] args) {
		BinaryHeap bh = new BinaryHeap(15);
		for (int i = 0; i < 10; i++) {
			bh.insert(i);
		}
		StdOut.println(bh.delMax());
		StdOut.println(bh.delMax());
		StdOut.println(bh.delMax());
		StdOut.println(bh.delMax());
	}
}
