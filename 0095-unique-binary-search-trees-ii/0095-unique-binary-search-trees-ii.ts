class BSTNode {
    val: number;
    left: BSTNode | null;
    right: BSTNode | null;
    constructor(val?: number, left?: BSTNode | null, right?: BSTNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
}

function generateTrees(n: number): BSTNode[] {
    // Base case: if n is 0, return an empty array of trees.
    if (n === 0) return [];
    
    // Recursive function to generate all trees from values between start and end.
    function buildTrees(start: number, end: number): BSTNode[] {
        const result: BSTNode[] = [];
        
        if (start > end) {
            result.push(null); // Base case: return an empty tree
            return result;
        }
        
        for (let i = start; i <= end; i++) {
            // Generate all possible left subtrees
            const leftSubtrees = buildTrees(start, i - 1);
            // Generate all possible right subtrees
            const rightSubtrees = buildTrees(i + 1, end);
            
            // Combine each left and right subtree with the root i
            for (const left of leftSubtrees) {
                for (const right of rightSubtrees) {
                    const root = new BSTNode(i);
                    root.left = left;
                    root.right = right;
                    result.push(root);
                }
            }
        }
        
        return result;
    }
    
    return buildTrees(1, n);
}
