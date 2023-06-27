import json

def save_history(history, filename):
    history_dict = history.history
    with open(f'saved_history/{filename}.json', 'w') as file:
        json.dump(history_dict, file)

def load_history(filename):
    with open(f'saved_history/{filename}.json', 'r') as file:
        loaded_history = json.load(file)
    if isinstance(loaded_history, dict):
        return loaded_history
    else:
        print("Error: Loaded history is not in the correct format.")
        return None

