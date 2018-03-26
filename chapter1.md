---
title: Cost of Acquisition and Lifetime Value
description: >-
  Define onboarding funnels, cost of acquisition, and lifetime value. Discuss
  the transition from event logs, which describe particular actions, to rollups
  per user and ultimately to a funnel. We also introduce the idea of success and
  retention actions.
---

## Welcome to the Course!

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 84953f572c
```

Define Marketing Funnel and Cost of Acquisition, and motivate that we can use them to identify problem areas in signup. 

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Cost of Acquisition

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 742e640a0c
```

Which of these is a description of Cost of Acquisition as described in the video?

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sct`

```{python}

```
---

## Import Data

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: a55e48cd99
```

Import sample data into a DataFrame using read_csv.

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

## Select all data for a single user

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: f6beaa1087
```

User row filtering to identify all rows for a particular user identifier, sorted by time.

intermediate = df[df.UserId == 'sample-id']
intermediate.sort_values

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

## Marketing Funnel as a Series of Steps

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 9fe927edf0
```

Introduce the funnel for a subscription service and talk about the steps required to go from lead to success. Link these to events in the event logs.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Filter data to identify steps in the funnel

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 3915f90e8d
```

The key thing here is removing a redundant logging step. There will be some steps that are too granular and can be removed.

df_filtered = df[df.Event != 'badEvent']

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

## Find a user who completed the funnel

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 5f69dfbf33
```

Decide on success event, identify the first user who completed that event. The user has to do a few things here:
decide on an end event (and set it to a variable)
use that variable to filter to success events
use that filtered set to identify a single user.

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

## Defining Retention and Lifetime Value

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: d9eab070e8
```

Shift gears from onboarding to retention of successfully onboarded users.

The definition of "retained" depends on the context. In a subscription model, we can either focus on continuing to pay subscriptions or on continuing to do a high value event. High value events are preferred because they are a leading indicator, whereas subscription is a lagging indicator because by the time it happens it's too late.

In an ecommerce or transactional system, the retention event is often repeated successful use.

Describe that we use the retention definition to identify whether each user was retained in a particular time period.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Retention in a subscription business

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: 494da40a30
```

Which of these is not a good retention event in a subscription music business like Pandora or Spotify?

List a few events:
Subscription paid
Listen to song
Add station
Open application


`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sct`

```{python}

```
---

## Retention in an ecommerce business

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: ec5f2e6dc3
```

Which of these is a good retention event in an ecommerce business?

List a few events:
Pay for item
Add to cart
Search for item
Land on landing page

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sct`

```{python}

```
---

## Filter to retention events

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 7379977ad1
```

Identify retention events in the data set and filter to them.

df[df.Event == 'Completed']

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

## Was this user retained?

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: c9abe3af17
```

What is the last time that a sample user was retained? 

I'll give the user a sample id and have them identify all success events for that user, then list the last such event.

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
