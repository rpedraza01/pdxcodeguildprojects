let idSearchField = document.getElementById("idSearchField");
let idSearchBtn = document.getElementById("idSearchBtn");
let idSearchResults = document.getElementById("idSearchResults");



	let url = `https://api.propublica.org/campaign-finance/v1/{cycle}/candidates/search`
	request.open("GET", url);
	request.setRequestHeader("Authorization", 'Token token="jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5"');
	request.send();
}


let finSearchField = document.getElementById("finSearchField");
let finSearchBtn = document.getElementById("finSearchBtn");
let finSearchResults = document.getElementById("finSearchResults");



	let url = `https://api.propublica.org/campaign-finance/v1/{cycle}/candidates/{fec-id}`
	request.open("GET", url);
	request.setRequestHeader("Authorization", 'Token token="jYFljixpLeen7YwGnVVpSTSPlpex7C0ttSgdwsS5"');
	request.send();
}