# Credit risk evaluation rule-based system
## Rules (knowledge base)
It uses the idea of backward chaining, assuming that the loan will always be rejected.

```
    Rule1: IF Income = High THEN Approve_loan = Yes

    Rule2: IF Income = Medium E Has_bachelor_degree = Yes E
    Has_job = Yes THEN Approve_loan = Yes

    Rule3: IF Income = Medium E Has_bachelor_degree = Yes E
    Has_job = No THEN keep_searching = Yes

    Rule4: IF Income = Medium E Has_bachelor_degree = No E
    Has_job = No THEN Approve_loan = No

    Rule5: IF Income = Medium E Has_bachelor_degree = No E
    Has_job = Yes THEN keep_searching = Yes

    Rule6: IF Income = Low E References = Boas THEN
    keep_searching = Yes

    Rule7: IF Income = Low E References = Más THEN
    Approve_loan = No
```

<b>Goal variable: Approve_loan</b>