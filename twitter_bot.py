import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from keys import *
from config import *


# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'users_to_tag.txt'

def retrieve_users_id_from_file(FILE_NAME):
    with open(FILE_NAME) as file:
        id_list = file.readlines()
        id_list = [line.rstrip() for line in id_list]
    return id_list
    
def store_followers(id_list, file_name):
    with open(FILE_NAME, 'w') as fp:
        for item in id_list:
            # write each item on a new line
            fp.write("%s\n" % str(item))
        print('Done Writing '+ str(len(id_list)) + " ID's")
    return

def get_user_id_from_username(screen_name):
      
    # fetching the user
    user = api.get_user(screen_name)
      
    # fetching the ID and returning it
    return user.id_str
def get_username_from_id(user_id):
    
    user = api.get_user(user_id)
    return user.screen_name
    
def get_followers_of_target():
    followers = api.followers_ids(USER_ID, "rozhanzi")
    return followers
    
user_id_list = retrieve_users_id_from_file(FILE_NAME)

#print(api.user_timeline(1516666578775023620)[0].id)
count = 0
for x in range(100):
    api.update_status("@rozhanzi " + "@" + get_username_from_id(user_id_list[count]) + " @" + get_username_from_id(user_id_list[count + 1]) + " @" + get_username_from_id(user_id_list[count + 2]) + " @" + get_username_from_id(user_id_list[count + 3]) + " @" + get_username_from_id(user_id_list[count + 4]),1542508486243647498)
    count += 5
    time.sleep(5)
    print("comment posted, sleeping 5 seconds...")

api.update_status("@rozhanzi " + "@" + get_username_from_id(user_id_list[count]) + " @" + get_username_from_id(user_id_list[count + 1]) + " @" + get_username_from_id(user_id_list[count + 2]) + " @" + get_username_from_id(user_id_list[count + 3]) + " @" + get_username_from_id(user_id_list[count + 4]),1542508486243647498)


#followers = get_followers_of_target()
#store_followers(followers,FILE_NAME)

#print(get_user_id_from_username("Dr_raisi_fan"))
