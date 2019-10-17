rm(list = ls())

library(data.table)
library(ppls)

#Create Single Dataframe with selected variables for 2010's

setwd("~/SeniorProject/Senior Project Data/raw csvs 2")

PBPraw = list.files(pattern="*.txt")

listofData = list()

for (k in 1:length(PBPraw)){
  listofData[[k]] <- read.csv(PBPraw[k])
  colnames(listofData[[k]]) = c("gameid", "visitor", "inning", "batting team", "vis score", "home score", "pitcher", "leadoff tag" )
}
PBPdataframe <- do.call("rbind", listofData)



#Seperate Dataframe into innings/half innings

#Inning1aData <- dataframe[ which(dataframe$inning==1  
                         #& dataframe$"batting team" ==1
                         #& dataframe$"leadoff tag" == "TRUE"), ]



#Create dataframe of results -> from different source file, so needs to be merged with play by play data

setwd("~/SeniorProject/Senior Project Data/results")

resultsRaw = list.files(pattern="*.txt")

listofData = list()

for (k in 1:length(resultsRaw)){
  listofData[[k]] <- read.csv(resultsRaw[k])
  colnames(listofData[[k]]) = c("gameid", "final visitor", "final home" )
}

resultsframe <- do.call("rbind", listofData)


#merge two dataframes
merged1 = merge(PBPdataframe, resultsframe, by="gameid")



#create new variables - current difference in scores, difference in finals cores, and boolean indicating whether home team wins

merged1$curDif = (merged1$"home score" - merged1$"vis score")
  
merged1$finalDif = (merged1$"final home" - merged1$"final visitor")

merged1$homeWins = ifelse(merged1$finalDif > 0, 1, 0)


#merging player IDs
Player.IDs <- read.csv("C:/Users/Colin.000/Desktop/Senior Project Data/Player IDs.csv")
PlayerIDs = Player.IDs[,-c(4:7)]

pitcherInfo = PlayerIDs
names(pitcherInfo) = c("pitcher", "pitcherLast", "pitcherFirst")

merged2 = merge(merged1, pitcherInfo, by="pitcher")


#fixing pitcher data/create dataframe w/ pitcher data with correctly formatted nametags


setwd("~/SeniorProject/Senior Project Data/Pitcher data")

temp2 = list.files(pattern="*.csv")
temp2 = temp2[c(1:9)]

listofData2 = list()

years = c(2010,2011,2012,2013,2014,2015,2016,2017,2018)

for (k in 1:length(temp2)){
  listofData2[[k]] <- read.csv(temp2[k])
  listofData2[[k]]$year = years[k]
}

pitcherFrame <- do.call("rbind", listofData2)

length(colnames(listofData2[[8]]))



pitcherFrame$Name <- gsub(pattern="\\", replacement="&", pitcherFrame$Name, fixed = TRUE)


splitnames = tstrsplit(pitcherFrame$Name, "&")[[1]]
firsts = tstrsplit(splitnames, " ")[[1]]
lasts = tstrsplit(splitnames, " ")[[2]]

pitcherFrame$PitcherFirst = firsts
pitcherFrame$PitcherLast = lasts

pitcherFrame$PitcherLast = gsub('\\*','',pitcherFrame$PitcherLast)


#merge pitcher data, creates merged 3 - Dataset containing PBP info, score differences, pitchers and pitcher stats

merged2$pitcherTeam <- ifelse(merged2$`batting team` == '0', substr(merged2$gameid, 1,3), as.character(merged2$visitor))

merged2$pitcherTag = paste(substr(merged2$gameid, 4,7), merged2$pitcherLast, merged2$pitcherFirst, merged2$pitcherTeam)

#Changing team tags to make datasets match
pitcherFrame$Team = as.character(pitcherFrame$Tm)
pitcherFrame$Team[pitcherFrame$Team == "LAA"] <- "ANA"
pitcherFrame$Team[pitcherFrame$Team == "CHC"] <- "CHN"
pitcherFrame$Team[pitcherFrame$Team == "CHW"] <- "CHA"
pitcherFrame$Team[pitcherFrame$Team == "FLA"] <- "FLO"
pitcherFrame$Team[pitcherFrame$Team == "KCR"] <- "KCA"
pitcherFrame$Team[pitcherFrame$Team == "LAD"] <- "LAN"
pitcherFrame$Team[pitcherFrame$Team == "NYY"] <- "NYA"
pitcherFrame$Team[pitcherFrame$Team == "NYM"] <- "NYN"
pitcherFrame$Team[pitcherFrame$Team == "SDP"] <- "SDN"
pitcherFrame$Team[pitcherFrame$Team == "SFG"] <- "SFN"
pitcherFrame$Team[pitcherFrame$Team == "WSN"] <- "WAS"
pitcherFrame$Team[pitcherFrame$Team == "TBR"] <- "TBA"
pitcherFrame$Team[pitcherFrame$Team == "STL"] <- "SLN"

pitcherFrame$pitcherTag = paste(pitcherFrame$year, pitcherFrame$PitcherLast, pitcherFrame$PitcherFirst, pitcherFrame$Team)

merged3 = merge(merged2, pitcherFrame, by="pitcherTag")



#Creating dataset for half inning/inning score differences

InningDifs <- merged3[ which(merged3$"leadoff tag" == "TRUE"), ]
InningDifsSorted1 = InningDifs[order(InningDifs$gameid,InningDifs$inning),]


testFrame = InningDifsSorted1[1:100,]

for (row in 1:nrow(InningDifsSorted1)) {
  if(InningDifsSorted1[row, "inning"] > 1)
  {
    InningDifsSorted1[row,'runsThisInning'] = abs(InningDifsSorted1[row, "curDif"] - InningDifsSorted1[row - 1, "curDif"])
  }
}



#Seperating merged data (merged3) into half innings

Inning1aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==1  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning1bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==1  
                                         & InningDifsSorted1$"batting team" ==1
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning2aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==2  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning2bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==2  
                               & InningDifsSorted1$"batting team" ==1
                               & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning3aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==3  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning3bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==3  
                                         & InningDifsSorted1$"batting team" ==1
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning4aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==4  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning4bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==4  
                                         & InningDifsSorted1$"batting team" ==1
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning5aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==5  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning5bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==5  
                                         & InningDifsSorted1$"batting team" ==1
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning6aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==6  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning6bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==6  
                                         & InningDifsSorted1$"batting team" ==1
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning7aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==7  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning7bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==7  
                                         & InningDifsSorted1$"batting team" ==1
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning8aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==8  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning8bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==8  
                                         & InningDifsSorted1$"batting team" ==1
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning9aData <- InningDifsSorted1[ which(InningDifsSorted1$inning==9  
                                         & InningDifsSorted1$"batting team" ==0
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]

Inning9bData <- InningDifsSorted1[ which(InningDifsSorted1$inning==9  
                                         & InningDifsSorted1$"batting team" ==1
                                         & InningDifsSorted1$"leadoff tag" == "TRUE"), ]




#Visualizations

#Checking Inning by Inning score differences (same population?)

hist(Inning1aData$runsThisInning)

hist(Inning3aData$runsThisInning)

hist(x=Inning5aData$runsThisInning, xlab = "Runs Scored", main = "Runs Scored in Fourth Inning")

hist(Inning6aData$runsThisInning)

hist(Inning8aData$runsThisInning)

boxplot(Inning2aData$runsThisInning,Inning3aData$runsThisInning,Inning4aData$runsThisInning,Inning5aData$runsThisInning,Inning6aData$runsThisInning,Inning7aData$runsThisInning,Inning8aData$runsThisInning,Inning9aData$runsThisInning, ylab = "Runs Scored", xlab = "Inning", names = c("1","2","3","4","5","6","7","8"))


summaries = data.frame(Min = double(), FQ = double(), Median = double(), Mean = double(), TQ = double(), Max = double())
summaries[1,] = summary(Inning2aData$runsThisInning)
summaries[2,] = summary(Inning3aData$runsThisInning)
summaries[3,] = summary(Inning4aData$runsThisInning)
summaries[4,] = summary(Inning5aData$runsThisInning)
summaries[5,] = summary(Inning6aData$runsThisInning)
summaries[6,] = summary(Inning7aData$runsThisInning)
summaries[7,] = summary(Inning8aData$runsThisInning)
summaries[8,] = summary(Inning9aData$runsThisInning)

summaries[1,7] = var(Inning2aData$runsThisInning)
summaries[2,7] = var(Inning3aData$runsThisInning)
summaries[3,7] = var(Inning4aData$runsThisInning)
summaries[4,7] = var(Inning5aData$runsThisInning)
summaries[5,7] = var(Inning6aData$runsThisInning)
summaries[6,7] = var(Inning7aData$runsThisInning)
summaries[7,7] = var(Inning8aData$runsThisInning)
summaries[8,7] = var(Inning9aData$runsThisInning)

names = colnames(summaries)[1:6]
names[7] = "Variance"

colnames(summaries) = names
rownames(summaries) = c("First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eight")

#live score gap relationship with final score gap
plot(Inning2aData$curDif, Inning2aData$finalDif, main = "Second Inning Score vs Final Score", xlab = "Second Inning Home Lead", ylab = "Final Home Lead")

plot(Inning5aData$curDif, Inning5aData$finalDif, main = "Fifth Inning Score vs Final Score", xlab = "Fifth Inning Home Lead", ylab = "Final Home Lead")

plot(Inning9aData$curDif, Inning9aData$finalDif, main = "Ninth Inning Score vs Final Score", xlab = "Ninth Inning Home Lead", ylab = "Final Home Lead")


#live score gap relationship with winning
plot(Inning2aData$curDif, Inning2aData$homeWins, main = "Second Inning Score vs Winning", xlab = "Second Inning Home Lead", ylab = "Home team Wins")

plot(Inning5aData$curDif, Inning5aData$homeWins, main = "Fifth Inning Score vs Winning", xlab = "Fifth Inning Home Lead", ylab = "Home team Wins")

plot(Inning9aData$curDif, Inning9aData$homeWins, main = "Ninth Inning Score vs Winning", xlab = "Ninth Inning Home Lead", ylab = "Home team Wins")


#pitcher era relationship with final score gap
plot(Inning1aData$ERA, Inning1aData$finalDif, main = "Home Team Starting Pitcher ERA vs Final Score", xlab = "Pitcher ERA", ylab = "Final Home Lead")

plot(Inning1aData$ERA[-c(9467)] , Inning1aData$finalDif[-c(9467)] , main = "Home Team Starting Pitcher ERA vs Final Score", xlab = "Pitcher ERA", ylab = "Final Home Lead")


#correlation


#live score gap correlation with final score gap
cor(Inning2aData$curDif, Inning2aData$finalDif)

cor(Inning5aData$curDif, Inning5aData$finalDif)

cor(Inning9aData$curDif, Inning9aData$finalDif)

corVec = vector()
corVec = c(2:9)
corVec[1] = cor(Inning2aData$curDif, Inning2aData$finalDif)
corVec[2] = cor(Inning3aData$curDif, Inning3aData$finalDif)
corVec[3] = cor(Inning4aData$curDif, Inning4aData$finalDif)
corVec[4] = cor(Inning5aData$curDif, Inning5aData$finalDif)
corVec[5] = cor(Inning6aData$curDif, Inning6aData$finalDif)
corVec[6] = cor(Inning7aData$curDif, Inning7aData$finalDif)
corVec[7] = cor(Inning8aData$curDif, Inning8aData$finalDif)
corVec[8] = cor(Inning9aData$curDif, Inning9aData$finalDif)

plot(y = corVec, x = c(2:9), xlab = "Inning", ylab = "Correlation between current lead and final lead")


#live score gap correlation with winning
cor(Inning2aData$curDif, Inning2aData$homeWins)

cor(Inning5aData$curDif, Inning5aData$homeWins)

cor(Inning9aData$curDif, Inning9aData$homeWins)



#model tests for specific innings - regular linear model
head(Inning3aData)

modelinning3 = lm(Inning3aData$finalDif ~ Inning3aData$curDif + Inning3aData$ERA)
summary(modelinning3)

modelinning6 = lm(Inning6aData$finalDif ~ Inning6aData$curDif + Inning6aData$ERA)
summary(modelinning6)

modelinning2 = lm(Inning2aData$finalDif ~ Inning2aData$curDif + Inning2aData$ERA)
summary(modelinning2)

mergedDataReduced = InningDifsSorted1[,c(5,7,8,12,26,37,38,13,14)]

length(mergedDataReduced[,1])
length(complete.cases(mergedDataReduced))
write.csv(mergedDataReduced[complete.cases(mergedDataReduced)], file = "mergedDataReduced.csv", row.names = FALSE, na="")

which(complete.cases(mergedDataReduced2) == FALSE) 

mergedDataReduced2 = mergedDataReduced[-c(306200),]

write.csv(mergedDataReduced2, file = "mergedDataReduced.csv", row.names = FALSE, na="")

row.names(mergedDataReduced2) <- 1:nrow(mergedDataReduced2)

listIn = mergedDataReduced2[,5]
# 
# normalize = function(listIn)
# {
#   listIn = listIn[which(is.finite(listIn))]
#   newList = NULL
#   variance = var(listIn,na.rm=TRUE)
#   sd = sqrt(variance)
#   if (!is.na(variance)  == TRUE)
#   {
#     return(listIn)
#   }
#   meanList = mean(listIn, na.rm=TRUE)
#   for (i in 1:length(listIn))
#   {
# 
#     newList[i] = (listIn[i] - meanList) / sd
#   }
#   return(newList)
# }
# normalData = list()
# for (i in c(1:8))
# {
#   normalData[i] = normalize(mergedDataReduced2[,i])
# }
# mergedDataReduced2

mergedDataReduced4 <- mergedDataReduced2[!is.infinite(rowSums(mergedDataReduced2)),]

write.csv(mergedDataReduced4, file = "mergedDataReduced.csv", row.names = FALSE, na="")

is.finite(mergedDataReduced2)
