let committeeSearchField = document.getElementById("committeeSearchField");
let yearCommSearchselect = document.getElementById("yearCommSearchselect");
let committeeSearchBtn = document.getElementById("committeeSearchBtn");
let committeeSearchResults = document.getElementById("committeeSearchResults");
let searchResultsdiv2 = document.querySelector("#searchResultsdiv2");
let resultsHTML2;

function committeeSearch() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		committeeSearchResults.innerText = "Getting committee info..."
	});

	request.addEventListener("error", function() {
		committeeSearchResults.innerText = "Info unavailable at this time, please try again later."
	});

	request.addEventListener("load", function() {
		console.log(request);
		let response;

		try {
			response = JSON.parse(request.responseText);
				console.log(response);
			committeeSearchResults.innerHTML = "";
			response.results.forEach(function(query) {
				console.log(query.id);
			resultsHTML2 = `
				<p><button class="idBtn2" value="${query.id}">More Info</button>  ${query.name} | ${query.party} | ${query.treasurer} | ${query.address}, ${query.city}, ${query.state}, ${query.zip}</p>
			`
			console.log(resultsHTML2);
				let committeeSearcharticle = document.createElement("article");
				committeeSearcharticle.className = "item";
				committeeSearcharticle.innerHTML = resultsHTML2;
				committeeSearchResults.appendChild(committeeSearcharticle);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("committeeSearchResults").innerHTML = message + err.message;
		}
	});
	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCommSearchselect.value)}/committees/search.json?query=${encodeURIComponent(committeeSearchField.value)}`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

committeeSearchBtn.addEventListener("click", function() {
	committeeSearch();
});

function committeeSearchId() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		committeeSearchResults.innerText = "Getting committee info..."
	});

	request.addEventListener("error", function() {
		committeeSearchResults.innerText = "Info unavailable at this time, please try again later."
	});

	request.addEventListener("load", function() {
		console.log(request);
		let response;

	try {
			response = JSON.parse(request.responseText);
				console.log(response);
			committeeSearchResults.innerHTML = "";
			response.results.forEach(function(query) {
				console.log(query.id);
			resultsHTML2 = `
			<p>Total Receipts: $${query.total_receipts}</p>
			<p>Total Contributions From Individuals: $${query.total_from_individuals}</p>
			<p>Total Contributions From PACs: $${query.total_from_pacs}</p>
			<p>Total Contributions: $${query.total_contributions}</p>
			<p>Total Disbursements: $${query.total_disbursements}</p>
			<p>Beginning Cash: $${query.begin_cash}</p>
			<p>Ending Cash: $${query.end_cash}</p>
			<p>Total Refunds: $${query.total_refunds}</p>
			<p>Debts Owed: $${query.debts_owed}</p>
			<p>Total Independent Expenditures: $${query.total_independent_expenditures}</p>
			<p>Total Candidate Contributions: $${query.total_candidate_contributions}</p>
			<p>This Information Was First Gathered: ${query.date_coverage_from}</p>
			<p>This Information Was Finalized: ${query.date_coverage_to}</p>
			`
			console.log(resultsHTML2);
				let committeeSearcharticle = document.createElement("article");
				committeeSearcharticle.className = "item";
				committeeSearcharticle.innerHTML = resultsHTML2;
				committeeSearchResults.appendChild(committeeSearcharticle);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("committeeSearchResults").innerHTML = message + err.message;
		}
	});

	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(committeeSearch(yearCommSearchselect.value))}/committees/${encodeURIComponent(committeeSearch(committeeSearchField.value))}.json`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

searchResultsdiv2.addEventListener("click", function(e) {
	if (e.target && e.target.matches("button.idBtn2")) {
		return;
		console.log(searchResultsdiv2);
	}
		committeeSearchId();
});