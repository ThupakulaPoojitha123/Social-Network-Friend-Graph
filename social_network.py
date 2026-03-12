from collections import deque, defaultdict

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(set)
    
    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = set()
    
    def add_friendship(self, user1, user2):
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)
    
    def remove_friendship(self, user1, user2):
        self.graph[user1].discard(user2)
        self.graph[user2].discard(user1)
    
    def get_friends(self, user):
        return list(self.graph[user])
    
    def mutual_friends(self, user1, user2):
        return list(self.graph[user1] & self.graph[user2])
    
    def friend_suggestions(self, user, top_k=5):
        suggestions = defaultdict(int)
        for friend in self.graph[user]:
            for friend_of_friend in self.graph[friend]:
                if friend_of_friend != user and friend_of_friend not in self.graph[user]:
                    suggestions[friend_of_friend] += 1
        
        sorted_suggestions = sorted(suggestions.items(), key=lambda x: -x[1])
        return [user for user, _ in sorted_suggestions[:top_k]]
    
    def shortest_path(self, user1, user2):
        if user1 == user2:
            return [user1]
        
        queue = deque([(user1, [user1])])
        visited = {user1}
        
        while queue:
            current, path = queue.popleft()
            for friend in self.graph[current]:
                if friend == user2:
                    return path + [friend]
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, path + [friend]))
        return []

if __name__ == "__main__":
    network = SocialNetwork()
    users = ["Alice", "Bob", "Charlie", "David", "Eve"]
    for user in users:
        network.add_user(user)
    
    network.add_friendship("Alice", "Bob")
    network.add_friendship("Alice", "Charlie")
    network.add_friendship("Bob", "David")
    network.add_friendship("Charlie", "Eve")
    
    print("Alice's friends:", network.get_friends("Alice"))
    print("Mutual friends of Alice and Bob:", network.mutual_friends("Alice", "Bob"))
    print("Friend suggestions for David:", network.friend_suggestions("David"))
    print("Path from Alice to Eve:", network.shortest_path("Alice", "Eve"))
