#include <bits/stdc++.h>
using namespace std;

#define cval(x) cout << #x << " = " << x << " \n"

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int num;
        long long ans;

        cin >> num;
        ans = ((num * num) / 4) + 1;

        cout << ans << '\n';
    }

    return 0;
}