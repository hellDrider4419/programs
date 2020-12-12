#include<iostream>
using namespace std;
int main(){
	int a=0,b=1,sum=0;
	int i=0,n;
	cout<<"enter the number to print faboncci serie";
	cin>>n;
	cout<<a<<" "<<b<<" ";
	while(i<=n){
		sum=a+b;
		a=b;
		b=sum;
		cout<<sum<<" ";
		i++;
	}
}
