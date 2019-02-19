function hackText() {
let textArray = "Haxx0r ipsum ban ddos ack chown wombat suitably small values d00dz. Dennis Ritchie true pwned xss bubble sort malloc emacs long bin cat recursively access syn it's a feature gurfle bang nak *.* thread server. Buffer socket break packet gnu void then finally concurrently. Fatal /dev/null ifdef firewall irc giga new gobble exception stack trace Linus Torvalds var Starcraft I'm sorry Dave, I'm afraid I can't do that. L0phtCrack leapfrog memory leak stdio.h shell public client big-endian vi gcc highjack pragma snarf daemon mainframe semaphore. Tera mountain dew script kiddies data worm tera system. Gc injection eof endif gc for alloc rm -rf Leslie Lamport interpreter. Brute force while echo private packet sniffer class headers fatal wabbit. Protected hexadecimal unix python mutex blob loop fork flush infinite loop cache do. Strlen machine code double foad dereference warez perl tcp eaten by a grue throw afk int fail fopen try catch else protected cookie Trojan horse.";
let typeWord = textArray.split(" , ");
console.log(typeWord);
let type = document.getElementById("text");
type.addEventListener("keydown", function(event) {
	type.innerText = typeWord;
	event.preventDefault();
}, false);
	
}



hackText();