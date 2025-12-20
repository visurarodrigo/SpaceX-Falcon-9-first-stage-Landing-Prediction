import pandas as pd

# Read the SpaceX data
df = pd.read_csv('spacex_launch_data_clean.csv')

print("=" * 80)
print("SPACEX LAUNCH DATA ANALYSIS - INSIGHTS")
print("=" * 80)

# Question 1: Which site has the largest successful launches?
print("\n1. Which site has the LARGEST SUCCESSFUL LAUNCHES?")
print("-" * 80)
success_by_site = df[df['Class'] == 1].groupby('LaunchSite').size().sort_values(ascending=False)
print(success_by_site)
print(f"\n✓ Answer: {success_by_site.idxmax()} with {success_by_site.max()} successful launches")

# Question 2: Which site has the highest launch success rate?
print("\n\n2. Which site has the HIGHEST LAUNCH SUCCESS RATE?")
print("-" * 80)
success_rate = df.groupby('LaunchSite').agg({
    'Class': ['sum', 'count', 'mean']
}).round(4)
success_rate.columns = ['Successful', 'Total', 'Success_Rate']
success_rate['Success_Rate_Pct'] = (success_rate['Success_Rate'] * 100).round(2)
success_rate = success_rate.sort_values('Success_Rate', ascending=False)
print(success_rate)
print(f"\n✓ Answer: {success_rate.index[0]} with {success_rate['Success_Rate_Pct'].iloc[0]}% success rate")

# Question 3 & 4: Which payload range(s) has the highest/lowest launch success rate?
print("\n\n3 & 4. Which payload range has the HIGHEST and LOWEST launch success rate?")
print("-" * 80)
df['PayloadRange'] = pd.cut(df['PayloadMass'], 
                             bins=[0, 2000, 4000, 6000, 8000, 10000, 15000], 
                             labels=['0-2000', '2000-4000', '4000-6000', '6000-8000', '8000-10000', '10000+'])
payload_analysis = df.groupby('PayloadRange', observed=True).agg({
    'Class': ['sum', 'count', 'mean']
}).round(4)
payload_analysis.columns = ['Successful', 'Total', 'Success_Rate']
payload_analysis['Success_Rate_Pct'] = (payload_analysis['Success_Rate'] * 100).round(2)
payload_analysis = payload_analysis.sort_values('Success_Rate', ascending=False)
print(payload_analysis)
print(f"\n✓ HIGHEST success rate: {payload_analysis.index[0]} kg with {payload_analysis['Success_Rate_Pct'].iloc[0]}% success rate")
print(f"✓ LOWEST success rate: {payload_analysis.index[-1]} kg with {payload_analysis['Success_Rate_Pct'].iloc[-1]}% success rate")

# Question 5: Which F9 Booster version has the highest launch success rate?
print("\n\n5. Which F9 Booster version has the HIGHEST launch success rate?")
print("-" * 80)
booster_analysis = df.groupby('BoosterVersion').agg({
    'Class': ['sum', 'count', 'mean']
}).round(4)
booster_analysis.columns = ['Successful', 'Total', 'Success_Rate']
booster_analysis['Success_Rate_Pct'] = (booster_analysis['Success_Rate'] * 100).round(2)
booster_analysis = booster_analysis.sort_values('Success_Rate', ascending=False)
print(booster_analysis)
print(f"\n✓ Answer: {booster_analysis.index[0]} with {booster_analysis['Success_Rate_Pct'].iloc[0]}% success rate")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
