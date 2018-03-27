---
title: Funnel Analysis with Pivot Tables
description: >-
  Learn how to analyze the success rate of each step in a funnel. This chapter
  will focus on pivot tables on Pandas data frames. We'll also discuss how to
  present and plot a funnel analysis.
---

## Introducing the pivot_table command

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 9ceed2202d
```

Introduce the chapter, discuss the end goal (to compute the completion rate) and discuss the pivot_table command in pandas. We will include an example of pivot_table in the video.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Create a pivot table

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 14d5591ef1
```

Create a pivot table on user and event. Use the len function as aggfunc to determine whether each user did each event.

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

## Verify the pivot table output for one user

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 785c06a066
```

Find raw data corresponding to a single row in the pivot table.

Filter the raw data to a particular user and see that each row in the raw data shows up in one of the counts in the pivot table.

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

## Compute funnel completion using sum

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: bf7b2a24d6
```

We need to aggregate our data, which has one row per user, to data that has one row per event. We'll do this using the sum function on our dataframe.

Also introduce the idea of converting a table from ints to Booleans using df > 0

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Compute funnel using sum

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 9c01b968f8
```

Use sum function from the video to compute the number of users (not events) at each step.

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

## Reorder the output columns

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 5100414f82
```

Use a column multi-select to reorder the output from the default ordering (alphabetical) to the correct funnel order.

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

## Normalize the output to compute funnel completion rate

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: e58448cc5a
```

Divide by the number of people in first step.

funnel_output / funnel_output['start_event']

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

## Plotting the funnel completion using Pandas

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 581ffd1627
```

Pandas includes basic plotting functions that can be used to quickly visualize a Series or DataFrame. Discuss line charts and bar charts. You should use a line chart of there is a numerical relationship between the x-axis columns. An example would be percent of people working in each hour of the day. If the x-axis doesn't have a numerical relationship, use a bar chart.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Why should we use a bar chart?

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 3e8ba6c9fe
```

Select reason we should use a bar chart, not line chart, for funnels.

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sct`

```{python}

```
---

## Create a bar chart from the funnel output

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: b70b042920
```

Use pandas built-in bar charts to create a bar chart that shows the ratio of users completing each step.

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

## Finish chart by adding axis labels and title

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: fac45031d7
```

Use the title and ylabel functions to add a sensible title and y-axis label to the chart.

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

## Time to completion

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 7be7d31fcd
```

Introduce the idea of a leading and lagging indicator, and explain that our funnel analysis is a lagging indicator. One potential leading indicator is to compute the time taken to complete a funnel. To compute this, we'll use a min as the aggfunc and Timestamp as the column. Compute time difference between first start event and first end event, and plot a histogram of start times.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Filter to users who completed the funnel

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: ab1bdd1373
```

Use filtering to remove rows with n/a for completion event.

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

## Find the first time a user took each action

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 46496bc867
```

Switch aggfunc to min and value to Timestamp column.

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

## Compute time difference between start and first complete

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 5e9be68f3c
```

This exercise requires two things. First, compute a new column df['Timediff'] = df['Completed'] - df['Start'].
Second, convert the timedelta Timediff to hours.

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

## Plot a histogram of completion times

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 182400ef00
```

Use pandas hist function on the time delta column to plot how long the funnel takes.

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
