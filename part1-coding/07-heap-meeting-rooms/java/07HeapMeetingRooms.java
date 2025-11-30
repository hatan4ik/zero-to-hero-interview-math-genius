import java.util.*;
public class MeetingRoomsII {
    public static int minMeetingRooms(int[][] in){
        Arrays.sort(in,(a,b)->a[0]-b[0]);
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        for(int[] m: in){
            if(!pq.isEmpty() && pq.peek()<=m[0]) pq.poll();
            pq.add(m[1]);
        }
        return pq.size();
    }
}
