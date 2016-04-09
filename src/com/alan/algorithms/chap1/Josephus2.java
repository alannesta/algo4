package com.alan.algorithms.chap1;

import edu.princeton.cs.algs4.StdOut;

public class Josephus2 {
    public static void main(String[] args) {
//        int M = Integer.parseInt(args[0]);
//        int N = Integer.parseInt(args[1]);
        int M = 2;
        int N = 27;

        // initialize the queue
        LinkedListQueue<Integer> q = new LinkedListQueue<Integer>();
        for (int i = 0; i < N; i++) {
            q.push(i);
        }
        while (q.size>0) {
            for (int i = 0; i < M-1; i++) {
                q.push(q.pop());
            }
            StdOut.print(q.pop() + " ");
        }
        StdOut.println();
    }
}
