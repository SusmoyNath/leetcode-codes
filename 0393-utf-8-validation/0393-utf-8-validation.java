class Solution {
    public boolean validUtf8(int[] data) {
        int remainingBytes = 0; // Counter for expected continuation bytes
        
        for (int num : data) {
            // Extract the 8 least significant bits
            int byteValue = num & 0xFF;
            
            if (remainingBytes == 0) {
                // Determine how many bytes the character should have
                if ((byteValue >> 5) == 0b110) { // 2-byte character
                    remainingBytes = 1;
                } else if ((byteValue >> 4) == 0b1110) { // 3-byte character
                    remainingBytes = 2;
                } else if ((byteValue >> 3) == 0b11110) { // 4-byte character
                    remainingBytes = 3;
                } else if ((byteValue >> 7) == 0b1) { // Single byte must start with '0'
                    return false;
                }
            } else {
                // Check if this is a valid continuation byte
                if ((byteValue >> 6) != 0b10) {
                    return false;
                }
                remainingBytes--;
            }
        }
        
        // If there are still expected bytes left, it's invalid
        return remainingBytes == 0;
    }
}
