from collections import defaultdict, deque

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(set)
    
    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = set()
    
    def add_friendship(self, user1, user2):
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)
    
    def get_friends(self, user):
        return list(self.graph[user])
    
    def mutual_friends(self, user1, user2):
        return list(self.graph[user1] & self.graph[user2])
    
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
    
    def friend_recommendations(self, user, top_k=3):
        recommendations = defaultdict(int)
        
        for friend in self.graph[user]:
            for fof in self.graph[friend]:
                if fof != user and fof not in self.graph[user]:
                    recommendations[fof] += 1
        
        return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:top_k]

if __name__ == "__main__":
    print("\n=== SOCIAL NETWORK ===")
    sn = SocialNetwork()
    
    while True:
        print("\n" + "="*40)
        print("1. Add User")
        print("2. Add Friendship")
        print("3. View Friends")
        print("4. Find Mutual Friends")
        print("5. Find Connection Path")
        print("6. Get Friend Recommendations")
        print("7. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            user = input("Enter username: ")
            sn.add_user(user)
            print(f"✓ User '{user}' added")
        elif choice == '2':
            user1 = input("Enter first user: ")
            user2 = input("Enter second user: ")
            sn.add_friendship(user1, user2)
            print(f"✓ {user1} and {user2} are now friends")
        elif choice == '3':
            user = input("Enter username: ")
            friends = sn.get_friends(user)
            print(f"{user}'s friends: {friends if friends else 'None'}")
        elif choice == '4':
            user1 = input("Enter first user: ")
            user2 = input("Enter second user: ")
            mutual = sn.mutual_friends(user1, user2)
            print(f"Mutual friends: {mutual if mutual else 'None'}")
        elif choice == '5':
            user1 = input("Enter start user: ")
            user2 = input("Enter end user: ")
            path = sn.shortest_path(user1, user2)
            if path:
                print(f"Connection path: {' -> '.join(path)}")
            else:
                print("No connection found")
        elif choice == '6':
            user = input("Enter username: ")
            recs = sn.friend_recommendations(user)
            if recs:
                print("Friend recommendations:")
                for name, count in recs:
                    print(f"  {name} ({count} mutual friends)")
            else:
                print("No recommendations")
        elif choice == '7':
            break