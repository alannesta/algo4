package com.alan.algorithms.chap1;

public class Josephus {
    private LinkedListQueue<Integer> guests = new LinkedListQueue();
    private LinkedListQueue<Integer> eliminated = new LinkedListQueue();
    private int step;

    public Josephus(int N, int M) {
        for (int i=0; i<N; i++) {
            guests.push(i);
        }
        step = M;
    }

    public LinkedListQueue<Integer> calculate() {
        LinkedListQueue<Integer> stay;
        int position = 1;
        while(guests.size()>step-1) {
            stay = new LinkedListQueue();
            for (Integer i: guests) {
                if (position % step == 0) {
                    eliminated.push(i);
                } else {
                    stay.push(i);
                }
                position++;
            }
            guests = stay;
        }
        return guests;
    }

    public void list(LinkedListQueue<Integer> queue) {
        for (Integer i: queue) {
            System.out.print(i + ", ");
        }
    }


    public static void main(String[] args) {
        Josephus sanJose = new Josephus(27, 2);
        LinkedListQueue lastguy = sanJose.calculate();
        System.out.println("Eliminated");
        sanJose.list(sanJose.eliminated);
        System.out.println("\nLast guys standing: ");
        sanJose.list(sanJose.guests);

    }


}
