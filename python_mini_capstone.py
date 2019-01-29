#python_mini_capstone.py
import sys
import requests

def get_all_questions(data):
	trivia_questions = []
	for item in range(len(data["results"])):
		trivia_question = data["results"][item]["question"]
		trivia_questions.append(trivia_question)
	return trivia_questions

def get_all_answers(data):
	trivia_correct_list = []
	for item in range(len(data["results"])):
		trivia_correct_list.append(data["results"][item]["correct_answer"])
	return trivia_correct_list

def question_correct_answer(data):
	questions = get_all_questions(data)
	answers = get_all_answers(data)
	question_answer_tuple_list = list(zip(questions, answers))
	return question_answer_tuple_list

def main():
	while True:
		response = requests.get("https://opentdb.com/api.php?amount=10")
		print("Status code:", response.status_code)
		data = response.json()
		# print(question_correct_answer(data))
		print("Let's play a game of trivia!")
		print("~"*25)
		q_and_a = question_correct_answer(data)
		while len(q_and_a) > 0:
			q = q_and_a.pop(0)
			print(q[0])
			guess = input("What is your guess? > ").strip().lower()
			correct_answer = q[1]
			if guess == correct_answer.strip().lower():
				print("That's correct!")
				print("~"*25)
			else:
				print("Sorry, that's incorrect.")
				print(f"The correct answer is {correct_answer}")
				print("~"*25)
		exit = input("Would you like 10 more trivia questions? > ").strip().lower()
		if exit.startswith("n"):
			print("~"*25)
			break

main()
# for item in get_all_questions():
# 	pass

# 	trivia_incorrect_list.append(data["results"][item]["incorrect_answers"])
# print(trivia_correct_list)
# print(trivia_incorrect_list)
# trivia_incorrect_list = []

# print(type(data))
# print(data)
# print(get_all_questions())

# print(response.headers)

# print(response.headers["content-type"])










# import markovify

# with open("/path/to/my/corpus.txt") as f:
# 	text = f.read()

# text_model = markovify.Text(text)

# for i in range(5):
# 	print(text_model.make_sentence())

# for i in range(3):
# 	print(text_model.make_short_sentence(140))