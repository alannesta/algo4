package com.alan.algorithms.chap1;

public class test {
	public static void main(String[] args) {
//		ResizableArrayStack<String> stack = new ResizableArrayStack<String>();
		LinkedListStack<String> stack = new LinkedListStack<>();


		stack.push("Kaka");
		stack.pop();
//		stack.pop();
//		stack.pop();
		stack.push("Kaka1");
		stack.push("Kaka2");
//		stack.pop();
		stack.push("Kaka3");
		stack.push("Kaka4");
//		stack.pop();
		stack.push("Kaka5");
//		stack.push("Kaka6");

//		stack.list();
//		System.out.println(stack.size());
//		for (String s:stack ) {
//			System.out.println(s);
//		}

		LinkedListQueue<Integer> queue = new LinkedListQueue<Integer>();
		queue.push(1);
		queue.pop();
		queue.push(3);
		queue.push(5);
		queue.push(7);
		queue.pop();

		queue.push(9);
//		queue.pop();
//		System.out.println(queue.size());
		for (Integer i:queue) {
			System.out.println(i);
		}

    }
}
