class Solution {
   // int U=-1;D=1;L=2;R=-2;
   
    public boolean judgeCircle(String moves) {
         char[] gfg = moves.toCharArray(); 
         int sum = 0;
            for (int i = 0; i < gfg.length; i++) 
            {   
               if(gfg[i]=='U')
               {
                     sum= sum+1; 
               }else if(gfg[i]=='D'){
                   sum= sum-1; 
               }else if(gfg[i]=='L'){
                    sum= sum+2; 
               }else if(gfg[i]=='R'){
                    sum= sum-2; 
               }
        }
        if(sum==0){
            return true;
        }else{
            return false;
        }
    }
}
