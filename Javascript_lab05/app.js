var urlLinks = ["http://www.espn.com/", "https://splinternews.com/", "https://www.recode.net/", "https://www.reddit.com/", "https://kotaku.com/", "https://www.reddit.com/r/ToiletPaperUSA/", "https://www.nba.com/blazers/", "https://techcrunch.com/"];

function randomPick() {
	var i = parseInt(Math.random() * urlLinks.length);
	location.href = urlLinks[i];
}

// setTimeout(function() {
// 	alert("Redirecting...");
// 	randomPick();
// }, 5000);

var timeSeconds = 5;
var timer = setInterval(function() {
	document.getElementById("countdown").innerHTML = timeSeconds + " seconds";
	timeSeconds -= 1;
	if(timeSeconds <= 0)
		randomPick(timer);
}, 1000);
