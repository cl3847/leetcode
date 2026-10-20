class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        pos_words = set(positive_feedback)
        neg_words = set(negative_feedback)
        
        scores = {}
        for i, r in enumerate(report):
            count = 0
            for word in r.split(" "):
                if word in pos_words: count += 3
                if word in neg_words: count -= 1
            scores[student_id[i]] = count
        
        return sorted(scores, key=lambda item: (-scores[item], item))[:k]
