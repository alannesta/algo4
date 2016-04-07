package com.alan.algorithms.chap1;

import java.util.Iterator;

public class ResizableArrayStack<Item> implements Iterable<Item> {

	private int count = 0;	// count of items in the stack
	private Item[] stack = (Item[])new Object[1];	// initalize an array of size 1

	public ResizableArrayStack() {

	}

	public Item pop() {
		int length = stack.length;
		if (count > 0 && count <= length/4) {
			resize(length/2);
		}
		Item poped = stack[count-1];
		stack[count-1] = null;
		count--;
		return poped;
	}

	public void push(Item item) {
		if ((++count) > stack.length) {
			resize(2*stack.length);
		}
		stack[count-1] = item;
	}

	public void list() {
		for (int i=0; i<count; i++) {
			System.out.println(stack[i].toString());
		}
	}

	private void resize(int size) {
		Item[] temp = (Item[]) new Object[size];
		for (int i=0; i<stack.length; i++) {
			temp[i] = stack[i];
		}
		stack = temp;
	}


	@Override
	public Iterator<Item> iterator() {
		return new StackIterator();
	}

	private class StackIterator implements Iterator<Item> {

		private int i = count;

		@Override
		public boolean hasNext() {
			return i > 0;
		}

		@Override
		public Item next() {
			return stack[--i];
		}
	}
}
