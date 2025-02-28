var searchMatrix = function(matrix, target) {
    const m = matrix.length;
    const n = matrix[0].length;
    
    let low = 0;
    let high = m * n - 1;
    
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const midElement = matrix[Math.floor(mid / n)][mid % n]; // Convert mid index to 2D indices
        
        if (midElement === target) {
            return true;
        } else if (midElement < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    return false;
};
