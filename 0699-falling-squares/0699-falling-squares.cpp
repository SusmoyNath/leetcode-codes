#include <bits/stdc++.h>
using namespace std;

class SegmentTree {
    vector<int> tree, lazy;
    int size;

public:
    SegmentTree(int n) {
        size = n;
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
    }

    void pushDown(int node, int start, int end) {
        if (lazy[node] != 0) {
            tree[node] = max(tree[node], lazy[node]);
            if (start != end) {
                lazy[node * 2] = max(lazy[node * 2], lazy[node]);
                lazy[node * 2 + 1] = max(lazy[node * 2 + 1], lazy[node]);
            }
            lazy[node] = 0;
        }
    }

    void update(int node, int start, int end, int l, int r, int val) {
        pushDown(node, start, end);
        if (start > r || end < l) return;
        if (start >= l && end <= r) {
            lazy[node] = max(lazy[node], val);
            pushDown(node, start, end);
            return;
        }
        int mid = (start + end) / 2;
        update(node * 2, start, mid, l, r, val);
        update(node * 2 + 1, mid + 1, end, l, r, val);
        tree[node] = max(tree[node * 2], tree[node * 2 + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        pushDown(node, start, end);
        if (start > r || end < l) return 0;
        if (start >= l && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return max(query(node * 2, start, mid, l, r), query(node * 2 + 1, mid + 1, end, l, r));
    }
};

class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        set<int> coords;
        for (auto& p : positions) {
            coords.insert(p[0]);
            coords.insert(p[0] + p[1] - 1);
        }

        unordered_map<int, int> index;
        int idx = 1;
        for (int x : coords) index[x] = idx++;

        SegmentTree segTree(idx + 1);
        vector<int> result;
        int maxHeight = 0;

        for (auto& p : positions) {
            int l = index[p[0]], r = index[p[0] + p[1] - 1];
            int h = segTree.query(1, 1, idx, l, r) + p[1];
            segTree.update(1, 1, idx, l, r, h);
            maxHeight = max(maxHeight, h);
            result.push_back(maxHeight);
        }
        return result;
    }
};
