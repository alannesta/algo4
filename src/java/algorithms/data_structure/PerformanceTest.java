package algorithms.data_structure;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.TreeMap;

public class PerformanceTest {
    private ArrayList<Map<Integer, Integer>> randomKeyValPairs = new ArrayList<>();
    private TreeMap<Integer, Integer> treeMap = new TreeMap<>();
    private HashMap<Integer, Integer> hashMap = new HashMap<>();

    private static int MAX = 100 * 100 * 100;

    PerformanceTest(int size) {
        Random rand = new Random();

        // Obtain a number between [0 - 49].
        for (int i = 0; i < size; i++) {
            treeMap.put(rand.nextInt(MAX), rand.nextInt(MAX));
            hashMap.put(rand.nextInt(MAX), rand.nextInt(MAX));
        }

    }

    public static void main(String[] args) {
        Random rand = new Random();
        int ITERATIONS = 100 * 100 * 100;
        PerformanceTest test = new PerformanceTest(10000);
        System.out.println(test.treeMap.keySet());
        System.out.println(test.hashMap.keySet());
        long currentTime = System.currentTimeMillis();
        for (int i = 0; i < ITERATIONS; i++) {
            // test.treeMap.remove(rand.nextInt(MAX));
            // test.treeMap.put(rand.nextInt(MAX), rand.nextInt(MAX));
            test.treeMap.get(rand.nextInt(MAX));
        }
        System.out.println("Time used: " + Long.toString(System.currentTimeMillis() - currentTime));

        currentTime = System.currentTimeMillis();
        for (int i = 0; i < ITERATIONS; i++) {
            // test.treeMap.remove(rand.nextInt(MAX));
            // test.treeMap.put(rand.nextInt(MAX), rand.nextInt(MAX));
            test.hashMap.get(rand.nextInt(MAX));
        }
        System.out.println("Time used: " + Long.toString(System.currentTimeMillis() - currentTime));
    }
}


