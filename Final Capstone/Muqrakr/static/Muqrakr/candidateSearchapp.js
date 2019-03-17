let candidateSearchField = document.getElementById("candidateSearchField");
// let idBtn = document.getElementsByClassName("idBtn");
let yearCandSearchselect = document.getElementById("yearCandSearchselect");
let candidateSearchBtn = document.getElementById("candidateSearchBtn");
let candidateSearchResults = document.getElementById("candidateSearchResults");
let searchResultsdiv = document.querySelector("#searchResultsdiv");
let resultsHTML;

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

		try {
		response = JSON.parse(request.responseText);
			console.log(response);
		candidateSearchResults.innerHTML = "";
		response.results.forEach(function(query) {
			console.log(query.candidate.id);
		resultsHTML = `
		<p><button class="idBtn" value="${query.candidate.id}">More Info</button>   ${query.candidate.name} | ${query.candidate.party}</p>
		`
		console.log(resultsHTML);
			let candidateSearcharticle = document.createElement("article");
			candidateSearcharticle.className = "item";
			candidateSearcharticle.innerHTML = resultsHTML;
			candidateSearchResults.appendChild(candidateSearcharticle);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("candidateSearchResults").innerHTML = message + err.message;
		}
	});
	console.log(resultsHTML);
	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCandSearchselect.value)}/candidates/search.json?query=${encodeURIComponent(candidateSearchField.value)}`;
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
	console.log(resultsHTML);
}

candidateSearchBtn.addEventListener("click", function() {
	candidateSearch();
	console.log(yearCandSearchselect.innerHTML);
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
			response = JSON.parse(request.responseText);
			candidateSearchResults.innerHTML = "";
			response.results.forEach(function(query) {
				console.log(query.candidate.id);
			let resultsHTML = `
			<p>Name: ${query.first_name} ${query.last_name}</p>
			<p>Date of Birth: ${query.date_of_birth}</p>
			<p>Gender: ${query.gender}</p>
			<p>URL: <a href="${query.url}">${query.url}</a></p>
			<p>Positon: ${query.title}, 
			<p>State and District: ${query.state} ${query.district}</p>
			<p>Party Affiliation: ${query.current_party}</p>
			<p>Congressional Office Phone #: ${query.phone}</p>
			<p>Bills Sponsored: ${query.bills_sponsored}</p>
			<p>Bills Cosponsored: ${query.bills_cosponsored}</p>
			<p>Missed Votes %: ${query.missed_votes_pct}%</p>
			<p>Votes with Party %: ${query.votes_with_party_pct}%</p>
			<p>Total Receipts: $${query.total_receipts}</p>
			<p>Total Contributions From Individuals: $${query.total_from_individuals}</p>
			<p>Total Contributions From PACs: $${query.total_from_pacs}</p>
			<p>Total Contributions: $${query.total_contributions}</p>
			<p>Total Loans: $${query.candidate_loans}</p>
			<p>Total Disbursements: $${query.total_disbursements}</p>
			<p>Beginning Cash on Hand: $${query.begin_cash}</p>
			<p>Ending Cash On Hand: $${query.end_cash}</p>
			<p>Total Refunds: $${query.total_refunds}</p>
			<p>Debts Owed: $${query.debts_owed}</p>
			<p>Independent Expenditures: $${query.independent_expenditures}</p>
			<p>Coordinated Expenditures: $${query.coordinated_expenditures}</p>
			<p>This Information Was First Gathered: ${query.date_coverage_from}</p>
			<p>This Information Was Finalized: ${query.date_coverage_to}</p>
			`
			let candidateSearcharticle = document.createElement("article");
			candidateSearcharticle.className = "item";
			candidateSearcharticle.innerHTML = resultsHTML;
			candidateSearchResults.appendChild(candidateSearcharticle);
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

searchResultsdiv.addEventListener("click", function(e) {
	if (e.target && e.target.matches("button.idBtn")) {
		return;
		console.log(searchResultsdiv);
	}
		candidateSearchId();
});