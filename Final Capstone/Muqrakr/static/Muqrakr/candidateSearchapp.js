let candidateSearchField = document.getElementById("candidateSearchField");
// let input = document.querySelector("#candidateSearchField"),
// 	data = input.dataset;

// let candsearch = document.getAttribute("data-candsearch");

let yearCandSearchselect = document.getElementById("yearCandSearchselect");
let candidateSearchBtn = document.getElementById("candidateSearchBtn");
let candidateSearchResults = document.getElementById("candidateSearchResults");

function candidateSearch() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		candidateSearchResults.innerText = "Getting candidate info..."
	});

	request.addEventListener("error", function() {
		candidateSearchResults.innerText = "Info unavailable at this time, please try again later."
	});

	request.addEventListener("load", function() {
		console.log(request);
		let response;
		// console.log(response);

		try {
			response.JSON.parse(request.responseText);
			candidateSearchResults.innerHTML = "";
			response.results.forEach(function(query) {
				console.log(query.candidate.id);
				console.log(query.committee);
			let resultsHTML = query.candidate.id;
			// , {query.committee};

			console.log(resultsHTML);
			// let candidateSearchP = document.createElement("p");
			// candidateSearchP.className = "item";
			// candidateSearchP.innerHTML = resultsHTML;
			// candidateSearchResults.appendChild(candidateSearchP);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("candidateSearchResults").innerHTML = message + err.message;
		}
	});
	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCandSearchselect.value)}/candidates/search.json?query=${encodeURIComponent(candidateSearchField.value)}`;
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

candidateSearchBtn.addEventListener("click", function() {
	candidateSearch();
	console.log(yearCandSearchselect);
	console.log(candidateSearchField.innerHTML);
});

function candidateSearchId() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		candidateSearchResults.innerText = "Getting candidate info..."
	});

	request.addEventListener("error", function() {
		candidateSearchResults.innerText = "Info unavailable at this time, please try again later."
	});

	request.addEventListener("load", function() {
		let response;
		console.log(response);

		try {
			response.JSON.parse(request.responseText);
			candidateSearchResults.innerHTML = "";
			response.results.forEach(function(query) {
				console.log(query.candidate.id);
			let resultsHTML = `
			<p>Name: ${query.results.first_name} ${query.results.last_name}</p>
			<p>Date of Birth: ${query.results.date_of_birth}</p>
			<p>Gender: ${query.results.gender}</p>
			<p>URL: <a href="${query.results.url}">${query.results.url}</a></p>
			<p>Positon: ${query.roles.title}, 
			<p>State and District: ${query.results.state} ${query.results.district}</p>
			<p>Party Affiliation: ${query.results.current_party}</p>
			<p>Congressional Office Phone #: ${query.roles.phone}</p>
			<p>Bills Sponsored: ${query.roles.bills_sponsored}</p>
			<p>Bills Cosponsored: ${query.roles.bills_cosponsored}</p>
			<p>Missed Votes %: ${query.roles.missed_votes_pct}%</p>
			<p>Votes with Party %: ${query.roles.votes_with_party_pct}%</p>
			`
			console.log(resultsHTML);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("candidateSearchResults").innerHTML = message + err.message;
		}
	});

	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(candidateSearch(yearCandSearchselect.value))}/candidates/${encodeURIComponent(candidateSearch(candidateSearchField.value))}.json`;
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}