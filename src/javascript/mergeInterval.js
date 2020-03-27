/*
 https://leetcode.com/problems/merge-intervals/description/
 Given a collection of intervals, merge all overlapping intervals.

 Example 1:

 Input: [[1,3],[2,6],[8,10],[15,18]]
 Output: [[1,6],[8,10],[15,18]]
 Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

 Example 2:

 Input: [[1,4],[4,5]]
 Output: [[1,5]]
 Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

 hint:
 classic two pointer solution

*/


function Interval(start, end) {
	this.start = start;
	this.end = end;
}

var interval1 = new Interval(1, 3);
var interval2 = new Interval(2, 6);
var interval3 = new Interval(5, 10);
var interval4 = new Interval(15, 18);
var interval5 = new Interval(16, 20);
var interval6 = new Interval(22, 33);
var interval7 = new Interval(23, 34);

var intervals = [interval6, interval1, interval4, interval2, interval3, interval5, interval6, interval7];

function mergeInterval(intervalArr) {
	var i = 0;

	intervalArr.sort((interval1, interval2) => {
		return interval1.start - interval2.start;
	});

	for (var j = 1; j < intervalArr.length; ) {
		if(isMergeable(intervalArr[i], intervalArr[j])) {
			intervalArr[i] = merge(intervalArr[i], intervalArr[j]);
			intervalArr[j] = null;
			j++
		} else {
			i = j;
			j++;
		}
	}
	console.log(intervalArr);
	return intervalArr.filter(t => t != null);
}


function isMergeable(intervalA, intervalB) {
	return intervalA.end >= intervalB.start && intervalA.start <= intervalB.start;
}

function merge(intervalA, intervalB) {
	return new Interval(Math.min(intervalA.start, intervalB.start), Math.max(intervalA.end, intervalB.end));
}


console.log(mergeInterval(intervals));
