let watchDate = new Date();
	watchDate.setHours(0,0,0,0);
// let startWatchtime = setInterval(watchTime, 1000);
function watchTime() {
	let stopwatchDisplay = document.getElementById("stopwatchDisplay");
	let watchHours = watchDate.getHours();
	let watchMinutes = watchDate.getMinutes();
	let watchSeconds = watchDate.getSeconds();
	watchDate.setSeconds(watchDate.getSeconds() + 1);
	// console.log(watchSeconds);
	stopwatchDisplay.innerHTML = watchHours + " hours : " + watchMinutes + " minutes : " + watchSeconds + " seconds";
}

let startBtn = document.getElementById("start");
	startBtn.innerText = "Start";
	startBtn.addEventListener("click", function() {
		startBtn = setInterval(watchTime, 1000);
	});

let stopBtn = document.getElementById("stop");
	stopBtn.innerText = "Stop";
	stopBtn.addEventListener("click", function() {
		stopBtn = clearInterval(startBtn);

	});

let lapNum = 1;
let lap = document.getElementById("lap");
lap.innerHTML = "Lap";
let lapTimes = document.getElementById("lapTimes");
lap.addEventListener("click", function(watchTime) {
	// let 
	lapTimes.innerHTML += `<li> Lap ${lapNum}: ${stopwatchDisplay.innerHTML} </li>`;
	lapNum += 1;
});

watchTime();