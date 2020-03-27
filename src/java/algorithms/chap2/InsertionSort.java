package algorithms.chap2;

import java.util.stream.IntStream;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Stopwatch;

public class InsertionSort {

	public static void sort(Comparable[] a) {
		int length = a.length;

		// text book impl
//		for (int i = 0; i < length; i++) {
//			for (int j = i; j > 0 && less(a[j], a[j-1]); j--) {
//				exchange(a, j, j-1);
//			}
//		}

		// my impl, same as text book one
//		for (int i = 0; i < length - 1; i++) {
//			for (int j = i+1; j > 0; j--) {
//				if (less(a[j], a[j-1])) {
//					exchange(a, j, j-1);
//				}else {
//					break;
//				}
//			}
//		}

		// minimize write operations than text book implementation
		for (int i = 0; i < length-1; i++) {
			int j = i + 1;
			int k = i + 1;
			while (j > 0) {
				if (less(a[k], a[j - 1])) {
					j--;
					if (j==0) {
						insert(a, a[k], j, k);
					}
				} else {
					insert(a, a[k], j, k);
					break;
				}
			}
		}
	}

	private static void insert(Comparable[] a, Comparable value, int index, int origin) {
		for (int i = origin; i >= index+1; i--) {
			a[i] = a[i - 1];
		}
		a[index] = value;
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
		for (int i = 0; i < a.length - 1; i++) {
			if (less(a[i + 1], a[i])) {
				return false;
			}
		}
		return true;
	}

	public static void print(Comparable[] a) {
		for (int i = 0; i < a.length; i++) {
			StdOut.print(a[i] + " ");
		}
		StdOut.println();
	}

	public static void main(String[] args) {
//		int[] arr = {1, 2, 43, 434, 55, 21, 3, 31};
//		int[] arr = {3, 2, 1};

//		String[] strs = {"alan", "jessica", "David", "Mary", "Gabi"};

		In in = new In("/Users/sijin.cao/git/princeton-algo/data/14Kints.txt");
		int[] arr = in.readAllInts();
		// JDK8 box
		Integer[] boxedInts = IntStream.of(arr).boxed().toArray(Integer[]::new);

//		insert(boxedInts, 31, 2, 7);
		Stopwatch timer = new Stopwatch();
		sort(boxedInts);

		StdOut.print("time used: " + timer.elapsedTime());
		StdOut.println();
		assert (isSorted(boxedInts));
		print(boxedInts);
	}

}
