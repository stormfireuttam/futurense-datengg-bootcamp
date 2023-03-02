# Loading the data
rdd1 = sc.textFile("/home/uttam/futurense-datengg-bootcamp/dataset/bankmarketing.txt")
header = rdd1.first()
rdd2 = rdd1.filter(lambda x : x != header).filter(lambda x : len(x) > 1)
rdd3 = rdd2.map(lambda x : x.split(';'))

# Success Rate
no_subscribed = rdd3.filter(lambda x : x[16] == 'yes').count()
total_count = rdd3.count()
success_rate = (no_subscribed / total_count) * 100

# Failure Rate
failure_rate = 100 - success_rate

# Age Analysis
ages = rdd3.map(lambda x : int(x[0]))
max_age = ages.max()
min_age = ages.min()
avg_age = ages.mean()

# Balance Analysis
balances = rdd3.map(lambda x : float(x[5]))
avg_balance = balances.mean()

def findMedian(count, balances):
   if count%2 == 0:
	median = (balances[(count//2)] + balances[(count//2) + 1])//2
   else:
	median = balances[(count + 1)//2]
   return median

median = findMedian(balances.count(), balances.collect())

# Grouping by Age and displaying count of records
age_rdd = rdd3.map(lambda x :(x[0],1))
age_rdd_grouped = age_rdd.reduceByKey(lambda a,b : a + b)
age_rdd_grouped_sorted = age_rdd_grouped.sortBy(lambda x : x[1], ascending=False)

# Grouping by Marital Status and displaying count of records
marital_rdd = rdd3.map(lambda x :(x[2],1))
marital_rdd_grouped = marital_rdd.reduceByKey(lambda a,b : a + b)
marital_rdd_grouped_sorted = marital_rdd_grouped.sortBy(lambda x : x[1], ascending=False)

# Grouping by Age and Marital Status and displaying count of records
marital_age_rdd = rdd3.map(lambda x :((x[0],x[2]),1))
marital_age_rdd_grouped = marital_age_rdd.reduceByKey(lambda a,b : a + b)
marital_age_rdd_grouped_sorted = marital_age_rdd_grouped.sortBy(lambda x : x[1], ascending=False)

