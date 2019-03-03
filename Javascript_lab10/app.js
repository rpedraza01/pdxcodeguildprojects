let idSearchField = document.getElementById("idSearchField");
let idSearchBtn = document.getElementById("idSearchBtn");
let idSearchResults = document.getElementById("idSearchResults");

function candidateId() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		// console.log(loaded);
		idSearchResults.innerText = "Getting candidate IDs...";
	});

	request.addEventListener("error", function() {
		console.log(status);
		idSearchResults.innerText = "IDs unavailable at this time, please try again later.";
	});

	request.addEventListener("load", function() {
		// console.log(request.responseText);
		let response;
		console.log(response);

		try {
			response = JSON.parse(request.responseText);
			idSearchResults.innerHTML = "";
			response.results.forEach(function(query) {
				console.log(query.candidate.id);
			let resultsHTML = `<p>${query.candidate.id} | ${query.candidate.name} | ${query.candidate.party}</p>`
			console.log(resultsHTML);
			let idSearchArticle = document.createElement("article");
			idSearchArticle.className = "item";
			idSearchArticle.innerHTML = resultsHTML;
			idSearchResults.appendChild(idSearchArticle);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("idSearchResults").innerHTML = message + err.message;
		}

	});

	let url = `https://api.propublica.org/campaign-finance/v1/2016/candidates/search.json?query=${encodeURIComponent(idSearchField.value)}`;
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

idSearchBtn.addEventListener("click", function() {
	candidateId();
});


let finSearchField = document.getElementById("finSearchField");
let finSearchBtn = document.getElementById("finSearchBtn");
let finSearchResults = document.getElementById("finSearchResults");

function candidateFinance() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		finSearchResults.innerText = "Getting financial info...";
	});

	request.addEventListener("error", function() {
		finSearchResults.innerText = "Financial info unavailable at this time.";
	});

	request.addEventListener("load", function() {
		console.log(request);
		let response;

		try {
			response = JSON.parse(request.responseText);

			finSearchResults.innerHTML = "";
			response.results.forEach(function(fecId) {
			console.log(fecId.id);
			let commID = fecId.committee?fecId.committee.slice(12,-5):"Campaign committee not found. Please try a different Candidate ID #";
			console.log(commID);
			let resultsHTML = `
				<p>FEC-ID#: ${fecId.id}</p>
				<p>Campaign Committee ID #: ${commID}</p>
				<p>Candidate Name: ${fecId.name}</p>
				<p>Party Affiliation: ${fecId.party}</p>
				<p>Follow This Link For More Candidate Info: <a href="${fecId.fec_uri}">FEC Link</a></p>
				<p>Total Receipts: $${fecId.total_receipts}</p>
				<p>Total Contributions From Individuals: $${fecId.total_from_individuals}</p>
				<p>Total Contributions From PACs: $${fecId.total_from_pacs}</p>
				<p>Total Contributions: $${fecId.total_contributions}</p>
				<p>Total Loans: $${fecId.candidate_loans}</p>
				<p>Total Disbursements: $${fecId.total_disbursements}</p>
				<p>Beginning Cash on Hand: $${fecId.begin_cash}</p>
				<p>Ending Cash On Hand: $${fecId.end_cash}</p>
				<p>Total Refunds: $${fecId.total_refunds}</p>
				<p>Debts Owed: $${fecId.debts_owed}</p>
				<p>Independent Expenditures: $${fecId.independent_expenditures}</p>
				<p>Coordinated Expenditures: $${fecId.coordinated_expenditures}</p>
				<p>This Information Was First Gathered: ${fecId.date_coverage_from}</p>
				<p>This Information Was Finalized: ${fecId.date_coverage_to}</p>
				`
			console.log(resultsHTML);
			let idFinArticle = document.createElement("article");
			idFinArticle.className = "item";
			idFinArticle.innerHTML = resultsHTML;
			// resultsHTML = resultsHTML.innerHTML;
			finSearchResults.appendChild(idFinArticle);
			// finSearchResults.appendChild(resultsHTML);
		});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("finSearchResults").innerHTML = message + err.message;
		}
		
	});

	let url = `https://api.propublica.org/campaign-finance/v1/2016/candidates/${encodeURIComponent(finSearchField.value)}.json`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

finSearchBtn.addEventListener("click", function() {
	candidateFinance();
});

let campidSearchField = document.getElementById("campidSearchField");
let campidSearchBtn = document.getElementById("campidSearchBtn");
let campidSearchResults = document.getElementById("campidSearchResults");

function campCommId() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		campidSearchResults.innerText = "Getting info...";
	});

	request.addEventListener("error", function() {
		campidSearchResults.innerText = "Info unavailable at this time."
	});

	request.addEventListener("load", function() {
		console.log(request);
		let response;

		try {
			response = JSON.parse(request.responseText);

			campidSearchResults.innerHTML = "";
			response.results.forEach(function(ccommId) {
			let resultsHTML = `
				<p>Campaign Committee ID #: ${ccommId.id}</p>
				<p>Campaign Committee Name: ${ccommId.name}</p>
				<p>Follow This Link For More Campaign Committee Info: <a href="${ccommId.fec_uri}">FEC Link</a></p>
				<p>Party Affiliation: ${ccommId.party}</p>
				<p>Treasurer: ${ccommId.treasurer}</p>
				<p>Total Receipts: $${ccommId.total_receipts}</p>
				<p>Total Contributions From Individuals: $${ccommId.total_from_individuals}</p>
				<p>Total Contributions From PACs: $${ccommId.total_from_pacs}</p>
				<p>Total Contributions: $${ccommId.total_contributions}</p>
				<p>Total Disbursements: $${ccommId.total_disbursements}</p>
				<p>Beginning Cash: $${ccommId.begin_cash}</p>
				<p>Ending Cash: $${ccommId.end_cash}</p>
				<p>Total Refunds: $${ccommId.total_refunds}</p>
				<p>Debts Owed: $${ccommId.debts_owed}</p>
				<p>Total Independent Expenditures: $${ccommId.total_independent_expenditures}</p>
				<p>Total Candidate Contributions: $${ccommId.total_candidate_contributions}</p>
				<p>This Information Was First Gathered: ${ccommId.date_coverage_from}</p>
				<p>This Information Was Finalized: ${ccommId.date_coverage_to}</p>
				`
			let campidArticle = document.createElement("article");
			campidArticle.className = "item";
			campidArticle.innerHTML = resultsHTML;
			campidSearchResults.appendChild(campidArticle);
		});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("campidSearchResults").innerHTML = message + err.message;
		}
	});

	let url = `https://api.propublica.org/campaign-finance/v1/2016/committees/${encodeURIComponent(campidSearchField.value)}.json`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

campidSearchBtn.addEventListener("click", function() {
	campCommId();
});

let campnameSearchField = document.getElementById("campnameSearchField");
let campnameSearchBtn = document.getElementById("campnameSearchBtn");
let campnameSearchResults = document.getElementById("campnameSearchResults");

function campName() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		campnameSearchResults.innerText = "Getting info...";
	});

	request.addEventListener("error", function() {
		campnameSearchResults.innerText = "Info unavailable at this time.";
	});

	request.addEventListener("load", function() {
		let response;

		try {
			response = JSON.parse(request.responseText);
			campnameSearchResults.innerHTML = "";
			response.results.forEach(function(cnameId) {
			let resultsHTML = `
				<p>Campaign Committee ID #: ${cnameId.id}</p>
				<p>Campaign Committee Name: ${cnameId.name}</p>
				<p>Party Affiliation: ${cnameId.party}</p>
				<p>Treasurer: ${cnameId.treasurer}</p>
				<p>Committee Address: ${cnameId.address}, ${cnameId.city}, ${cnameId.state}, ${cnameId.zip}</p>
				<p>Follow This Link For More Campaign Committee Info: <a href="${cnameId.fec_uri}"> FEC Link</a></p>
				`
			let nameIdArticle = document.createElement("article");
			nameIdArticle.className = "item";
			nameIdArticle.innerHTML = resultsHTML;
			campnameSearchResults.appendChild(nameIdArticle);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("campnameSearchResults").innerHTML = message + err.message;
		}
	});
	let url = `https://api.propublica.org/campaign-finance/v1/2016/committees/search.json?query=${encodeURIComponent(campnameSearchField.value)}`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

campnameSearchBtn.addEventListener("click", function() { 
	campName();
});

let lobidSearchField = document.getElementById("lobidSearchField");
let lobidSearchBtn = document.getElementById("lobidSearchBtn");
let lobidSearchResults = document.getElementById("lobidSearchResults");

function lobId() {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function() {
		lobidSearchResults.innerText = "Getting info...";
	});

	request.addEventListener("error", function() {
		lobidSearchResults.innerText = "Info unavailable at this time.";
	});

	request.addEventListener("load", function() {
		let response;

		try {
			response = JSON.parse(request.responseText);
			lobidSearchResults.innerHTML = "";
			response.results.forEach(function(lobbyID) {
			let resultsHTML = `
			<p>Campaign Committee ID #: ${lobbyID.fec_committee_id}</p>
			<p>Filing ID #: ${lobbyID.fec_filing_id}</p>
			<p>Transaction ID #: ${lobbyID.transaction_id}</p>
			<p>Entity Type: ${lobbyID.entity_type}</p>
			<p>Lobbyist Organization Name: ${lobbyID.bundler_organization_name}</p>
			<p>Lobbyist Name: ${lobbyID.bundler_first_name}, ${lobbyID.bundler_middle_name}, ${lobbyID.bundler_last_name}</p>
			<p>Lobbyist Address: ${lobbyID.bundler_street_1}, ${lobbyID.bundler_city}, ${lobbyID.bundler_state}, ${lobbyID.bundler_zip}</p>
			<p>Lobbyist Employer: ${lobbyID.bundler_employer}</p>
			<p>Lobbyist Occupation: ${lobbyID.bundler_occupation}</p>
			<p>Amount Contributed: $${lobbyID.bundled_amount}</p>
			<p>This Information Was First Gathered: ${lobbyID.start_date}</p>
			<p>This Information Was Finalized: ${lobbyID.end_date}</p>
			`

			let lobIdArticle = document.createElement("article");
			lobIdArticle.className = "item";
			lobIdArticle.innerHTML = resultsHTML;
			lobidSearchResults.appendChild(lobIdArticle);
			});
		}
		catch(err) {
			let message = "Error, please try again later.";
			document.getElementById("lobidSearchResults").innerHTML = message + err.message;
		}
	
	});
	let url = `https://api.propublica.org/campaign-finance/v1/2016/committees/${encodeURIComponent(lobidSearchField.value)}/lobbyist_bundlers.json`
	request.open("GET", url);
	request.setRequestHeader("X-API-Key", "jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5");
	request.send();
}

lobidSearchBtn.addEventListener("click", function() {
	lobId();
});