# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401 "error":"authentication failed"
- Step 0.4, the name of your pizza: A Small Napoletana
- Step 0.12, results of the three runs without a session (optional): 1st time FAILED 401, 2nd time FAILED 401, 3rd time PASSED
- Step 0.16, blocks of "how many of the three tools are excluded": none (0 tools), one tool, two tools, all three tools

## Defect report
- Title: Excluding all three tools makes /api/pizza answer 500 with an empty body
- Request: POST /api/pizza with body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]} and a valid token
- Expected result: status 400 and a JSON error message
- Actual result: status 500 and an empty body
- Severity: Medium (the server fails on a valid but impossible request, and the caller gets no message)

## Part A
- Step A4, status codes when the other user reads, changes and deletes: read 404 ({"error":"not found"}), update 400 ({"error":"rating ID...not found"}), delete 400 ({"error":"rating ID...not found"})
| Characteristic | Blocks | Values in the tests |
|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short |

## Part B
1.
2.
3.
4.
5.
6.
7.
8.
