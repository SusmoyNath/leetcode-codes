class Solution(object):
    def findRelativeRanks(self, score):
        sorted_scores = {s: str(i + 1) for i, s in enumerate(sorted(score, reverse=True))}
        for i, medal in enumerate(["Gold Medal", "Silver Medal", "Bronze Medal"]):
            if i < len(score):
                sorted_scores[sorted(score, reverse=True)[i]] = medal
        return [sorted_scores[s] for s in score]