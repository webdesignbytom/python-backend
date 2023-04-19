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
user_vote = max_score/5000000

## dictionary 
original_categories = {'General Knowledge': {"score: ": (max_score/100) * 25, "subcategories": { "sports": 1, "biology": 1, "maths": 1, "art": 1}}, 'Spacial Reasoning': {"score: ": (max_score/100) * 15, "subcategories": {"visual": 1, "reflexs": 1, "audio": 1}}, 'IQ': {"score: ": (max_score/100) * 60, "subcategories": {"words": 1, "puzzle": 1}} }
                       
new_categories = dict(original_categories)

## Upvote a category
def vote_up(category):
    print("Your up vote is being cast for " + category)

    upvote_score = user_vote
    downvote_score = user_vote / (len(new_categories) - 1)

    print('up score: ', upvote_score)
    print('down score: ', downvote_score)
    print("length: ", len(new_categories) - 1)
    print("")
    print("Selected category score:", new_categories[category]['score: '])

    ## loop through categories
    for x in new_categories:
        if x != str(category):
            print("Its not", x)
            print("AA", new_categories[x])
            current_score = new_categories[x]["score: "]
            print("BB", current_score)
            new_score = current_score - downvote_score
            print("CC", new_score)
            new_categories[x]["score: "] = new_score
        else:
            print("It's", x)
            current_score = new_categories[x]["score: "]
            new_score = current_score + upvote_score
            print("CC", new_score)
            new_categories[x]["score: "] = new_score
    print("End")
    print("")

## Down vote a category
def vote_down(category):
    print("Your down vote is being cast for " + category)

    downvote_score = user_vote
    upvote_score = user_vote / (len(new_categories) - 1)

    print('up score: ', upvote_score)
    print('down score: ', downvote_score)
    print("length: ", len(new_categories) - 1)
    print("")
    print("Selected category score:", new_categories[category]['score: '])

    ## loop through categories
    for x in new_categories:
        if x != str(category):
            print("Its not", x)
            print("AA", new_categories[x])
            current_score = new_categories[x]["score: "]
            print("BB", current_score)
            new_score = current_score - downvote_score
            print("CC", new_score)
            new_categories[x]["score: "] = new_score
        else:
            print("It's", x)
            current_score = new_categories[x]["score: "]
            new_score = current_score + upvote_score
            print("CC", new_score)
            new_categories[x]["score: "] = new_score

    print("")

## vote up or down query
def vote_query(category):
    query = str(input("Do you want to vote " + category + " up or down? "))
    print("You voted", query)

    # If voted up. increase score of category and decrease score of all other categories
    if query.lower() == "up":
        vote_up(category)

    elif query.lower() == "down":
        vote_down(category)


## Main run loop for program
while True:
    print('----------------START-------------------')
    print('')
    print('Max Score:', max_score, '| User Vote Value:', user_vote)
    print('Original Categories:', original_categories)
    print('Mutated Categories:', new_categories)
    print('')

    ## user selects what to vote for
    category_choice = str(input("What Category do you want to vote for? "))
    if category_choice.lower() == 'q':
        print("Quitting")
        break

    if category_choice.lower() == 'gk' or category_choice.lower() == 'general knowledge':
        print("You have selected General Knowledge")
        print('')
        category_choice = str("General Knowledge")
        vote_query(category_choice)

    elif category_choice.lower() == 'spacial reasoning' or category_choice.lower() == 'sr':
        print("You have selected Spacial Reasoning")
        print('')
        category_choice = str("Spacial Reasoning")
        vote_query(category_choice)

    elif category_choice.lower() == 'iq':
        print("You have selected IQ")
        print('')
        category_choice = str("IQ")
        vote_query(category_choice)

    print("New Scores: ", new_categories)
    print('----------------END-------------------')


        