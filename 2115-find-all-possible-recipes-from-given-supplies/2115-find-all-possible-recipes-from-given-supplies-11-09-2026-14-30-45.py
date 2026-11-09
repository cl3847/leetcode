class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        unlocks = defaultdict(list)
        needed = defaultdict(int)
        relevant = set()

        for i in range(len(recipes)):
            for ing in ingredients[i]:
                rec = recipes[i]
                relevant.add(rec)
                unlocks[ing].append(rec)
                needed[rec] += 1

        queue = deque(supplies)
        res = []
        while queue:
            ing = queue.popleft()
            if ing in relevant:
                res.append(ing)

            for rec in unlocks[ing]:
                needed[rec] -= 1
                if needed[rec] == 0:
                    queue.append(rec)
        return res
            


        

