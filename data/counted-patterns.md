# Counted cascade patterns

Generated 2026-11-09 from https://uc-000.stratiqx.com/index.json by `scripts/count_patterns.py`. 331 published cases with a recorded cascade; 331 have two or more layers. Counts, not probabilities. A case can list several dimensions in one layer, so counts in a row can add up to more than the case count.

## Overall

| Dimension | Origin of | Reached in (any layer) | Lands in the last layer |
|---|---|---|---|
| D1 Customer | 50 | 301 of 331 | 65 of 331 |
| D2 Employee | 59 | 295 of 331 | 132 of 331 |
| D3 Revenue | 96 | 304 of 331 | 18 of 331 |
| D4 Regulatory | 57 | 285 of 331 | 158 of 331 |
| D5 Quality | 81 | 294 of 331 | 49 of 331 |
| D6 Operational | 74 | 312 of 331 | 33 of 331 |

## D1 Customer

- Origin in 50 multi-layer cases. Next layer includes: Revenue 29 of 50, Quality 26 of 50, Operational 23 of 50, Employee 5 of 50, Regulatory 2 of 50
- When Customer appears after the origin, the layer before it most often includes: Operational 118, Revenue 114, Quality 69
- Recent cases with this origin: [UC-305 The One That Actually Worked](https://uc-305.stratiqx.com) (D1>D3+D6>D5>D4, amplifying); [UC-300 The Accusation Was Enough](https://uc-300.stratiqx.com) (D1>D2+D5>D4+D6>D3, at-risk); [UC-282 The Coverage That's Quietly Disappearing](https://uc-282.stratiqx.com) (D1>D3+D6>D4+D5>D2, at-risk); [UC-277 The Click Nobody Sees](https://uc-277.stratiqx.com) (D1>D3+D6>D5+D4>D2, diagnostic)

## D2 Employee

- Origin in 59 multi-layer cases. Next layer includes: Revenue 31 of 59, Operational 27 of 59, Quality 18 of 59, Customer 13 of 59, Regulatory 7 of 59
- When Employee appears after the origin, the layer before it most often includes: Customer 102, Operational 100, Revenue 89
- Recent cases with this origin: [UC-341 Three Stars, Three Exits](https://uc-341.stratiqx.com) (D2>D4+D3>D6+D1, diagnostic); [UC-334 Answered in Kind](https://uc-334.stratiqx.com) (D2>D4+D5>D6+D1, amplifying); [UC-327 Both Teams Bought an Identity](https://uc-327.stratiqx.com) (D2>D3+D5>D6+D1+D4, diagnostic); [UC-320 Less Heads, More Heads](https://uc-320.stratiqx.com) (D2>D3+D6, diagnostic)

## D3 Revenue

- Origin in 96 multi-layer cases. Next layer includes: Operational 65 of 96, Customer 43 of 96, Quality 32 of 96, Regulatory 20 of 96, Employee 16 of 96
- When Revenue appears after the origin, the layer before it most often includes: Operational 74, Quality 62, Customer 50
- Recent cases with this origin: [UC-324 Full Rebuild](https://uc-324.stratiqx.com) (D3>D6+D2>D5+D1, diagnostic); [UC-323 The Twenty Percent Ceiling](https://uc-323.stratiqx.com) (D3+D4>D2+D6>D1+D5, diagnostic); [UC-322 $53 Billion Passed, $8 Billion Spent](https://uc-322.stratiqx.com) (D3>D6+D1, diagnostic); [UC-316 75 Up, 75 Down](https://uc-316.stratiqx.com) (D3>D6+D1, diagnostic)

## D4 Regulatory

- Origin in 57 multi-layer cases. Next layer includes: Revenue 36 of 57, Operational 29 of 57, Customer 25 of 57, Quality 14 of 57, Employee 11 of 57
- When Regulatory appears after the origin, the layer before it most often includes: Revenue 91, Quality 90, Operational 82
- Recent cases with this origin: [UC-337 Old Because It Was Free](https://uc-337.stratiqx.com) (D4>D6+D3>D5+D1, diagnostic); [UC-333 Infinitely Many Is Not Every](https://uc-333.stratiqx.com) (D4>D5+D6>D2+D1, diagnostic); [UC-330 The Trouble Was Only at the Crossings](https://uc-330.stratiqx.com) (D4>D5+D2>D6+D1, diagnostic); [UC-326 The Stick Tariff Is a Liquor Tariff](https://uc-326.stratiqx.com) (D4>D6+D3>D1+D2, diagnostic)

## D5 Quality

- Origin in 81 multi-layer cases. Next layer includes: Operational 45 of 81, Revenue 39 of 81, Customer 29 of 81, Regulatory 13 of 81, Employee 12 of 81
- When Quality appears after the origin, the layer before it most often includes: Operational 108, Revenue 91, Customer 74
- Recent cases with this origin: [UC-342 Now the Work Begins](https://uc-342.stratiqx.com) (D5>D2+D6>D4+D1, amplifying); [UC-340 Every Dimension, Three Months Later](https://uc-340.stratiqx.com) (D5>D2+D6>D4+D1, amplifying); [UC-339 Two Machines, One Hypothesis](https://uc-339.stratiqx.com) (D5>D6+D2>D4+D1, amplifying); [UC-338 Translation Was Never the Hard Part](https://uc-338.stratiqx.com) (D5>D3+D6>D2+D1, diagnostic)

## D6 Operational

- Origin in 74 multi-layer cases. Next layer includes: Revenue 55 of 74, Quality 35 of 74, Customer 33 of 74, Employee 11 of 74, Regulatory 11 of 74
- When Operational appears after the origin, the layer before it most often includes: Revenue 103, Quality 76, Customer 46
- Recent cases with this origin: [UC-336 How to Read a Book You Can't Open](https://uc-336.stratiqx.com) (D6>D2+D5>D4+D1, amplifying); [UC-335 Thirty-Six to Find One](https://uc-335.stratiqx.com) (D6>D2+D5>D4+D1, amplifying); [UC-319 The Fleet Doubled. The Coverage Didn't](https://uc-319.stratiqx.com) (D6>D3+D5, diagnostic); [UC-315 Nobody Did Anything Wrong](https://uc-315.stratiqx.com) (D6>D3+D5, diagnostic)
