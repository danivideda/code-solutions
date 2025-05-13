/*
lengli_QAQ
Hope there are no bugs!!!
*/
#include <bits/stdc++.h>
#define fastio                    \
    std::ios::sync_with_stdio(0); \
    std::cin.tie(0);              \
    std::cout.tie(0)
#define all(x) x.begin(), x.end()
#define pb push_back
#define i64 long long

void solve()
{
    int n;
    std::cin >> n;
    std::vector<int> a(n), b(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> a[i];
        b[i] = a[i];
    }
    sort(all(b));
    if (b[0] == b.back())
    {
        std::cout << "No" << "\n";
        return;
    }
    std::cout << "Yes" << "\n";
    std::vector<int> res(n, 1);
    for (int i = 0; i < n; i++)
    {
        if (a[i] == b.back())
        {
            res[i] = 2;
            break;
        }
    }
    for (int i = 0; i < n; i++)
        std::cout << res[i] << " ";
    std::cout << "\n";
}

signed main()
{
    fastio;

    int T;
    std::cin >> T;
    while (T--)
        solve();

    return 0;
}