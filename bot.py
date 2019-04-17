import praw
import config
import os
import json
      
def bot_login():
    # uses the information from the config.py file to log the bot into its reddit account
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Kings Reddit Bot v1.0")
    
    return reddit

def run_bot(reddit):
    subreddit = reddit.subreddit('kings') # Bot only streams on 'r/kings' 

    for submission in subreddit.stream.submissions(): # Reads submissions from stream of threads
        if 'fan here' in submission.title.lower() and submission.id not in submissions_replied_to:
            encoded_title = submission.title.encode('unicode-escape').decode('utf-8') # Emoji's cause the bot to crash, this encodes them to avoid errors
            split_text = encoded_title.split(' ')
            
            for i in range(len(split_text)):
                if 'fan' in split_text[i]:
                    team_name = find_team(split_text[i-1].lower(), team_compliments) # sends the word before "fan here" to check if it's a team name
                    if team_name != "Not Found":
                        submission.reply("It seems that you are a fan of the `" + team_names[team_name] + "`\n\n If I am programmed correctly, I have also detected that this is a 'fan here' thread. Thank you for complimenting our team, here is a compliment for your team:\n\n &nbsp;\n >**" + team_compliments[team_name] + "** \n\n>>!If it appears that I have a bug, please PM me so my creator can fix me! Thanks! !<")
                        submissions_replied_to.append(submission.id)
                        print("Submissions found and replied to")
                        print()

                        with open("submissions_replied_to.txt", "a") as f:
                            f.write(submission.id + "\n")

def load_saved_submissions(): # loads the "submissions_replied_to.txt" file to read if any submissions have already been replied to
	if not os.path.isfile("submissions_replied_to.txt"):
		submissions_replied_to = []
	else:
		with open("submissions_replied_to.txt", "r") as f:
			submissions_replied_to = f.read()
			submissions_replied_to = submissions_replied_to.split("\n")

	return submissions_replied_to
    
def load_json_dict(file: str):
    with open(file) as f:
        json_dict = json.load(f)
    return json_dict
    
def find_team(team: str, team_compliments: dict):
    for team_name, compliment in team_compliments.items():
        if team_name in team:
            return team_name
        
    return "Not Found" # if an nba team name not found
               
reddit = bot_login()
submissions_replied_to = load_saved_submissions()
team_compliments = load_json_dict('json_files/team_compliments.json') # creates two dictionaries extracted from .json files
team_names = load_json_dict('json_files/team_names.json')
run_bot(reddit)
    
