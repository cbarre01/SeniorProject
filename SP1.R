`10ATL` <- read.csv("C:/Users/Colin/Desktop/Senior Project Data/raw csvs 2010s/10ATL.txt", header=FALSE)
setwd("Users/Colin/Desktop/Senior Project Data/raw csvs 2010s")



#Create Single Dataframe with selected variables for 2010's

setwd("~/SeniorProject/Senior Project Data/raw csvs 2")

temp = list.files(pattern="*.txt")

listofData = list()

for (k in 1:length(temp)){
  listofData[[k]] <- read.csv(temp[k])
  colnames(listofData[[k]]) = c("gameid", "visitor", "inning", "batting team", "vis score", "home score", "pitcher", "leadoff tag" )
}
dataframe <- do.call("rbind", listofData)



#Seperate Dataframe into innings/half innings

Inning1aData <- dataframe[ which(dataframe$inning==1  
                         & dataframe$"batting team" ==1
                         & dataframe$"leadoff tag" == "TRUE"), ]



#Create dataframe of results

setwd("~/SeniorProject/Senior Project Data/results")

temp2 = list.files(pattern="*.txt")

listofData = list()

for (k in 1:length(temp2)){
  listofData[[k]] <- read.csv(temp2[k])
  colnames(listofData[[k]]) = c("gameid", "final visitor", "final home" )
}

resultsframe <- do.call("rbind", listofData)

test1 = merge(dataframe, resultsframe, by="gameid")