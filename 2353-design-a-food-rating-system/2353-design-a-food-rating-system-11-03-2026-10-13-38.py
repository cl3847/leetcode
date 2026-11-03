class FoodRatings:
    # option 1:
    # hashmap (cuisine, list<food>)
    #   - maintaining sorted order in the list is nlogn
    #   - retrieving would be o(1)

    # option 2:
    # heap 
    # changing a rating is potentially complex (hard to retrieve single item?)
    # we could get the highest rated item in constant time 
    # init would be faster
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisines = defaultdict(list)
        self.foods = {}
        for i in range(len(foods)):
            f, c, r = foods[i], cuisines[i], ratings[i]
            pair = (-r, f, c)
            heappush(self.cuisines[c], pair)
            self.foods[f] = pair

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.foods[food][2]
        pair = (-newRating, food, c)
        self.foods[food] = pair
        heappush(self.cuisines[c], pair)

    def highestRated(self, cuisine: str) -> str:
        best = self.cuisines[cuisine][0]
        while best[0] != self.foods[best[1]][0]:
            heappop(self.cuisines[cuisine])
            best = self.cuisines[cuisine][0]
        return best[1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)