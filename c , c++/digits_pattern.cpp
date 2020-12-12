#include<iostream>
using namespace std;
int main(){
	for(int i=1;i<6;i++){
		for(int j=1;j<6;j++){
			if((i>=2&&i<=4)&&(j>=2&&j<=4))
				cout<<" ";
			else
				cout<<"*";
		}
		cout<<"\n";
	}
	for(int i=1;i<6;i++){
		for(int j=1;j<2;j++){
			cout<<"*";
		}
		cout<<"\n";
	}
	cout<<"\n";
	for(int i=1;i<6;i++){
		for(int j=1;j<6;j++){
			if((i==2&&j<=4)||(i==4&j>=2))
				cout<<" ";
			else
				cout<<"*";
		}
		cout<<"\n";
	}
	cout<<"\n";
	for(int i=1;i<6;i++){
		for(int j=1;j<6;j++){
			if((i==2||i==4)&&j<=4)
				cout<<" ";
			else
				cout<<"*";
		}
		cout<<"\n";
	}
	cout<<"\n";
	for(int i=1;i<6;i++){
		for(int j=1;j<6;j++){
			if((j>=2&&j<=4&&i<=2)||(i>=4&&j<=4))
				cout<<" ";
			else
				cout<<"*";
		}
		cout<<"\n";
	}
	cout<<"\n";
	for(int i=1;i<6;i++){
		for(int j=1;j<6;j++){
			if((i==2&&j>=2)||(i==4&j<=4))
				cout<<" ";
			else
				cout<<"*";
		}
		cout<<"\n";
	}
	cout<<"\n";
	for(int i=1;i==1;i++){
		for(int j=1;j<6;j++){
			if((i<=2&&j>=2)||(i>=2&&i<=4&&j==4))
				cout<<" ";
			else
				cout<<"*";
		}
		cout<<"\n";
	}
}
