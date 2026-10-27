class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        matches = defaultdict(list)
        for path in paths:
            path = path.split(" ")
            path, files = path[0], path[1:]
            for file in files:
                file, _, content = file.partition('(')
                matches[content].append(path + "/" + file)
        return [l for k, l in matches.items() if len(l) > 1]