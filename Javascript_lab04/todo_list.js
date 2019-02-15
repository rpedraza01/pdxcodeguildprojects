let body = document.getElementsByTagName("body");
let ul = document.getElementById("ulTodo");

let inputField = document.getElementById("inputField");
let addTodobutton = document.querySelector("#addTodobutton");

addTodobutton.addEventListener("click", function() {
	let text = inputField.value;
	console.log(text);
	let li = document.createElement("li");
	li.setAttribute("className", "todoItem");
	let p = document.createElement("p");
	p.innerText = text;
	console.log(p);

	let completedBtn = document.createElement("button");
	let ulNew = document.getElementById("ulCompleted");
	completedBtn.innerText = "Completed";
	completedBtn.addEventListener("click", function() {
		ulNew.appendChild(li);
		completedBtn.remove();
		let deleteBtn = document.createElement("button");
		deleteBtn.innerText = "Delete";
		deleteBtn.addEventListener("click", function() {
		completedBtn.parentNode.remove();
		});

	});
		
		let deleteBtn = document.createElement("button");
		deleteBtn.innerText = "Delete";
		deleteBtn.addEventListener("click", function() {
			deleteBtn.parentNode.remove();

	});

	ul.appendChild(li);
	li.appendChild(p);
	li.appendChild(completedBtn);
	li.appendChild(deleteBtn);
	});
