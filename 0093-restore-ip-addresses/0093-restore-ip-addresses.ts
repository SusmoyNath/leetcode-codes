function restoreIpAddresses(s: string): string[] {
    const result: string[] = [];
    
    // Helper function to check if a given part is valid
    function isValid(part: string): boolean {
        // A part must be between 0 and 255 and cannot have leading zeros unless it's exactly "0"
        if (part.length > 1 && part[0] === '0') return false;
        const num = parseInt(part);
        return num >= 0 && num <= 255;
    }

    // Backtracking function to generate all possible IP addresses
    function backtrack(start: number, parts: string[]) {
        // If we have 4 parts and we've used up all characters in the string
        if (parts.length === 4) {
            if (start === s.length) {
                result.push(parts.join('.'));
            }
            return;
        }
        
        // Try all possible lengths for the next part (1 to 3 characters)
        for (let length = 1; length <= 3; length++) {
            if (start + length <= s.length) {
                const part = s.substring(start, start + length);
                if (isValid(part)) {
                    parts.push(part);
                    backtrack(start + length, parts);
                    parts.pop();
                }
            }
        }
    }

    backtrack(0, []);
    return result;
}
