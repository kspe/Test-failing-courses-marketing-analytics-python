# Marketing Analytics in Python: Cost of Acquisition and Lifetime Value

## Chapter 1: Defining Cost of Acquisition and Lifetime Value

* Defining a Marketing Funnel and Cost of Acquisition
  * Import the data into a DataFrame
  * Identify events column in the funnel
  * Identify user identifier
  * Filter to a particular user
* Specifying steps in a Marketing Funnel
  * Build a data subset for funnel analysis
  * Identify funnel events
  * Filtering the data set to a subset of events
  * Find a particular user that completed the funnel
* Defining Retention and Lifetime Value
  * Decide on set of retention events
  * Subscription retention
  * Action-based retention and a "high value action"
  * Filter the data to retention events

## Chapter 2: Funnel Analysis with Pivot Tables

* Introducing Pivot Tables in Python
  * Trace a single user through a pivot table
  * Use the len function to compute number of events
  * Use the min function to identify first action time
* Computing absolute funnel completion
  * Using the sum function in pandas to compute funnel completion counts
  * Computing completion rate
  * Computing step-by-step completion rate
* Plotting funnel completion rate using pandas
  * Making a bar chart
  * Sorting the x-axis
  * Making relative bar chart
  * Labeling chart and axes
* Measuring time to completion
  * Using min function on time column to compute first time per action
  * Combine columns to compute time to action
  * Plotting a histogram

## Chapter 3: Lifetime Value: Computing Retention Rate

* Preparing timestamps: normalizing to active date and computing time since activation.
  * Computing cohorts using timestamp column: datetime
  * Computing time since activation and discretizing: timedelta
  * Computing a retention table with a pivot table
* Averaging across cohorts to compute retention rate
  * 28 days or monthly? Show difference
  * Using the mean and variance function on a dataframe
  * How does Pandas handle rolling data with missing values?
* Plotting retention curves with pandas
  * Bar chart or Line Chart
  * Visualizing changes in retention over time.
  * Adding titles and axis labels
* Introduce the Lifetime Value formula
  * Computing lifetime value for a single user (ecommerce) 
  * Projecting lifetime value for a currently active user
  * Computing estimated lifetime value for a cohort

## Chapter 4: Understanding Customer Sources

* Identifying customer sources
  * Importing sample logs and identifying referrer field
  * Introduce the apply function to simplify the referrer field
  * Introduce string.split to improve our referrer field. [n.b. would be great to have real data here]
* Joining Cost of Acquisition with Source information
  * use merge function to combine source information with the funnel logs
  * Left vs. inner join
  * Handling empty values in the source field
* Introducing GroupBy in pandas
  * Grouping on more than one index
  * Using GroupBy on the pivot table output to produce cost of acquisition for a source
* Wrapping up: which sources provide highest lifetime value?
  * combining funnel data with retention data
  * combining with attribution information
  * computing lifetime value per customer source
