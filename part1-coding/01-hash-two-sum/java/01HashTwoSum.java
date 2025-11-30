import java.util.*;
public class TwoSum {
    public static int[] twoSum(int[] a, int t){
        Map<Integer,Integer> m = new HashMap<>();
        for(int i=0;i<a.length;i++){
            int need = t - a[i];
            if(m.containsKey(need)) return new int[]{m.get(need), i};
            m.put(a[i], i);
        }
        return new int[0];
    }
}
