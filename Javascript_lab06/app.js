let watchDate = new Date()
	watchDate.setHours(0,0,0,0);
let startWatchtime = setInterval(watchTime, 1000);
function watchTime() {
	let stopwatchDisplay = document.getElementById("stopwatchDisplay");
	let watchHours = watchDate.getHours();
	let watchMinutes = watchDate.getMinutes();
	let watchSeconds = watchDate.getSeconds();
		// watchSeconds = setInterval(function() {
	watchDate.setSeconds(watchDate.getSeconds() + 1);
				// watchTime(watchSeconds);
		// }, 1000);
	console.log(watchSeconds);
	stopwatchDisplay.innerHTML = watchHours + " hours : " + watchMinutes + " minutes : " + watchSeconds + " seconds";
	// setTimeout(watchTime(), 1000);
}

let startBtn = document.getElementById("start");
	startBtn.innerText = "Start";
	startBtn.addEventListener("click", function() {

	});

let lapTimesul = document.createElement("ul");
let lapLi = document.createElement("li");
let lapBtn = document.getElementById("lap");
	lapBtn.innerText = "Lap";
	lapBtn.addEventListener("click", function() {
		lapTimesul.appendChild(lapLi);

	});

watchTime();