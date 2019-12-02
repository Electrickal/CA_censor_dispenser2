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

def censor_neg_remove_email(email):
	email = negative_remove(email, negative_words)
	email = censor_email(email, proprietary_terms)

	return email

# Censors the immediate word before and after a word that is already censored 
def super_censor(email):
	email = censor_neg_remove_email(email)

	spl_email = email.split()

	siter = iter(range(len(spl_email)))
	for i in siter:
		if spl_email[i] == '#' * len(spl_email[i]):
			if i > 0:
				spl_email[i - 1] = '#' * len(spl_email[i - 1])
			if i < len(spl_email) - 1:
				spl_email[i + 1] = '#' * len(spl_email[i + 1])
				next(siter, None)

	return ' '.join(spl_email)


###				Main					###

#print(email_two)
email_four = super_censor(email_four)
print(email_four)




