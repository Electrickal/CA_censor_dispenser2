# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


###				Variables 				###
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


### 			Functions 				###

# Takes two variables, list of terms to sensor and a text file that you want to edit
def censor_email(email, prop_terms):
	for term in prop_terms:
		email = email.replace(term + ' ', '#' * len(term) + ' ')
		email = email.replace(term.title() + ' ', '#' * len(term) + ' ')
		email = email.replace(term.upper() + ' ', '#' * len(term) + ' ')

	return email


print(censor_email(email_two, proprietary_terms))
print("#" * len(proprietary_terms[0]))



