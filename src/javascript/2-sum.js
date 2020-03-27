/*
 Given an array of integers, return indices of the two numbers such that they add up to a specific target.

 You may assume that each input would have exactly one solution, and you may not use the same element twice.

 Leetcode的第一题...
 */


//  time: O(n2), space: O(1)
function twoSums(arr, target) {
	for (var i = 0; i < arr.length; i++) {
		var subTarget = target - arr[i];
		for (var j = 1; j < arr.length; j++) {
			if (arr[j] === subTarget) {
				console.log([i, j]);
				return [i, j];
			}
		}
	}
}

//  time: O(n), space: O(n)
function twoSumsV2(arr, target) {
	var map = new Map();
	for (var i = 0; i < arr.length; i++) {
		map.set(target - arr[i], i);
	}
	for (var j = 0; j < arr.length; j++) {
		if (map.has(arr[j])) {
			console.log([map.get(arr[j]), j]);
			return [map.get(arr[j]), j];
		}
	}
}

var arr = [2, 7, 11, 15, 23, 8, 1, 0, 12];

twoSums(arr, 23);
twoSumsV2(arr, 23);