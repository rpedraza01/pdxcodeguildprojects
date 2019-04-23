let candidateSearchField = document.getElementById("candidateSearchField");
let yearCandSearchselect = document.getElementById("yearCandSearchselect");
let candidateSearchBtn = document.getElementById("candidateSearchBtn");
let candidateSearchResults = document.getElementById("candidateSearchResults");
// let searchResultsdiv = document.querySelector("#searchResultsdiv");
let resultsHTML;
let apiKey;

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

		let moreInfoBtn = document.getElementsByClassName("idBtn");
		for (let i = 0; i < moreInfoBtn.length; i++) {
			moreInfoBtn[i].addEventListener("click", function() {
				candidateSearchId(this.value);
			});
		}
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("candidateSearchResults").innerHTML = message + err.message;
		}
	});
	console.log(resultsHTML);
	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCandSearchselect.value)}/candidates/search.json?query=${encodeURIComponent(candidateSearchField.value)}`;
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", apiKey);
	request.send();
	console.log(resultsHTML);
}

candidateSearchBtn.addEventListener("click", function() {
	fetch('api')
	.then(res => res.text())
	.catch(err => console.log(err))
	.then(res => {
		apiKey = res
		candidateSearch();
	})
	// console.log(yearCandSearchselect.innerHTML);
	// console.log(candidateSearchField.innerHTML);
});

function candidateSearchId(fecCandId) {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		candidateSearchResults.innerText = "Getting candidate info..."
	});

	request.addEventListener("error", function() {
		candidateSearchResults.innerText = "Info unavailable at this time, please try again later."
	});

	request.addEventListener("load", function() {
		let response;
		console.log(request.responseText);

		try {
			response = JSON.parse(request.responseText);
			candidateSearchResults.innerHTML = "";
			response.results.forEach(function(query, i) {
				console.log('query=',query);
			let commID = query.committee?query.committee.slice(12,-5):"Campaign committee not found. Please try a different Candidate ID #";
			let resultsHTML = `
			<p>Name: ${query.name}</p>
			<p>Party Affiliation: ${query.party}</p>
			<p>Office Address: ${query.mailing_address}, ${query.mailing_city}, ${query.mailing_state}, ${query.mailing_zip}</p>
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
			<button class="idBtn4" value="${commID}">Lobbyist Contributors</button>
			<button id="save${i}">Save Search</button>
			`
			let candidateSearcharticle = document.createElement("article");
			candidateSearcharticle.className = "item";
			candidateSearcharticle.innerHTML = resultsHTML;
			candidateSearchResults.appendChild(candidateSearcharticle);
			console.log(resultsHTML);
			document.getElementById(`save${i}`).addEventListener("click", function() {
				$.ajax({
					  method: "POST",
					  url: "/ajax/save_search/",
					  data: JSON.stringify(query),
					  // contentType: "application/json",
					  processData: false
					})
					  .done(function( msg ) {
					    alert( "Data Saved: " + msg );
					  });
				})
			});

		let lobInfoBtn2 = document.getElementsByClassName("idBtn4");
			for (let i = 0; i < lobInfoBtn2.length; i++) {
			lobInfoBtn2[i].addEventListener("click", function() {
				lobbyistSearch2(this.value);
			});
		}
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("candidateSearchResults").innerHTML = message + err.message;
		}
	});

	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCandSearchselect.value)}/candidates/${encodeURIComponent(fecCandId)}.json`;
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", apiKey);
	request.send();
}

function lobbyistSearch2(fecLobId2) {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		candidateSearchResults.innerText = "Getting committee info..."
	});

	request.addEventListener("error", function() {
		candidateSearchResults.innerText = "Info unavailable at this time, please try again later."
	});

	request.addEventListener("load", function() {
		console.log(request);
		let response;
		console.log(request.responseText);

	try {
			response = JSON.parse(request.responseText);
				// console.log(response);
			candidateSearchResults.innerHTML = "";
			response.results.forEach(function(query) {
			resultsHTML =`
			<p>Filing ID#: ${query.fec_filing_id}</p>
			<p>Transaction ID #: ${query.transaction_id}</p>
			<p>Entity Type: ${query.entity_type}</p>
			<p>Lobbyist Organization: ${query.bundler_organization_name}</p>
			<p>Lobbyist Name: ${query.bundler_first_name} ${query.bundler_last_name}</p>
			<p>Lobbyist Address: ${query.bundler_street_1}, ${query.bundler_city}, ${query.bundler_state}, ${query.bundler_zip}</p>
			<p>Lobbyist Employer: ${query.bundler_employer}</p>
			<p>Lobbyist Occupation: ${query.bundler_occupation}</p>
			<p>Amount Contributed: $${query.bundled_amount}</p>
			<p>This Information Was First Gathered: ${query.start_date}</p>
			<p>This Information Was Finalized: ${query.end_date}</p>
			`
			console.log(resultsHTML);
			let lobbyistSearcharticle2 = document.createElement("article");
			lobbyistSearcharticle2.className = "item";
			lobbyistSearcharticle2.innerHTML = resultsHTML;
			candidateSearchResults.appendChild(lobbyistSearcharticle2);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("candidateSearchResults").innerHTML = message + err.message;
		}
	});

	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCandSearchselect.value)}/committees/${encodeURIComponent(fecLobId2)}/lobbyist_bundlers.json`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", apiKey);
	request.send();
}