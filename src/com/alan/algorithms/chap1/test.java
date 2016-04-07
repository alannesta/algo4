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
		stack.pop();
		stack.push("Kaka5");
		stack.push("Kaka6");

//		stack.list();
		System.out.println(stack.size());
		for (String s:stack ) {
			System.out.println(s);
		}
    }
}
