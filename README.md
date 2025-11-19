# Manim Animation – Best Time to Buy and Sell Stock II

This repository contains a Manim animation that explains the LeetCode problem  
**“Best Time to Buy and Sell Stock II”**, including:

- Problem statement  
- Examples  
- Graph visualization  
- Step-by-step profit calculation  
- Greedy strategy explanation  
- Full C++ implementation  
- Full Python implementation  
- Final answer  

This animation was created as part of the **Python Developer Internship Assignment**.

---

## 📹 Video Link
**Google Drive Video:**  
<PASTE YOUR DRIVE LINK HERE>

---

## 📜 Problem Description

You are given an integer array `prices` where `prices[i]` is the price of a stock on the `i`-th day.

You may buy and sell multiple times, but you can hold at most **one stock** at a time.  
You may even buy and sell on the same day.

Your task is to return the **maximum profit** possible.

---

## 📊 Approach Used

The animation demonstrates the **Greedy Solution**:

- Loop through the array
- Add every **positive price difference** (`prices[i] − prices[i − 1]`)
- This simulates:
  - Buying whenever the price will rise tomorrow  
  - Selling at every peak  

This guarantees the maximum possible profit.

---

## Python Solution 

                class Solution:
                     def maxProfit(self, prices):
                       profit = 0
        
                       for i in range(1, len(prices)):
                            if prices[i] > prices[i - 1]:
                            profit += prices[i] - prices[i - 1]
        
                     return profit


## 🧠 C++ Code Used in the Animation

            ```cpp
                    class Solution {
                    public:
                       int maxProfit(vector<int>& prices) {
                       int profit = 0;

                       for (int i = 1; i < prices.size(); i++) {
                          if (prices[i] > prices[i - 1]) {
                             profit += prices[i] - prices[i - 1];
                          }
                         }
 
                       return profit;
                        }
                    };
