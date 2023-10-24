#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    int i;
    cin >> i;

    vector<int> l(i);
    for(int a = 0; a < i; a++) {
        cin >> l[a];
    }

    sort(l.begin(), l.end());

    map<int, int> count_map;
    for(int a = 0; a < i; a++) {
        count_map[l[a]]++;
    }

    int max_count = 0;
    for(auto const& pair: count_map) {
        max_count = max(max_count, pair.second);
    }

    for(auto const& pair: count_map) {
        if(pair.second == max_count) {
            cout << pair.first << " " << max_count << "\n";
        }
    }

    return 0;
}
