disney = '''Disney's two most famous mice ___1___ , and his faithful companion ___2___ mouse have been staples of the
Disney family for 90 years. The creator of this empire ___3___ disney is known as one of the fathers of animation and
is responsible for some of the earliest animated films ever made. The first fully animated feature film Snow White and 
the Seven ___4___was released by disney in 1938.'''

fantasy = '''When Harry goes to diagon alley Hagrid buys him a ___1___ named Hedwig. Harry's patronus charm takes 
the form of a ___2___ in the Prisoner of Azkaban.___3___ are refered to as people who do not posses any magical powers. 
The last horcrux that needs to be destroyed to defeat Lord Voldemort is ___4___.'''

for the tidal shifts on the Earths surface, and without it a day would only last about 6-to-8 hours. In 4 billion years
our galaxy the Milky Way, will collide with our neighboring galaxy, ___3___.Scientist predict that the footprint left by
the astronauts on the ___4___ mission will be there for 100 million years '''

blanks = ['___1___', '___2___', '___3___', '___4___']
answer_key_1 = ["Mickey", "Minnie", "Walt", "Dwarfs"]
answer_key_2 = ["owl", "stag", "muggles", "Harry"]
answer_key_3 = ["Earth", "Moon", "Andromeda", "Apollo"]


# def user_input(counter):
# creates an index for the blanks which we assign to the user_input so that we can use this input in our main function
# def word_in_blanks to return the user_input and fill in the blanks in the selected paragraph.


def user_input(counter):
    user_input = input("\nType your answer for {}:(make sure to capitalize!)\n".format(counter))
    return user_input

# def attempt_selector():
# creates an int for the user input and assigns that input to attempts we return attempts and pick it up in the
# def word_in_blanks function so we can keep track of the number of attempts


def attempt_selector():
    attempts = int(input('\nEnter the amount of attempts you want to give yourself: \n'))
    return attempts

# def paragraph_selector():
# Allows you to choose the difficulty level, if the you choose a valid level it will print a short blurb and return
# the associated paragraph and its answer_key, if the level you select is not valid it will loop back through the prompt
# with the while loop and ask you to type a valid level. We pick up the returned values in the function to iterated
# through.

def paragraph_selector():
    level = ''
    levels = ['easy', 'medium', 'hard']
    print('Levels: easy | medium | hard')
    while level not in levels:
        level = input("\nType difficulty level: \n")
        if level == 'easy':
            print("\nYou must be an imagineer.\n")
            return disney, answer_key_1

        if level == 'medium':
            print("\nOh so you fancy yourself a wizard ehh?\n")
            return fantasy, answer_key_2

        if level == 'hard':
            print("\nPrepare for blastoff!\n")
            return space, answer_key_3


# def word_in_blanks()
# start the counter at 0 so we can iterate through the blanks in a loop, assign the selected_level and answer to the
# paragraph_selector function so we can grab the returned values we got from that function to be used in this function.
# Now keeping in mind the counter should only go to 4 given our 4 blanks we say while the counter is less than the
# length of the blanks array preform this function noting that we add 1 to the counter each correct answer.
# We want the user to see the paragraph, so as long as the counter has not hit 4 correct answers print the
# selected_level which will be the level the user selected when they went through the paragraph_selector function. Also
# in this function we add the  amount of attempts the user selects in the def attempts_selector() function. Similar
# principle to the counter variable however we assign attempts the the user input from the attempts_selector function
# then we set it to itself - 1 whenever a incorrect answer is sent until attempts == 0 which we then return a string and
# break the program so it needs to be reset.
# --------------------------------------------------------------------------------------------------------------------
# As for the Blanks we need to access the returned value for the def guess(counter) so we can use that value to validate
# against the answer and fill in the blank if that answer is correct. To do this I created a variable called user_answer
# and assigned that to the user input from the def guess(counter)function since this is now the user_answer for the
# blank. If that user answer is equal to the answer in the counter list print "Nice, that's correct! in addition assign
# the selected level to itself so we can match the correct blank and user answer and replace that answer in the
# paragraph after that is added we add 1 to the counter so that we move to the next blank so we can repeat this
# while loop. Once the counter > len(blanks) it will print the selected level with the user_answers. If the user_answer
# does not not equal the the correct answer associated with the counter print 'Incorrect answers, try again.'
# which will always loop if the answer is incorrect until attempts == 0.


def word_in_blanks():
    counter = 0
    selected_level, answer = paragraph_selector()
    attempt = attempt_selector()
    while counter < len(blanks):
        print(selected_level)
        user_answer = user_input(blanks[counter])
        if user_answer == answer[counter]:
            print("\nNice, that's correct!\n")
            selected_level = selected_level.replace(blanks[counter], user_answer)
            counter += 1

        else:
            print('\nIncorrect answers, try again.\n')
            attempt = attempt - 1
            if attempt == 0:
                print('\nYou have maxed out our attempts, please try again.\n')
                break

    print(selected_level)


word_in_blanks()
























































