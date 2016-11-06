""" Used to update the displayed paragraph with the user's answers """
def word_in_current_paragraph(user_answer, answer_number, current_paragraph): 
    updated_paragraph = []
    current_paragraph = current_paragraph.split()
    for word in current_paragraph:
        if word == "___" + (str(answer_number)) + "___":
            word = user_answer
            updated_paragraph.append(word)
        else:
            updated_paragraph.append(word)
    updated_paragraph = " ".join(updated_paragraph)
    return updated_paragraph

""" answer key for easy, medium, and hard levels """
answers = ['function', 'argument', 'none', 'byte', 'obvious', 'start', 'correct', 'short', 'sequence', 'append', 'mutate', 'elements'] 

#The following are the paragraphs displayed to the user depending on their selection of the level of difficulty
paragraph_easy = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by \
 adding an ___2___ separated by commas between the parentheses. A ___1___ by default will return ___3___ if you\
  don't specify the value to return. An ___2___ can be standard data types such as string, number, dictionary,\
   tuple, and ___4___ or can be more complicated such as objects and lambda functions."""

paragraph_medium = """Comments are lines of code that are ignored by the computer. You should not\
 comment ___1___ code. All functions should ___2___ with a comment. Comments should be kept up-to-date\
  with ___3___ information. Comments should be ___4___ and explain only the most important details of your code."""

paragraph_hard = """Python has a number of list operations. Lists respond to all of the general ___1___ operations\
 that are used on strings. An ___2___ can be used to add a new element to the end of a list. Plus produces a\
  new list but does not ___3___ either of the two input lists. The output of len is the number of ___4___ in\
   the input."""

print

""" This function prompts the user to select the level difficulty which is returned as user_input """
user_input = ""
def select_level():
    user_selection = False
    while user_selection == False:
        user_input = raw_input("Please select a game difficulty by typing it in! Your choices are easy, medium, or hard." + "  ").lower()
        #user_input = user_input.lower()
        if user_input == "easy" or user_input == "medium" or user_input == "hard":
            user_selection = True
            print "\n" + "You have chosen " + "\033[1m" + user_input.lower() + "\033[0m" + "."
            print "\n" + "You will get 5 guesses per problem." + "\n"
        else:
            print "Please enter a valid selection."
    return user_input

""" Sets the paragraph to the level of difficulty based on the user's difficulty level selection """
def allocate_quiz_current_paragraph():
    difficulty = user_input
    if difficulty == "easy":
        current_paragraph = paragraph_easy
        print current_paragraph + "\n"
    elif difficulty == "medium":
        current_paragraph = paragraph_medium
        print current_paragraph + "\n"
    else:
        current_paragraph = paragraph_hard
        print current_paragraph + "\n"
    return current_paragraph

""" Determines which set of answers will be used based on the user's difficulty level selection """
def allocate_quiz_answer_index():
    difficulty = select_level()
    if difficulty == "easy":
        easy_start_index = 0
        answer_index = easy_start_index
    elif difficulty == "medium":
        medium_start_index = 4
        answer_index = medium_start_index
    else:
        hard_start_index = 8
        answer_index = hard_start_index
    return answer_index

""" Initializes set up for the assigned variables for starting the quiz """
	

def run_quiz(answer_number, total_number_of_answers, number_of_guesses, no_guesses_remaining):
	answer_index = allocate_quiz_answer_index()
	current_paragraph = allocate_quiz_current_paragraph()
	while (answer_number - 1) < total_number_of_answers and number_of_guesses >= no_guesses_remaining:
		user_answer = raw_input("What should be subsituted in for ___" + (str(answer_number)) + "___?" + "  ").lower()
		if user_answer == answers[answer_index]:
			answer_index += 1
			print "\n" + "Correct!" + "\n"
			current_paragraph = word_in_current_paragraph(user_answer, answer_number, current_paragraph)
			print current_paragraph + "\n"
			answer_number += 1
			number_of_guesses = 4
		else:
			print "\n" + "That isn't the correct answer!  Let's try again; you have " +  (str(number_of_guesses)) + " trys left!" + "\n"
			number_of_guesses -= 1
	user_wins_loses_prompt(number_of_guesses)
	

""" Gives appropriate response for if the user wins or loses """
def user_wins_loses_prompt(number_of_guesses):
	if number_of_guesses < 0:
		print "You have failed. Too many wrong guesses. Game over!" + "\n"
	else:
		print "You Win!" + "\n"

""" Prompts the user to fill in the blanks with the appropriate answers and keeps track of the number of guesses.
If the user enters the correct answer for each selection they win. If the user makes 5 incorrect guesses for a
given blank the game is over. """
def play_game():
	answer_number = 1
	total_number_of_answers = 4
	number_of_guesses = 4
	no_guesses_remaining = 0
	run_quiz(answer_number, total_number_of_answers, number_of_guesses, no_guesses_remaining)
    
play_game()








