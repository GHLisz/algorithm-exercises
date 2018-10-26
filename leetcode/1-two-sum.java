class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int key = target - nums[i];
            if (seen.containsKey(key)) {
                return new int[]{seen.get(key), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }
}
