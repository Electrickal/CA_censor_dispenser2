# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


###				Variables 				###
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]


### 			Functions 				###

# Takes two variables, list of terms to sensor and a text file that you want to edit
def censor_email(email, prop_terms):
	for term in prop_terms:
		email = email.replace(term + ' ', '#' * len(term) + ' ')
		email = email.replace(term.title() + ' ', '#' * len(term) + ' ')
		email = email.replace(term.upper() + ' ', '#' * len(term) + ' ')

	return email

# Removes subsequent mentions of "negative words" from a text strig after one mention of a word.
def negative_remove(email, neg_terms):
	for term in neg_terms:

		# Use word_index to find the 3rd mention of term in a string. start index at -1
		word_index = -1
		for i in range(2):
			word_index = email.lower().find(term[word_index + 1 :])

		if word_index > 0:
			email = email.replace(term + ' ', '#' * len(term) + ' ')
			email = email.replace(term.title() + ' ', '#' * len(term) + ' ')
			email = email.replace(term.upper() + ' ', '#' * len(term) + ' ')

	return email
def censor_neg_remove_email(email, neg_terms, prop_terms):
	email = negative_remove(email, neg_terms)
	email = censor_email(email, prop_terms)

	return email


print(email_three)
print(censor_neg_remove_email(email_three, negative_words, proprietary_terms))





