# harvest_tracker
class activity 
---
A local farming cooperative needs a program to record the weight
of 4 crates of produce from a single harvest. The program
calculates the total weight and checks if the batch meets the
"Export Quality" standard.


----
Requirement:

User Details: Collect the Farmer's Name and the Batch Code.

Validation:

Batch Code must be exactly 6 characters and start with "GR-" (e.g., "GR-001").

Individual crate weight must be between 5kg and 50kg.

Selection (Logic):

If a crate weighs more than 40kg, mark it as "Heavy Load."

If the average weight of the 4 crates is above 30kg, the batch is "Export Grade."

Iteration (For Loop): Use a for loop to strictly collect exactly 4 crate weights.

Output Summary: An itemized "Harvest Report" showing:

Farmer Name & Batch Code.

Individual weights of all 4 crates.

Total weight and Export Status.
