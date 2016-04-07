package com.alan.algorithms.chap1;


import java.util.Iterator;

public class LinkedListStack<Item> implements Iterable<Item> {

	Node first;
	int n = 0;        // size of the stack

	public void push(Item item) {
		Node old = first;
		first = new Node();
		first.item = item;
		first.next = old;
		n++;
	}

	public Item pop() {
		Item item = first.item;
		first = first.next;
		n--;
		return item;
	}

	public boolean isEmpty() {
		return n == 0;
	}

	public int size() {
		return n;
	}

	@Override
	public StackIterator iterator() {
		return new StackIterator();
	}

	private class StackIterator implements Iterator<Item> {
		Node head = first;

		@Override
		// Returns true if the iteration has more elements.
		// (In other words, returns true if next() would return an element rather than throwing an exception.)
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

	private class Node {
		private Node next;
		private Item item;
	}
}

