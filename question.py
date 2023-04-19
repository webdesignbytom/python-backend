# I am making a quiz app. It has its backend controlled by python. 
# I want users to answer questions as usual in various categories.
# Also I want users to be able to vote on the value of each category. 
# Then futher be able to vote on the value of the subcategories.
# There is an overall total and people score a percentage of that throughout all the question categories.

# Max score for all categories and questions is 6000
max_score = 6000
# Each category has a percentage of that 6000 
# Users can vote on the categories value, up or down.
# Each user has a power to change the percentage of a category by 0.00001% of 6000
user_vote = max_score/1000000

## so gen knowledge is worth 25% of 6000 points
## dictionary 
original_categories = {'General knowledge': (max_score/100) * 25, 'Spacial Reasoning': (max_score/100) * 15, 'IQ': (max_score/100) * 60}

## Sub categories of general knowledge
gen_knowledge_sub_cats = {'history': '10%', 'sports': '10%', 'math': '55%', 'science': '25%'}

# if you up vote the category up. your percentage is added to the selected category
def vote_up(category):
    print("Your up vote is being cast for " + category)

    upvote_score = user_vote
    downvote_score = user_vote / (len(original_categories) - 1)

    print('up score: ', upvote_score)
    print('down score: ', downvote_score)
    print("length: ", len(original_categories) - 1)
    # category_percentage += user_vote
    # other_category1 -= user_vote / len(original_categories) -1 ## -1 because one cat gets added to
    # other_category2 -= user_vote / len(original_categories) -1 

def vote_down(category):
    print("Your down vote is being cast for " + category)

    # category_percentage -= user_vote
    # other_category1 += user_vote / len(original_categories) -1 ## -1 because one cat gets added to
    # other_category2 += user_vote / len(original_categories) -1 

# So the value of the category changes but you still only score 10/10 per category

## vote up or down
def vote_query(category):
    query = str(input("Do you want to vote " + category + " up or down? "))
    print("You voted", query)

    # If voted up. increase score of category and decrease score of all other categories
    if query.lower() == "up":
        vote_up(category)

    elif query.lower() == "down":
        vote_down(category)

## Am i not going to get some serious rounding errors after a while if alot of people vote. And the other_categories are at a certain number that leaves a remainder?
## Im concerned it could turn out to be quite buggy.
while True:
    print('--------------------------------')
    print('')
    print('Max Score:', max_score, '| User Vote Value:', user_vote)
    print('Original Categories:', original_categories)
    print('')

    ## user selects what to vote for
    category_choice = str(input("What Category do you want to vote for? "))
    if category_choice.lower() == 'q':
        print("Quitting")
        break


    if category_choice.lower() == 'gk' or category_choice.lower() == 'general knowledge':
        print("You have selected General knowledge")
        print('')
        vote_query(category_choice)

        pass

    elif category_choice.lower() == 'spacial reasoning' or category_choice.lower() == 'sr':
        print("You have selected Spacial Reasoning")
        print('')
        vote_query(category_choice)

        pass

    elif category_choice.lower() == 'iq':
        print("You have selected IQ")
        print('')
        vote_query(category_choice)

        continue

print("----------------------------------")