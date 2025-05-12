class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        vector<int> mpp(10, 0);
        for (int i = 0; i < digits.size(); i++)
            mpp[digits[i]]++;

        vector<int> res;
        for (int i = 1; i <= 9; i++) {
            if (mpp[i] == 0) continue;
            mpp[i]--;

            for (int j = 0; j <= 9; j++) {
                if (mpp[j] == 0) continue;
                mpp[j]--;
                for (int k = 0; k <= 8; k += 2) {
                    if (mpp[k] == 0) continue;
                    res.push_back(i*100 + j*10 + k);
                }
                mpp[j]++;

            }
            mpp[i]++;
        }
        return res;
    }
};

// Time Complexity: O(9*10*5) = O(450) = O(1)
// Space Complexity: O(1)
// The solution is efficient because the number of digits is limited to 10, and the number of even digits is limited to 5.
// The algorithm iterates through the digits and constructs 3-digit even numbers by checking the conditions for each digit.     
// The use of a frequency map (mpp) allows for efficient checking of available digits, and the nested loops ensure that all combinations are considered.
// The final result is stored in a vector (res) which is returned at the end of the function.
