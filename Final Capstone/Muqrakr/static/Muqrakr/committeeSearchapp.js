let committeeSearchField = document.getElementById("committeeSearchField");
let yearCommSearchselect = document.getElementById("yearCommSearchselect");
let committeeSearchBtn = document.getElementById("committeeSearchBtn");
let committeeSearchResults = document.getElementById("committeeSearchResults");
// let searchResultsdiv2 = document.querySelector("#searchResultsdiv2");
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
		let moreInfoBtn2 = document.getElementsByClassName("idBtn2");
		for (let i = 0; i < moreInfoBtn2.length; i++) {
			moreInfoBtn2[i].addEventListener("click", function() {
				committeeSearchId(this.value);
			});
		}
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

function committeeSearchId(fecCommId) {
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
		console.log(request.responseText);

	try {
			response = JSON.parse(request.responseText);
				console.log(response);
			committeeSearchResults.innerHTML = "";
			response.results.forEach(function(query, i) {
				// console.log(query.id);
			resultsHTML2 = `
			<p>Committee Name: ${query.name}</p>
			<p>Party Affiliation: ${query.party}</p>
			<p>Committee Treasurer: ${query.treasurer}</p>
			<p>Committee Address: ${query.address}, ${query.city}, ${query.state}, ${query.zip}</p>
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
			<button class="idBtn3" value="${query.id}">Lobbyist Bundlers</button>
			<button id="save${i}">Save Search</button>
			`
			console.log(resultsHTML2);
				let committeeSearcharticle = document.createElement("article");
				committeeSearcharticle.className = "item";
				committeeSearcharticle.innerHTML = resultsHTML2;
				committeeSearchResults.appendChild(committeeSearcharticle);
				document.getElementById(`save${i}`).addEventListener("click", function() {
				$.ajax({
					  method: "POST",
					  url: "/ajax/save_search_committee/",
					  data: JSON.stringify(query),
					  // contentType: "application/json",
					  processData: false
					})
					  .done(function( msg ) {
					    alert( "Data Saved: " + msg );
					  });
				})
			});
			let lobInfoBtn = document.getElementsByClassName("idBtn3");
			for (let i = 0; i < lobInfoBtn.length; i++) {
			lobInfoBtn[i].addEventListener("click", function() {
				lobbyistSearch(this.value);
			});
		}
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("committeeSearchResults").innerHTML = message + err.message;
		}
	});

	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCommSearchselect.value)}/committees/${encodeURIComponent(fecCommId)}.json`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

function lobbyistSearch(fecLobId) {
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
		console.log(request.responseText);

	try {
			response = JSON.parse(request.responseText);
				console.log(response);
			committeeSearchResults.innerHTML = "";
			response.results.forEach(function(query) {
			resultsHTML2 =`
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
			console.log(resultsHTML2);
			let lobbyistSearcharticle = document.createElement("article");
			lobbyistSearcharticle.className = "item";
			lobbyistSearcharticle.innerHTML = resultsHTML2;
			committeeSearchResults.appendChild(lobbyistSearcharticle);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("committeeSearchResults").innerHTML = message + err.message;
		}
	});

	let url = `https://api.propublica.org/campaign-finance/v1/${encodeURIComponent(yearCommSearchselect.value)}/committees/${encodeURIComponent(fecLobId)}/lobbyist_bundlers.json`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}