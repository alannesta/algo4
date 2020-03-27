package algorithms.misc;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class MergeIntervals {

    static class Interval implements Comparable {
        public int start;
        public int end;

        Interval(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public String toString() {
            return "[" + start + ", " + end + "]";
        }


        @Override
        public int compareTo(Object o) {
            return start - Interval.class.cast(o).start;
        }
    }

    private static boolean isMergeable(Interval A, Interval B) {
        return A.end >= B.start && A.start <= B.start;
    }

    private static Interval merge(Interval A, Interval B) {
        return new Interval(Math.min(A.start, B.start), Math.max(A.end, B.end));
    }

    public static void main(String[] args) {
        List<Interval> intervals = Arrays.asList(new Interval(2, 6), new Interval(15, 18), new Interval(5, 10),new Interval(16, 20), new Interval(22, 33), new Interval(23, 34), new Interval(1, 3));

        List<Interval> results = new ArrayList<>();

        Collections.sort(intervals);

        for (Interval interval : intervals) {
            if (results.size() == 0) {
                results.add(interval);
                continue;
            }
            if (isMergeable(results.get(results.size() - 1), interval)) {
                results.set(results.size() - 1, merge(results.get(results.size() - 1), interval));
            } else {
                results.add(interval);
            }
        }

        System.out.println(results);

    }
}

