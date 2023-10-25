#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int i;
    cin >> i;
    vector<int> n(i);
    for(int t = 0; t < i; t++) {
        cin >> n[t];
    }
    sort(n.begin(), n.end());
    vector<int> T, F;
    for(int t = 0; t < i; t++) {
        if(n[t] >= 60) {
            T.push_back(n[t]);
        } else {
            F.push_back(n[t]);
        }
    }
    for(int t = 0; t < i; t++) {
        cout << n[t] << ' ';
    }
    cout << '\n';
    if(!T.empty() && !F.empty()) {
        cout << F.back() << '\n' << T.front() << '\n';
    } else if(T.empty()) {
        cout << F.back() << '\n' << "worst case" << '\n';
    } else {
        cout << "best case" << '\n' << T.front() << '\n';
    }
    return 0;
}
