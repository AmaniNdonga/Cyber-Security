from fbchat import Client
from fbchat.models import Message, MessageReaction

username = "ndonga50@gmail.com"
password = "itslit"

client = Client(username, password)

users = client.fetchThreadList()
print(users)

detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[0] for user in users]

sorted_detailed_users = sorted(detailed_users, key=lamda u: u.message_count, reverse=True)
best_friend = sorted_detailed_user[0]

print("Best Friend:", best_friend.name, "with a message count of", best_friend.message_count)

client.send(Message(
    text=f"Congratulations {best_friend.name}, you are {best_friend.message_count}"
    ),
    thread_id=best_friend.uid)

all_users = client.fetchAllUsers()

print("You talked with a total of", len(all_users), "users!")

