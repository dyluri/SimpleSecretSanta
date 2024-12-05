import random
import pickle

names_back_up = []
names = []

def get_response(message, username) -> str:
    global names
    global names_back_up
    p_message = message.lower()

    if p_message == '!enroll':
        names.append(username)
        names_back_up.append(username)
        return username + ', you have been placed into the secret santa'

    elif p_message == '!redo':
        names = names_back_up.copy()
        return 'Restarting Secret Santa! Number of people is back to ' + str(len(names))

    elif p_message == '!fullreset':
        names.clear()
        names_back_up.clear()
        return 'Names have been erased, please enroll or load names'

    elif p_message == '!people_left':
        return str(len(names)) + ' people are left'

    elif p_message == '!save_names':
        try:
            with open('names_list.pkl', 'wb') as file:
                pickle.dump(names_back_up, file)
            return str(len(names_back_up)) + ' names saved'
        except Exception:
            return 'Error with saving names, try again'

    elif p_message == '!load_names':
        try:
            with open('names_list.pkl', 'rb') as file:
                names_back_up = pickle.load(file)
            return str(len(names_back_up)) + ' names loaded, run `!redo`'
        except Exception:
            return 'Error with loading names, or no names have been saved, try again'

    # To visually see the remaining names:
    elif p_message == '!view_names_debug':
        if len(names) == 0:
            return 'No one enrolled'
        return ', '.join(names)
    
    elif p_message == '!help':
        return "`!enroll - places you into the secret santa\n!people_left - view how many people are left\n?draw - gives you a random name\n\n!save_names - saves the current list of names\n!load_names - loads the names last saved\n\n!fullreset - wipes everything except the save file`"

    # Add whatever else you want
    # elif p_message == 'whats updog?':
    #     return 'idk'

    else:
        return None
def get_private_response(message, username) -> str:
    p_message = message.lower()
    
    if p_message == 'draw':
        if len(names) == 0:
            return 'non one left to draw from'
        temp = random.choice(names)
        if len(names) == 1:
            if names[0] == username:
                return 'You are the last name in the drawing, please ask to !redo'

            while temp == username:
                temp = random.choice(names)
            print("Name is: ", temp)
            names.remove(temp)

            return 'You got: ' + temp + '!'