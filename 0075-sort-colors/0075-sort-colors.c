void sortColors(int* nums, int numsSize) {
    int low = 0, mid = 0, high = numsSize - 1;

    while (mid <= high) {
        if (nums[mid] == 0) {
            // Swap nums[low] and nums[mid], then increment low and mid
            int temp = nums[low];
            nums[low] = nums[mid];
            nums[mid] = temp;
            low++;
            mid++;
        } else if (nums[mid] == 1) {
            // If it's 1, it's already in the correct place, just move mid
            mid++;
        } else {
            // Swap nums[mid] and nums[high], then decrement high
            int temp = nums[mid];
            nums[mid] = nums[high];
            nums[high] = temp;
            high--;
        }
    }
}
