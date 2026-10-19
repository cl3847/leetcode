class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        queue = deque(friends[id])
        seen = set([id] + friends[id])
        counts = {}
        i = 1
        while queue:
            for _ in range(len(queue)):
                person = queue.popleft()
                if level == i:
                    for video in watchedVideos[person]:
                        counts[video] = counts.get(video, 0) + 1
                else:
                    for friend in friends[person]:
                        if not friend in seen:
                            queue.append(friend)
                            seen.add(friend)
            i += 1
        
        return sorted(counts, key=lambda x: (counts.get(x), x))
                
        