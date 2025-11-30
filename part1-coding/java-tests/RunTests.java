import java.util.*;
public class RunTests {
    public static void main(String[] args){
        // TwoSum
        int[] r = TwoSum.twoSum(new int[]{2,7,11,15}, 9);
        assert r.length==2 && r[0]==0 && r[1]==1;

        // LongestSubstring
        int len = LongestSubstring.lengthOfLongestSubstring("abba");
        assert len==2;

        // MergeIntervals
        int[][] iv = new int[][]{{1,3},{2,6},{8,10},{15,18}};
        int[][] m = MergeIntervals.merge(iv);
        assert m.length==3 && m[0][0]==1 && m[0][1]==6;

        // ClimbStairs
        assert ClimbStairs.climbStairs(5)==8;

        // TopoSort
        int[][] edges = new int[][]{{1,0},{2,0},{3,1},{3,2}};
        int[] order = TopoSort.topoSort(4, edges);
        assert order.length==4;

        // MeetingRoomsII
        int[][] meet = new int[][]{{0,30},{5,10},{15,20}};
        assert MeetingRoomsII.minMeetingRooms(meet)==2;

        System.out.println("Java sanity tests passed.");
    }
}
