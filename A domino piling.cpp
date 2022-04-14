#include<iostream>
#include<Math.h>


using namespace std;

int main(){
    int m,n;
    cin >>n;
    cin>>m;
	if(n%2==0){
		cout<< (n/2)*m;
	}
	else if(m%2==0){
		cout<< (m/2)*n;
	}
	else{
		cout << (n/2)*m + (m/2);
	}
    return 0;
}