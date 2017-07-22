library(BoolNet)

network <- loadNetwork("~/PycharmProjects/scrap/booleanTestNetwork.txt")

fixGenes( network, "CTNNB1", 1)



fixGenes( network, "TGFbeta", 1)






attr <- getAttractors(network, method = "chosen", startStates = list(c(1,
1,
1,
0,
1,
0,
0,
1,
0,
1,
1,
0,
1,
1,
0,
0,
0,
1,
0,
0,
1,
1,
0,
0,
0, 0, 1,
0,
0,
0, 1, 0)))

attrSeq <- getAttractorSequence(attr, 1)

if (all(attrSeq[ , 26] == 1)){
  print(0)
} else {
  print(1)
}