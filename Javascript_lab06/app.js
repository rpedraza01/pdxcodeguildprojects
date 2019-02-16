function addNum(i) {
	if (i < 10) {
		i = "0" + i;
	}
	return i;
}

// function time() {
let date = new Date();
let dateTimedisplay = document.getElementById("clockDisplay");
dateTimedisplay.addEventListener("onload", function() {

});
let hours = addNum(date.getHours());
let minutes = addNum(date.getMinutes());
let seconds = addNum(date.getSeconds());
	let timeSeconds = 0;
	let tSeconds = setInterval(function() {
		timeSeconds += 1;
			date(seconds);
	}, 1000);
dateTimedisplay.innerHTML = hours + " : " + minutes + " : " + seconds;
// }

// function watchTime() {
let watchDate = new Date()
watchDate.setHours(0,0,0,0);
let stopwatchDisplay = document.getElementById("stopwatchDisplay");
stopwatchDisplay.addEventListener("onload", function() {

});
let watchHours = watchDate.getHours();
let watchMinutes = watchDate.getMinutes();
let watchSeconds = watchDate.getSeconds();
	let time_watchSeconds = 0;
	let twatchSeconds = setInterval(function() {
		time_watchSeconds += 1;
			watchDate(watchSeconds);
	}, 1000);
let watchMilliseconds = watchDate.getMilliseconds();
stopwatchDisplay.innerHTML = watchHours + " : " + watchMinutes + " : " + watchSeconds + " : " + watchMilliseconds;
// }