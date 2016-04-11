package com.alan.algorithms.chap1;


import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.Stopwatch;
import edu.princeton.cs.algs4.ThreeSum;

public class DoublingTest {
	private static final int MAXIMUM_INTEGER = 1000000;

	// This class should not be instantiated.
	private DoublingTest() { }

	/**
	 * Returns the amount of time to call <tt>ThreeSum.count()</tt> with <em>N</em>
	 * random 6-digit integers.
	 * @param N the number of integers
	 * @return amount of time (in seconds) to call <tt>ThreeSum.count()</tt>
	 *   with <em>N</em> random 6-digit integers
	 */
	public static double timeTrial(int N) {
		In in = new In("/Users/sijin.cao/git/princeton-algo/data/8Kints.txt");
		int[] a = in.readAllInts();

//		int[] a = new int[N];

// 		for (int i = 0; i < N; i++) {
//			a[i] = StdRandom.uniform(-MAXIMUM_INTEGER, MAXIMUM_INTEGER);
//		}
		Stopwatch timer = new Stopwatch();
		ThreeSumFast.count(a);
//		TreeSum.count(a);
		return timer.elapsedTime();
	}

	/**
	 * Prints table of running times to call <tt>ThreeSum.count()</tt>
	 * for arrays of size 250, 500, 1000, 2000, and so forth.
	 */
	public static void main(String[] args) {
//		for (int N = 250; true; N += N) {
//			double time = timeTrial(N);
//			StdOut.printf("%7d %5.1f\n", N, time);
//		}
		double time = timeTrial(4000);
		StdOut.printf("%7d %5.1f\n", 4000, time);
	}
}
