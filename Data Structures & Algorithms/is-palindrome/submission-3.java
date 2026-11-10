class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        char[] arr = s.toLowerCase().replaceAll("[^a-z0-9]", "").toCharArray();
        int r = arr.length - 1;

        while(l < r){
            if (arr[r] != arr[l]){
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
}
