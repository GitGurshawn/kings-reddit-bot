# kings-reddit-bot
A reddit bot that streams submissions form reddit.com/r/Kings. Its job is to search for submissions made by other team fans that come to compliment the Sacramento Kings. The bot will find the fan's team name and reply with a comment that compliments that specific team. The bot currently does not run on a server and runs locally.  

Example of how these types of submissions look: https://i.imgur.com/9l7WrnC.png
Example reply from the bot: https://i.imgur.com/3uTNBjc.png

HOW TO RUN:
1. Place 'bot.py', 'config.py', and the 'json_files' folder into the same directory
2. Edit 'config.py' and replace variables with the the bot account's information
3. Run 'bot.py'
4. A file called 'submissions_replied_to.txt' will be created if a submission is found and replied to. DO NOT delete this file or the bot will reply to the same submission again the next time the program is ran.
