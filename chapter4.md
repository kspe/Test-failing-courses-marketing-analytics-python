---
title: Understanding Customer Sources
description: >-
  Discover which sources of data are producing valuable customers. 


  This chapter will introduce customer acquisition data and cost of acquisition,
  funnels by channel, and LTV as a function of cost of acquisition. We'll
  primarily discuss the merge function in pandas.
---

## Tracking customer source through the funnel.

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: 6a8a766812
```

Discuss the basic idea of tagging a user and building a data set of acquisition channel per user.

There are many companies doing this work, particularly in conjunction with ad sales. Examples are Facebook and Google.

While these companies provide many interesting features, it's important to understand both the basic idea behind customer source tracking and to develop tools we can use for any acquisition channel.

The core data requirement is a data set that includes user id and source information. Other useful information like cost of ad click could be included if it's available.

In this section, we'll start with acquisition channel then move to paid acquisition.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Extract source data from raw URLs

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 316d124c68
```

One common source of data in the web is http referrer field, which tracks the URL that a user was on when they clicked on your page. Use string functions (hint: split and indexing) to identify the site that a user came from.

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

## Use Apply Function to apply a function to every row

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: c097066701
```

Using the string cleanup logic from previous exercise, use the DataFrame.apply function to apply those changes to every row in the frame.

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

## Extract paid clicks

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 1a20c02ffe
```

Explain that some urls are evidence of a paid ad. Create a function that identifies whether the string is a boolean ad. Use apply to run this function on every referrer.

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

## Joining acquisition data to the funnel

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: c00a52013b
```

Explain that event data will have a user id, but it will not have attribution data on every row. 

However, some rows will have attribution data. It's common to extract this data into an attribution data set.

We can join the attribution data to our funnel data using the merge function.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Extract acquisition data from raw funnel logs.

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: b94cd1d3b6
```

Introduce new data set, which is the same as data in Chapter 2 but includes referrer information when available. Exercise is to filter to only rows that have funnel data.

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

## Merge the data to user-aggregated step of the funnel

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 8e9b9f874e
```

df.merge(small_df) using left join. The key thing here is to merge at right place: you have to merge to UserId

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

## Finish the funnel, grouping by acquisition source. 

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: cb0553de90
```

Instead of just sum, must use groupby then agg(sum) on the pivoted data.

This will produce a long tail of sources.

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

## Clean aggregation source

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: f1e9049626
```

This exercise is a repeat of 7 and 8, but before merging, add an apply function that classifies incoming source as either google, facebook, paid ad (using definition from earlier exercise) or "other"

Outcome is a set of 4 funnels.

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

## Thinking about funnel sources: good leads vs plentiful leads

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: d4b75e260a
```

Some user sources may provide many but low value users. Other sources may have few but high value users. Introduce cost of acquisition, which helps us determine the cost of getting a paying user.

Cost of acquisition for a channel is the amortized cost of acquiring a user from that channel including money spent on leads that didn't convert. So a channel with higher conversion rates can be a better deal.

To compute this, we need to introduce costs. We'll work with sample data from Facebook and Google ad spends, broken out by campaign. We'll focus on CPC data, which means you only paid for a user that clicked your ad.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Introducing ad data

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: cae5c555ce
```

Introduce sample data set that includes columns for user, ad source, ad cost, and ad campaign.

Exercise is to compute the average cost of each campaign using groupby and agg.

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

## Merge ad data to main data set

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 350e30d82a
```

Merge the ad data using df.merge on user id. Assume that any users who don't have an ad click are organic traffic with zero cost. 

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

## Compute cost of acquisition

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 53f20eeb37
```

GroupBy channel to compute the cost of the channel (total spend on all ads) and the number of sales.

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

## Plot cost of acquisition per channel

```yaml
type: NormalExercise
lang: python
xp: 100
skills: 2
key: 1512dbdb63
```

Create a bar chart using pandas bar chart (we had a bar chart earlier - this is primarily so we repeat the idea)

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

## Wrap Up

```yaml
type: VideoExercise
lang: python
xp: 50
skills: 2
key: c3014d0287
```

Summarize the cost of acquisition flow. There are services that will do this work for you, particularly services that sell ads. The advantage of knowing how to do it in python is that you can combine data from many individual sources.

`@video_link`

//player.vimeo.com/video/154783078

`@video_hls`

//videos.datacamp.com/transcoded/000_placeholders/v1/hls-temp.master.m3u8
---

## Interpret the acquisition channel

```yaml
type: MultipleChoiceExercise
lang: python
xp: 50
skills: 2
key: f07af4c0d6
```

There will be one channel with more leads but higher cost of acquisition because it has a low funnel completion rate. 

`@instructions`


`@hint`


`@pre_exercise_code`

```{python}

```

`@sct`

```{python}

```
