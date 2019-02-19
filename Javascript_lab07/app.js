let counter = 0;

function hackText() {
let textArray = "Haxx0r ipsum ban ddos ack chown wombat suitably small values d00dz. Dennis Ritchie true pwned xss bubble sort malloc emacs long bin cat recursively access syn it's a feature gurfle bang nak *.* thread server. Buffer socket break packet gnu void then finally concurrently. Fatal /dev/null ifdef firewall irc giga new gobble exception stack trace Linus Torvalds var Starcraft I'm sorry Dave, I'm afraid I can't do that. L0phtCrack leapfrog memory leak stdio.h shell public client big-endian vi gcc highjack pragma snarf daemon mainframe semaphore. Tera mountain dew script kiddies data worm tera system. Gc injection eof endif gc for alloc rm -rf Leslie Lamport interpreter. Brute force while echo private packet sniffer class headers fatal wabbit. Protected hexadecimal unix python mutex blob loop fork flush infinite loop cache do. Strlen machine code double foad dereference warez perl tcp eaten by a grue throw afk int fail fopen try catch else protected cookie Trojan horse. Stdio.h fail private public worm back door infinite loop spoof int float headers brute force mega flood packet cookie port exception. Cd new hack the mainframe unix gcc James T. Kirk null cd void highjack. Perl hexadecimal bubble sort chown double mainframe printf. Case big-endian fork false rm -rf it's a feature bytes class less ssh tcp fopen cat alloc protected break injection script kiddies. Tunnel in tarball Trojan horse crack ifdef terminal concurrently L0phtCrack kilo d00dz giga stack *.* lib flush interpreter frack. Function gobble gurfle then system stack trace server afk leet /dev/null throw protocol snarf suitably small values do linux boolean gc hello world. Salt mutex fatal recursively race condition client mountain dew for malloc I'm compiling wannabee memory leak function. Grep dereference socket Starcraft wabbit machine code baz mailbomb default shell root buffer Linus Torvalds tera leapfrog. Ip wombat while semaphore I'm sorry Dave, I'm afraid I can't do that endif win else access bin syn finally echo over clock rsa emacs irc Donald Knuth. Loop data char pwned loop continue ascii warez stdio.h pragma sudo ctl-c segfault January 1, 1970.";
let typeWord = textArray.split(" ");
console.log(typeWord);
let type = document.getElementById("text");
type.addEventListener("keydown", function(event) {
	type.innerText = type.value + " " + typeWord[counter];
	counter += 1;
	event.preventDefault();
}, false);
	
}
hackText();