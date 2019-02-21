let quoteBox = document.getElementById("quoteBox");
let getQuoteButton = document.getElementById("quoteButton");
let quoteField = document.getElementById("quoteField");
let pageCounter = 1;
let nextPageTop = document.getElementById("nextTop");
let previousPageTop = document.getElementById("previousTop");

let nextPageBottom = document.getElementById("nextBottom");
let previousPageBottom = document.getElementById("previousBottom");

nextPageTop.addEventListener("click", function() {
pageCounter += 1;
Quote();
});

previousPageTop.addEventListener("click", function() {
pageCounter -= 1;
console.log(pageCounter);
Quote();
});

nextPageBottom.addEventListener("click", function() {
pageCounter += 1;
Quote();
});

previousPageBottom.addEventListener("click", function() {
pageCounter -= 1;
console.log(pageCounter);
Quote();
});

getQuoteButton.addEventListener("click", function() {
Quote();
});

function Quote(e) {
	let request = new XMLHttpRequest();

	request.addEventListener("progress", function(e) {
		console.log(e.loaded);
		quoteBox.innerText = "Getting your quotes...";
	});

	request.addEventListener("error", function(e) {
		console.log(e.status);
		quoteBox.innerText = "Quotes unavailable, try again later."
	});

	request.addEventListener("load", function(e) {
		console.log(request.responseText);
		let response = JSON.parse(request.responseText);
		console.log(response);

		quoteBox.innerHTML = "";
		response.quotes.forEach(function(quote) {
		let resultHTML = `
			<h3>${quote.body}</h3>
			<h3><i><a href="${quote.url}">${quote.author}</a></i></h3>
			`;
		let quoteDiv = document.createElement("div");
		quoteDiv.className = "item";
		quoteDiv.innerHTML = resultHTML;
		quoteBox.appendChild(quoteDiv);
		// console.log(resultHTML);
		});
	});

	// request.open("GET", "https://favqs.com/api/qotd");
	let url = `https://favqs.com/api/quotes?filter=${encodeURIComponent(quoteField.value)}&page=${pageCounter}`;

	request.open("GET", url);
	request.setRequestHeader("Authorization", 'Token token="4b3888849b4ef0bec9f217ffd39869a9"');
	request.send();
}

// quoteField.addEventListener("keydown", function(e) {
// 	if (e.keyCode === 13) {
// 		Quote(e);
// 	};
// });

// nextPage.addEventListener("keydown", function() {
// 	if (keyCode === 107) {
// 		Quote();
// 	};
// });

// previousPage.addEventListener("keydown", function() {
// 	if (keyCode === 109) {
// 		Quote();
// 	};
// });

// getQuoteButton.addEventListener("click", Quote);