#include<iostream>
using namespace std;
int main(){
	int n;
	cout<<"Enter the number to find even and odd";
	cin>>n;
	int i=0;
	while( i<=n){
		if(i%2==0)
			cout<<"even number\n";
		else 
			cout<<"odd number\n";
		i++;
	}
}
