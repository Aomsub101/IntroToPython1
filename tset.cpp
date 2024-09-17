#include <iostream>
#include <vector>

int square(int n){
    return n*n;
}

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n = 10;
    int result = square(n);

    cout << result;
}