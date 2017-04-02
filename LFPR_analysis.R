'''
Author: Cathy (Shiyuan Dai)
'''

setwd("/Users/Cathy 1/Downloads/RA_TestData/")
library(ggplot2)
library(plotly)
data = read.csv('MarchCPS_1995_2015.csv')

############### Quick look at structure #########
summary(data)

data[which(data$wt.labforce == 16858.4),]
unique(data$year)

table(data$age)

##################### Q1  #######################

#age distribution each year 
table(data$age[which(data$year == 1995 )])
table(data$age[which(data$year == 2015)])


#age distribution for adult civilian each year

# so to answer first question, all ppl under 15 are not included, so as age above 90,
# which indicates that 15 is a proper starting point for the age range

table(data$age[which(data$year == 1995 & data$popstat == 1)])
table(data$age[which(data$year == 2015 & data$popstat == 1)])


#age distribution for NOT_IN_UNIVERSE ppl
table(data$age[which(data$labforce == 0)])


data$year = as.factor(data$year)
data$wt.popstat = as.numeric(data$popstat == 1 ) 
data$wt.popstat = data$wt.popstat * data$wtsupp

data$wt.labforce = as.numeric(data$labforce == 2 )
data$wt.labforce = data$wt.labforce * data$wtsupp

#===aggregate men and women seperately 
data.res = aggregate(cbind(wt.labforce, wt.popstat)~ year + age + sex, data=data, sum )
data.res$LFPR = data.res$wt.labforce / data.res$wt.popstat

#to get rid of all invalid LFPR, simply do:
#data.res = data.res[ !is.na(data.res$LFPR) ,]

data.res$sex_char = "Female"
data.res$sex_char[data.res$sex == 1] = "Male"

data.res$category = paste( data.res$year, data.res$sex_char)
p1 <- ggplot(data.res , aes( x= age, y = LFPR, color = category) ) + geom_line()
p1

#===calculate LFPR for whole population
data.res.all = aggregate(cbind(wt.labforce, wt.popstat)~ year + age , data=data, sum )
data.res.all$LFPR = data.res.all$wt.labforce / data.res.all$wt.popstat
p2 <- ggplot(data.res.all , aes( x= age, y = LFPR, color = year) ) + geom_line()
p2


# interactive plot

p1 <- ggplotly(p1)
p1
p2 <- ggplotly(p2)
p2


##################### Q2 #######################

data.res.econ.wide  = aggregate(cbind(wt.labforce, wt.popstat)~ year + sex, data=data, sum )
data.res.econ.wide$LFPR = data.res.econ.wide$wt.labforce / data.res.econ.wide$wt.popstat
data.res.econ.wide

data.res.all.econ.wide  = aggregate(cbind(wt.labforce, wt.popstat)~ year , data=data, sum )
data.res.all.econ.wide$LFPR = data.res.all.econ.wide$wt.labforce / data.res.all.econ.wide$wt.popstat
data.res.all.econ.wide


####################Q3#######################


data.res.all = data.res.all[ !is.na(data.res.all$LFPR) ,]
LFPR.by.age.2015 = data.res.all[ data.res.all$year == 2015 , c("age", "LFPR")]
pop.size.by.age.1995 = data.res.all[ data.res.all$year == 1995 , c("age", "wt.popstat")]

# as ages > 80 are treated differently in 1995 and 2015
# transform age tags
pop.size.by.age.1995$age[ pop.size.by.age.1995$age %in% c(81,82,83,84) ] = 80
pop.size.by.age.1995$age[ pop.size.by.age.1995$age >85 ] = 85
pop.size.by.age.1995.aggr = aggregate( wt.popstat ~ age , data = pop.size.by.age.1995, sum )

LFPR.2015.adjusted.by.1995 = sum( LFPR.by.age.2015$LFPR * pop.size.by.age.1995.aggr$wt.popstat )/ sum(pop.size.by.age.1995.aggr$wt.popstat) 
LFPR.2015.adjusted.by.1995

# compare with 
data.res.all.econ.wide[data.res.all.econ.wide$year == 2015 , "LFPR"]


