from file_utils import load_with_pickle
from covid_point import CovidRecord

# load covid data as list of CovidRecord objects
data = load_with_pickle('covid_data.pickle')

# each element in data is a CovidRecord object. Each of which contains
# date, county, state, fips, cases, and deaths

# for example, we can print out the data for the first point in the US counties file
point = data[0]

print("Data: ", point.date, " County: ", point.county, " State: ", point.state,
      " FIPS: ",point.fips, " Cases: ", point.cases, " Deaths: ",point.death)

# write code to address the following question:
# When was the first positive COVID case in Rockingham County and Harrisonburg?

# write code to address the following question:
# What day was the greatest number of new daily cases recorded in Harrisonburg and Rockingham County?

# write code to address the following question:
# In terms of absolute number of cases, when was the worst seven day period in the city/county for new COVID cases?

# write code to address the following question:
# In terms of absolute number of cases, when was the rise in cases the fastest over a rolling week window?
# Over what period was the rise in cases the greatest
