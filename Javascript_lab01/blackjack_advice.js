var card_dict = {
		"A": 1,
	
		"2": 2,
	
		"3": 3,
	
		"4": 4,
	 
		"5": 5,
	
		"6": 6,
	
		"7": 7,
	 
		"8": 8,
	
		"9": 9,
	 
		"10": 10,
	 
		"J": 10,
	 
		"Q": 10,
	 
		"K": 10
};

let card_hand;
let newCardhand;
let advicetotalField = 0;
let adviceTotal = document.getElementById("adviceTotal");
let newAdvicetotal = document.getElementById("newAdvicetotal");
let cardAdvice;

let adviceButton = document.querySelector("#adviceButton");
adviceButton.addEventListener("click", function() {
	let adviceField1 = document.getElementById("card_input1");
	let card_input1 = adviceField1.value;
	let adviceField2 = document.getElementById("card_input2");
	let card_input2 = adviceField2.value;
	card_hand = card_dict[card_input1] + card_dict[card_input2];
	// advicetotalField = parseFloat(card_input1) + parseFloat(card_input2);
	adviceTotal.innerText = `Your hand is ${card_hand}`;
	if (card_hand < 17) {
		cardAdvice = alert("I suggest you hit.");
	}
	else if (card_hand >= 17 && card_hand < 21) {
		cardAdvice = alert("I advise you stay.");
	}
	else if (card_hand === 21) {
		cardAdvice = alert("You've got Blackjack!");
	}
	else if (card_hand > 21) {
		cardAdvice = alert("You've busted. Better luck next time.");
	}
});

let adviceAgainbutton = document.querySelector("#adviceAgainbutton");
adviceAgainbutton.addEventListener("click", function() {
	let newadviceField = document.getElementById("nextCard_input");
	let nextCard_input = newadviceField.value;
	newCardhand = card_hand + card_dict[nextCard_input];
	// let newAdvicetotalField = advicetotalField + parseFloat(nextCard_input);
	newAdvicetotal.innerText = `Your hand is now ${newCardhand}`;
	if (newCardhand < 17) {
		cardAdvice = alert("I suggest you hit.");
	}
	else if (newCardhand >= 17 && newCardhand < 21) {
		cardAdvice = alert("I advise you stay.");
	}
	else if (newCardhand === 21) {
		cardAdvice = alert("You've got Blackjack!");
	}
	else if (newCardhand > 21) {
		cardAdvice = alert("You've busted. Better luck next time.");
	}
});

// let card_input1 = document.querySelector("#card_input1");
// let card_input2 = document.querySelector("#card_input2");
// card_hand.push(card_dict[card_input1]);
// card_hand.push(card_dict[card_input2]);
// let adviceButton = document.querySelector("#adviceButton");
// let total = document.querySelector("#total");
// run_button.onclick = function() {
// 	let card1 = card_input1.value;
// 	let card2 = card_input2.value;
// 	total.innerText = `You have ${card1 + card2}!`;
// }

// let cardAdvice;
// // while (true) {
// 	if (card_hand < 17) {
// 		cardAdvice = alert("I suggest you hit.");
// 		// var next_card = prompt("What is your next card?");
// 		// total += card_dict[next_card];
// 	}
// 	else if (card_hand >= 17 && card_hand < 21) {
// 		cardAdvice = alert("I advise you stay.");
// 		// break;
// 	}
// 	else if (card_hand === 21) {
// 		cardAdvice = alert("You've got Blackjack!");
// 		// break;
// 	}
// 	else if (card_hand > 21) {
// 		cardAdvice = alert("You've busted. Better luck next time.");
// 		// break;
// 	}
// // }