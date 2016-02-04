#include "Solution.h"

bool Solution::canWinNim(int n) {
    //if(n<=3) return true;
    //bool* win=new bool[n+1];
    //win[1]=win[2]=win[3]=true;
    //for(int i = 4; i <= n; i++) {
        //win[i] = !win[i-1]||!win[i-2]||!win[i-3];
    //}
    //return win[n];
	
	/* the code above uses DP to prove the rest result */
	return n%4!=0; // :)
}
