#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long n, sum, x;

    cin >> n;
    sum = (n * (1 + n)) / 2;

    while (cin >> x)
    {
        sum = sum - x;
    }

    cout << sum << '\n';

    return 0;
}