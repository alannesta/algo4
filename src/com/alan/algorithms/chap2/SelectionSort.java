package com.alan.algorithms.chap2;

import java.util.stream.IntStream;

import com.alan.algorithms.chap1.ThreeSumFast;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Stopwatch;

public class SelectionSort {

	public static void sort(Comparable[] a) {
		int N = a.length;

		// stupid brute force, unneccessary exchange operations
//		for (int i = 0; i < N-1; i++) {
//			for (int j = i+1; j<N; j++) {
//				if (less(a[j], a[i])) {
//					exchange(a, i, j);
//				}
//			}
//		}

		// reduce exchange operations (array access)
		for (int i = 0; i < N-1; i++) {
			int min = i;
			for (int j = i+1; j<N; j++) {
				if (less(a[j], a[min])) {
					min = j;
				}
			}
			exchange(a, i, min);
		}

		// faster implementation from textbook
//		for (int i = 0; i < N; i++) {
//			int min = i;
//			for (int j = i+1; j < N; j++) {
//				if (less(a[j], a[min])) {
//					min = j;
//				}
//			}
//			exchange(a, i, min);
//		}
	}

	private static boolean less(Comparable a, Comparable b) {
		return a.compareTo(b) < 0;
	}

	private static void exchange(Comparable[] a, int i, int j) {
		Comparable temp = a[i];
		a[i] = a[j];
		a[j] = temp;
	}

	public static boolean isSorted(Comparable[] a) {
		for (int i=0; i<a.length-1; i++) {
			if (less(a[i+1], a[i])) {
				return false;
			}
		}
		return true;
	}

	public static void print(Comparable[] a) {
		for (int i=0; i<a.length; i++) {
			StdOut.print(a[i] + " ");
		}
		StdOut.println();
	}

	public static void main(String[] args){
//		int[] arr = {1,2,43, 434, 43, 21, 3, 31};
//		String[] strs = {"alan", "jessica", "David", "Mary", "Gabi"};

		In in = new In("/Users/sijin.cao/git/princeton-algo/data/14Kints.txt");
		int[] arr = in.readAllInts();
		// JDK8 box
		Integer[] boxedInts = IntStream.of(arr).boxed().toArray(Integer[]::new);
		Stopwatch timer = new Stopwatch();
		sort(boxedInts);

		StdOut.print("time used: " + timer.elapsedTime());
		StdOut.println();
		assert(isSorted(boxedInts));
		print(boxedInts);
	}
}
