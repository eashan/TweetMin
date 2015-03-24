#include<iostream>
#include<vector>

using namespace std;
 long gettrailingzeros(long n)
{
long i=0;
while(n%10==0)
{
i++;
}
return i;
}
long getfact(long n){
long fact=1;
for(long i=1;i<=n;i++)
{
fact=fact*i;
}
return fact;
}

int main(){

long t,n,i,j;
cin>>t;
vector <long> output(10000);

for(i=0;i<t;i++)
{
cin>>n;
output[i]=gettrailingzeros(getfact(n));
}
for(j=0;j<t;j++)
{
cout<<output[j]<<endl;

}


return 0;
}