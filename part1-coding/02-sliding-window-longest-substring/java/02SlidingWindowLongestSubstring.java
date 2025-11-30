import java.util.*;
public class LongestSubstring {
    public static int lengthOfLongestSubstring(String s){
        Set<Character> set = new HashSet<>();
        int l=0,b=0;
        for(int r=0;r<s.length();r++){
            while(set.contains(s.charAt(r))) set.remove(s.charAt(l++));
            set.add(s.charAt(r));
            b = Math.max(b, r-l+1);
        }
        return b;
    }
}
