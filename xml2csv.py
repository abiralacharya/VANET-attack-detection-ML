def ns2sec(timeInNS):
    timeInNS_temp = int(timeInNS[1:-4])
    timeInSec = timeInNS_temp * pow (10,-9)
    return timeInSec

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("blackhole.flowmon")
root = tree.getroot()

#open a csv file
#output_file = open('blackholedataset.csv','a')
with open('blackholedataset.csv','a+') as fd:
    #create csv writer object
    csvwriter = csv.writer(fd)
    #headers = []
    rows = []
    count = 0
    for flow in root.findall('FlowStats/Flow'):
        for tpl in root.findall('Ipv4FlowClassifier/Flow'):
            #print(member.attrib)
            """
            if count == 0:
                headers.append('flowId')
                headers.append('sourceAddress')
                headers.append('destinationAddress')
                headers.append('sourcePort')
                headers.append('destinationPort')
                headers.append('timeFirstTxPacket')
                headers.append('timeFirstRxPacket')
                headers.append('timeLastTxPacket')
                headers.append('timeLastRxPacket')
                headers.append('delaySum')
                headers.append('jitterSum')
                headers.append('lastDelay')
                headers.append('txBytes')
                headers.append('rxBytes')
                headers.append('txPackets')
                headers.append('rxPackets')
                headers.append('lostPackets')
                csvwriter.writerow(headers)
                print(headers)
                count = count + 1
            """
            rows = []
            if flow.get('flowId') ==tpl.get('flowId'):
                rows.append(flow.get('flowId'))
                rows.append(tpl.get('sourceAddress'))
                rows.append(tpl.get('destinationAddress'))
                rows.append(tpl.get('sourcePort'))
                rows.append(tpl.get('destinationPort'))
                rows.append(ns2sec(flow.get('timeFirstTxPacket')))
                rows.append(ns2sec(flow.get('timeFirstRxPacket')))
                rows.append(ns2sec(flow.get('timeLastTxPacket')))
                rows.append(ns2sec(flow.get('timeLastRxPacket')))
                rows.append(ns2sec(flow.get('delaySum')))
                rows.append(ns2sec(flow.get('jitterSum')))
                rows.append(ns2sec(flow.get('lastDelay')))
                rows.append(flow.get('txBytes'))
                rows.append(flow.get('rxBytes'))
                rows.append(flow.get('txPackets'))
                rows.append(flow.get('rxPackets'))
                rows.append(flow.get('lostPackets'))      
                throughput = (int(flow.get('rxBytes')) * 8.0) / abs((ns2sec(flow.get('timeLastRxPacket')) - ns2sec(flow.get('timeFirstTxPacket')))) /1024/1024
                
                rows.append(throughput)
                if throughput > 0:
                    rows.append(0)
                elif throughput == 0.0:
                    rows.append(1)
                csvwriter.writerow(rows)
                #print(rows)
                

fd.close()


