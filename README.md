# Product Recommendations: A-Priori Algorithm

This is a popular data mining algorithm used for finding frequent item sets in large market-basket data.
If we have a frequent item set rule {x1, x2, x3}, then we say a basket containing items x1 and x2 is likely to contain item x3.
Once we have these rules, we can then make recommendations to customers based on what they have in their shopping cart while shopping.
This has applications in eCommerce (amazon, ebay, etc.), and in streaming services (Netflix, Hulu, Spotify, etc.).
This particular program finds frequent item sets of sizes 2 and 3 from a collection of past customer's shopping carts.
It then outputs the 5 top rules and their confidence scores.
To run, execute run_code.sh in terminal.
