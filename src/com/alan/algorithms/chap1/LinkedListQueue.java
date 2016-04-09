package com.alan.algorithms.chap1;

import java.util.Iterator;

public class LinkedListQueue<Item> implements Iterable<Item> {

    Node first;
    Node last;
    int size = 0;

    public void push(Item item) {
        if (last != null) {
            Node old = last;
            last = new Node();
            last.item = item;
            old.next = last;
        }else {
            first = last = new Node();
            last.item = item;
        }

        size++;
    }

    public Item pop() {
        Item result = first.item;
        if (first != last) {
            first = first.next;
        }else {
            first = last = null;
        }
        size--;
        return result;
    }

    public int size() {
        return size;
    }

    @Override
    public Iterator iterator() {
        return new LinkedListIterator();
    }

    class Node {
        Node next;
        Item item;
    }

    private class LinkedListIterator implements Iterator<Item> {
        Node head = first;

        @Override
        public boolean hasNext() {
            return head != null;
        }

        @Override
        public Item next() {
            Item item = head.item;
            head = head.next;
            return item;
        }
    }
}
