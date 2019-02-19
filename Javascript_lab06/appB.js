function addNum(i) {
	if (i < 10) {
		i = "0" + i;
	}
	return i;
}

let date = new Date();
let timeSeconds = setInterval(time, 1000);
function time() {
	let dateTimedisplay = document.getElementById("clockDisplay");
	let hours = addNum(date.getHours());
	let minutes = addNum(date.getMinutes());
	let seconds = addNum(date.getSeconds());
	date.setSeconds(date.getSeconds() + 1);
	// console.log(seconds);
	dateTimedisplay.innerHTML = hours + " : " + minutes + " : " + seconds;
}

time();