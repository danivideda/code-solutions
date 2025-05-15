#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define cval(x) cout << #x << " = " << x << " \n"

int main()
{
    int n;
    cin >> n;

    ll prev, res = 0;
    cin >> prev;

    for (int i = 1; i < n; i++)
    {
        ll curr;
        cin >> curr;

        ll count = prev - curr;
        if (count > 0) 
        {
            res = res + count;
        } else
        {
            prev = curr;
        }
    }

    cout << res << '\n';
    

    return 0;
}