package algorithms.data_structure;

/**
 * https://leetcode.com/problems/merge-k-sorted-lists/
 * <p>
 * Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
 * <p>
 * Example:
 * <p>
 * Input:
 * [
 * 1->4->5,
 * 1->3->4,
 * 2->6
 * ]
 * Output: 1->1->2->3->4->4->5->6
 */


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class MergeKSortedList {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        ListNode mergedHead = new ListNode();
        ListNode cursor = mergedHead;

        PriorityQueue<ListNode> minHeap = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        });

        //meanHeap.addAll(Arrays.asList(lists));
        for (ListNode listHead : lists) {
            if (listHead != null) {
                minHeap.add(listHead);
            }
        }

        while (minHeap.peek() != null) {
            ListNode minNode = minHeap.poll();
            if (minNode != null) {
                if (mergedHead != null) {
                    cursor.next = minNode;
                    cursor = cursor.next;
                } else {
                    cursor = mergedHead.next = minNode;
                }
            }
            if (minNode.next != null) {
                minHeap.add(minNode.next);
            }
        }

        return mergedHead.next;
    }

    private static ArrayList<ListNode> buildLists() {

        ArrayList<ListNode> result = new ArrayList<>();
        int lists[][] = {{1, 3, 6, 12, 33, 55}, {2, 4, 6, 20, 22, 66}, {3, 9, 10, 18, 41, 42}};

        for (int[] list : lists) {
            ListNode head = null;
            ListNode cursor = null;

            for (int i : list) {
                if (head != null) {
                    cursor.next = new ListNode(i);
                    cursor = cursor.next;
                } else {
                    head = new ListNode(i);
                    cursor = head;
                }
            }
            result.add(head);
        }

        return result;
    }

    public static void main(String[] args) {
        ArrayList<ListNode> res = buildLists();
        ListNode kaka[] = new ListNode[res.size()];
        kaka = res.toArray(kaka);
        MergeKSortedList msl = new MergeKSortedList();
        ListNode result = msl.mergeKLists(kaka);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
        //System.out.print(res);
    }
}


class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}