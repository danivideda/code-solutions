#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define cval(x) cout << #x << " = " << x << " \n"

int main()
{
    string str;
    cin >> str;

    int maximum = 1, temp = 1;

    for (int i = 1; i < int(str.length()); i++)
    {
        if (str[i - 1] == str[i])
        {
            temp++;
            maximum = max(maximum, temp);
        } else 
        {
            temp = 1;
        }
    }

    cout << maximum << '\n';

    return 0;
}