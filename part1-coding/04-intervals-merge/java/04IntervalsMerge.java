import java.util.*;
public class MergeIntervals {
    public static int[][] merge(int[][] in){
        Arrays.sort(in,(a,b)->a[0]-b[0]);
        List<int[]> res=new ArrayList<>();
        for(int[] cur: in){
            if(res.isEmpty() || res.get(res.size()-1)[1] < cur[0]) res.add(new int[]{cur[0],cur[1]});
            else res.get(res.size()-1)[1] = Math.max(res.get(res.size()-1)[1], cur[1]);
        }
        return res.toArray(new int[res.size()][]);
    }
}
