#include <iostream>
#include <bits/stdc++.h>
using namespace std;
void InOut(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
        #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
}
int main() {
	// your code goes here
	InOut();
	int test;
	cin>>test;
	while(test--){
	    int n,q,m;
	    cin>>n>>q>>m;
	    int a[n];
	    for(int i=0;i<n;i++)
	        cin>>a[i];
        int x[1000001]={};
        map <pair<int,int>,int> in;
        while(q--){
            int l,r;
            cin>>l>>r;
            l--,r--;
            if(a[l]>m){
                continue;
            }
            else if(a[l]<=m && a[r]>m){
                x[a[l]]++;
                x[m+1]--;
            }else{
                x[a[l]]++;
                x[m+1]--;
                in[{a[l],a[r]}]++;
            }
        }
        for(auto y:in){
            int ai=y.first.first;
            int bi=y.first.second;
            int l=y.second;
            x[bi+ai]-=l;
            x[bi + 2 * ai]+=l;
            int  c=bi + 2 * ai;
            while(c+bi <= m){
                c+=bi;
                x[c]-=l;
                x[c+ai]+=l;
                c+=ai;
            }
        }
        int mi=0;
        for(int i=1;i<=m;i++){
            x[i]+=x[i-1];
            mi=max(mi,x[i]);
        }
        cout<<mi<<endl;
	}
// 	return 0;
}