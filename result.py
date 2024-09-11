import json

def calculate_stats(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    num_tasks = len(data)
    total_reward = sum(item['reward'] for item in data)
    average_reward = total_reward / num_tasks if num_tasks > 0 else 0

    print(f"Number of tasks: {num_tasks}")
    print(f"Total reward: {total_reward}")
    print(f"Average reward: {average_reward}")

if __name__ == "__main__":
    calculate_stats('results.json')