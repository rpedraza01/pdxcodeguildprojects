
alert("Welcome to the Blackjack Advisor. Let's get you some wins!");
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

let card_hand = [];
var first_card = prompt("What is your first card?");
card_hand.push(card_dict[first_card]);
var second_card = prompt("What is your second card?");
card_hand.push(card_dict[second_card]);

var total = card_hand[0] + card_hand[1]

// let card_input1 =
// document.querySelector("#card_input1");
// let card_input2 =
// document.querySelector("#card_input2");
// let run_button = document.querySelector("#run_button");
// let total =
// document.querySelector("#total");
// run_button.onclick = function() {
// 	let card1 = card_input1.value;
// 	let card2 = card_input2.value;
// 	total.innerText = `You have ${card1 + card2}!`;
// }

let cardAdvice;
while (true) {
	if (total < 17) {
		cardAdvice = alert("I suggest you hit.");
		var next_card = prompt("What is your next card?");
		total += card_dict[next_card];
	}
	else if (total >= 17 && total < 21) {
		cardAdvice = alert("I advise you stay.");
		break;
	}
	else if (total === 21) {
		cardAdvice = alert("You've got Blackjack!");
		break;
	}
	else if (total > 21) {
		cardAdvice = alert("You've busted. Better luck next time.");
		break;
	}
}