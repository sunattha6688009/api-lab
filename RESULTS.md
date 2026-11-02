# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: A Small Napoletana
- Step 0.12, results of the three runs without a session (optional): 1st run FAILED (401), 2nd run FAILED (401), 3rd run PASSED
- Step 0.16, blocks of "how many of the three tools are excluded": none (0 tools), one tool, two tools, all three tools

## Defect report
- Title: Excluding all three tools makes /api/pizza answer 500 with an empty body
- Request: POST /api/pizza with body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]} and a valid token
- Expected result: status 400 and a JSON error message
- Actual result: status 500 and an empty body
- Severity: Medium

## Part A
- Step A4, status codes when the other user reads, changes and deletes: read 404, update 400, delete 400

## Part B
1. Real server tests can find integration problems, such as a load balancer sending a request to the wrong server or the API answering 500. A unit test with stubs cannot see these. I still write unit tests with stubs because they are fast and show exactly which function failed.
2. The public token belongs to everyone, so other students could change my data while my test runs. Each test creates its own user, so no test disturbs another one. In Project 2, I will only change data that my own tests created.
3. A session keeps cookies, so every request goes to the same server. Without a session, the login can go to a server that does not know the new user. In my three runs, the login failed twice (401) and passed once.
4. The block "all three tools excluded" showed the defect. A 500 with an empty body gives the app no information, but a 400 with a message explains the problem. The test stays as xfail so the defect stays visible, and strict=True tells me when it is fixed.
5. Base choice: 1 + 2 + 3 + 1 + 2 = 9 tests. All combinations: 3 x 4 x 2 x 3 = 72 tests.
6. The codes were 404 (read), 400 (update) and 400 (delete). I expected 403 or 404. All attempts were refused and the rating did not change, so it is not a security defect, only a small inconsistency.
7. It returned status 200 and a list of ratings, although the token was made up. This is a defect, because the API should answer 401. A stranger could read data without a login.
8. An API test is better for trying many wrong inputs quickly. Only a test through the web pages can check what the user sees on the screen.