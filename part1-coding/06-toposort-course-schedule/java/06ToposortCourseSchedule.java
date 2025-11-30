import java.util.*;
public class TopoSort {
    public static int[] topoSort(int n, int[][] edges){
        List<List<Integer>> g=new ArrayList<>();
        for(int i=0;i<n;i++) g.add(new ArrayList<>());
        int[] indeg=new int[n];
        for(int[] e: edges){ g.get(e[1]).add(e[0]); indeg[e[0]]++; }
        Queue<Integer> q=new LinkedList<>();
        for(int i=0;i<n;i++) if(indeg[i]==0) q.add(i);
        int[] order=new int[n]; int k=0;
        while(!q.isEmpty()){
            int u=q.poll(); order[k++]=u;
            for(int v: g.get(u)) if(--indeg[v]==0) q.add(v);
        }
        return k==n?order:new int[0];
    }
}
