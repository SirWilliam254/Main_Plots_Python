## Line Charts
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Add title
plt.title(" ")
# plot
sns.lineplot(data= )


## Scatter plot
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Add title
plt.title(" ")
# plot
sns.scatterplot(x= [' '], y= [' '])

## color coded scatter
sns.scatterplot(x= [' '], y= [' '], hue= [' '])


## Histogram
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Add title
plt.title(" ")
# plot
sns.distplot(a= [' '], kde=False) # if we do not set kde = false it produces a slightly different plot



## BarCharts
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

sns.barplot(x= .index, y= [' '])
plt.ylabel( )


## Heatmaps
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Setting the width and height of the figure
plt.figure(figsize=( , ))
# annot if set to true it shows the values in the heatmap
sns.heatmap(data= , annot=True)
# Add label for horizontal axis
plt.xlabel()


## Density plots
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

# Add title
plt.title(" ")
# KDE plot 
sns.kdeplot(data= [' '], shade=True)

# 2D KDE plot
sns.jointplot(x= [' '], y= [' '], kind="kde")

