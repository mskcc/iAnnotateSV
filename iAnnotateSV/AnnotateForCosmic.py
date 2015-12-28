'''
Created on 12/23/2015
@Ronak Shah

'''


def ReadCosmicCensusFile (file, verbose, count, sv):
    if(verbose):
        print ("Checking Entry in Cosmic data")
    # Initialize List to store repeat annotation
    list_ccData = []
    sv_chr1 = sv.loc['Chr1']
    sv_pos1 = sv.loc['Pos1']
    sv_chr2 = sv.loc['Chr2']
    sv_pos2 = sv.loc['Pos2']
    sv_gene1 = str(sv.loc['Gene1'])
    sv_gene2 = str(sv.loc['Gene2'])
 
    with open(file, 'r') as filecontent:
        header = filecontent.readline()
        for line in filecontent:
            data = line.rstrip('\n').split('\t')
            if(str(data[0]) == sv_gene1): 
                slicedData = getVar(data,[4,7,9,12,13])
                slicedProcessedData = []
                for sData in slicedData:
                    if(sData):
                        sData = "site1:" + sData
                        slicedProcessedData.append(sData)
                    else:
                        slicedProcessedData.append(" ")
                joinedData = '\t'.join(slicedProcessedData)
                list_ccData.append(joinedData)  
            if(str(data[0]) == sv_gene2):
                slicedData = getVar(data,[4,7,9,12,13]) 
                slicedProcessedData = []
                for sData in slicedData:
                    if(sData):
                        sData = "site2:" + sData   
                        slicedProcessedData.append(sData)
                    else:
                        slicedProcessedData.append(" ")
                joinedData = '\t'.join(slicedProcessedData)
                list_ccData.append(joinedData)             
    return list_ccData