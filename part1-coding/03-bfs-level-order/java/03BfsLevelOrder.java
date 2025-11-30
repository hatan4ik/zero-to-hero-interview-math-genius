import java.util.*;
class TreeNode { int val; TreeNode left,right; TreeNode(int v){val=v;} }
public class LevelOrder {
    public static List<List<Integer>> levelOrder(TreeNode root){
        List<List<Integer>> res=new ArrayList<>();
        if(root==null) return res;
        Queue<TreeNode> q=new LinkedList<>(); q.add(root);
        while(!q.isEmpty()){
            int size=q.size(); List<Integer> lvl=new ArrayList<>();
            for(int i=0;i<size;i++){
                TreeNode n=q.poll(); lvl.add(n.val);
                if(n.left!=null) q.add(n.left);
                if(n.right!=null) q.add(n.right);
            } res.add(lvl);
        } return res;
    }
}
