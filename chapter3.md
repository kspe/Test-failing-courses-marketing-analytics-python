---
title: 'Lifetime Value: Computing Retention Rate'
description: >-
  Once a lead has converted to a customer, we want to track how long we retain
  them as a customer. The definition of retained depends on the kind of business
  one is doing, but the analysis we will is applicable to many definitions of
  retention. We'll discuss cohorts, or groups of users who activate in the same
  time period, then we'll discuss retention rates within subsequent time
  windows. Finally, we'll discuss how to estimate lifetime value of a user from
  the customer retention rate.
---

## Introducing cohorts and retention time periods

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: e42e214412
```

Introduce the new theoretical concepts in this chapter. The most important new concept is computing cohorts by rounding timestamps down to the nearest week or month. 

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Filter data to include only activation event and retention events.

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 80b668f37c
```

Filter out events that aren't the actual activation event. This is very similar to an exercise in chapter 1 and should be fast. 

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Add a column for year and month

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: e5c2a37e6e
```

Discretize time using strptime and make a new column.

df['yearmonth'] = df.timestamp.apply(lambda x: x[:7])

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Compute cohort period using groupby and agg

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: a60cfa7242
```

Compute a new dataframe that contains the first discrete timeframe per user.

df_cohort = df.groupby('user_id').agg({'yearmonth': min})
df_cohort.columns = ['cohort']
df_cohort.reset_index()  # this makes the merge below easier to conceptualize.

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Compute retention table

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 702898889b
```

Use a pivot_table with cohort as the index, retention period as the columns, and count of distinct users as the aggfunc and value.

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Make a retention table using the merge function

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 1781d6bf94
```

Describe two data sets: original data with one row per event and the new data with one row per user.

Introduce merge. Explain that we'll combine rows from the two data sets.
Explain using pivot table to compute retention. Index is cohort period and columns are yearmonth

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Merge two data sets

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 06959a8895
```

df_merged = df.merge(df_cohort, on='user_id')

Verify that the output has the cohort for each user

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Pivot table to produce a cohort table

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 4f7c107ec3
```

df_merged.pivot_table(index='cohort', columns='yearmonth', aggfunc=len, values='user_id')

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Computing average retention

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 689d230ba4
```

Steep dropoff in first cohort cycle followed by more shallow dropoff. This is common.
Non-zero in upper right, but this means that average retention in every month is misleading. It's better to compute retention by normalizing dates. Explain what that is and why it matters.

Python concepts: using a custom function in an apply.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Normalize dates in the original data

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: b9e5a864c7
```

Use datetime subtraction to normalize dates. This will require writing a function that we use in apply.

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Create table with time from activation as the y-axis

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 154f2dc645
```

Similar to pivot table above.

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Plotting retention curves

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 6a7270b609
```

Use line chart to plot each retention curve.

Update axis and title

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Interpreting the retention chart

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 7f0ca0ae08
```

The data will show retention increasing over time. Multiple choice will include options:

3-month retention has gone down over time
3-month retention has increased over time
3-month retention is about the same
12-month retention is down over time [impossible to measure since should only have 1 data point at that retention level]

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sct`

```{python}

```
---

## Presenting Retention Analysis: Curves and LTV

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 59ae7113c8
```

Review the retention curves. Point out how to identify changes in the curve over time.

Introduce lifetime value and how to compute it. 

LTV is the expected total profit from a customer. We'll discuss it for subscription models, where revenue is fixed per customer in a cycle. In this model, LTV is simply number of months of revenue generated times monthly fee.

To compute expected retention period, use 1 / churn rate.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Compute Churn rate excluding first 

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 261b1f4009
```

Compute the average churn rate for the retention funnel.

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
---

## Compute LTV

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: dcfcc6d4a0
```

Assuming a value of $15/month, what is the expected LTV in this funnel?

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sample_code`

```{python}

```

`@solution`

```{python}

```

`@sct`

```{python}

```
