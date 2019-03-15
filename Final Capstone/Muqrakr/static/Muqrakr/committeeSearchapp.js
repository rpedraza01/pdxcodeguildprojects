let campidSearchField = document.getElementById("campidSearchField");
let yearCommSearchselect = document.getElementById("yearCommSearchselect");
let campidSearchBtn = document.getElementById("campidSearchBtn");
let campidSearchResults = document.getElementById("campidSearchResults");




	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCommSearchselect.value)}/committees/${encodeURIComponent(campidSearchField.value)}.json`;
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();


campidSearchBtn.addEventListener("click", function() {
	candidateId();
});