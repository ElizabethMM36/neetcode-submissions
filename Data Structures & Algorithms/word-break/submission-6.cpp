class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        // memo[i] stores: -1 for unvisited, 0 for false, 1 for true
        vector<int> memo(s.size(), -1);
        return dfs(s, wordSet, 0, memo);
    }

    bool dfs(const string& s, const unordered_set<string>& wordSet, int i, vector<int>& memo) {
        if (i == s.size()) {
            return true;
        }
        
        // Return cached result if we have already evaluated this index
        if (memo[i] != -1) {
            return memo[i] == 1;
        }

        for (int j = i; j < s.size(); j++) {
            if (wordSet.find(s.substr(i, j - i + 1)) != wordSet.end()) {
                if (dfs(s, wordSet, j + 1, memo)) {
                    memo[i] = 1; // Cache true result
                    return true;
                }
            }
        }
        
        memo[i] = 0; // Cache false result
        return false;
    }
};
