# Social Network Friend Graph

## Description
Graph-based social network with friend connections, suggestions, and pathfinding.

## Features
- Add/remove friendships
- Find mutual friends
- Friend suggestions algorithm
- Shortest path between users
- BFS-based connection discovery

## Usage
```python
network = SocialNetwork()
network.add_user("Alice")
network.add_friendship("Alice", "Bob")
suggestions = network.friend_suggestions("Alice")
```

## Run
```bash
python social_network.py
```
