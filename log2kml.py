import argparse
import pandas as pd


parser = argparse.ArgumentParser(description='Extracts GPS data from either DashCommand or a Torque log file and creates KML path file for viewing in Google Earth')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--DashCommand', help='Specifies that the input is a DashCommand log file', action="store_true")
group.add_argument('-t', '--Torque', help='Specifies that the input is a Torque log file', action="store_true")
parser.add_argument('-i', '--input', help='Enter path to input log file: ', required=True)
parser.add_argument('-o', '--output', help='Enter name of new .kml file to write', required=True)

args = parser.parse_args()
inputf = args.input
output = args.output


if args.DashCommand:

    df = pd.read_csv(inputf, low_memory=False)
    df['AUX.GPS.LATITUDE \xc2\xb0'] = ',' + df['AUX.GPS.LATITUDE \xc2\xb0'].astype(str) + ',4'
    df['coords'] = df['AUX.GPS.LONGITUDE \xc2\xb0'] + df['AUX.GPS.LATITUDE \xc2\xb0']
    df = pd.DataFrame(df, columns=['coords'])
    df = df.drop_duplicates(take_last=True)
    df = df.convert_objects(convert_numeric=True).dropna()
    df = df.ix[1:]

    coords = df.to_string(header=False, index=False, justify='left', index_names=False)



    fname = output
    with open(fname, 'w') as fout:
        print >> fout, """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
        <Document id="feat_23">
            <Style id="stylesel_11">
                <LineStyle id="substyle_11">
                    <color>ff0000ff</color>
                    <colorMode>normal</colorMode>
                    <width>5</width>
                </LineStyle>
            </Style>
            <Placemark id="feat_24">
                <name>Path</name>
                <styleUrl>#stylesel_11</styleUrl>
                <LineString id="geom_11">
                    <coordinates>"""
    fname = output
    with open(fname, 'a') as fout:
        print >> fout, coords


    fname = output
    with open(fname, 'a') as fout:
        print >> fout, """               </coordinates>
                    <extrude>1</extrude>
                    <altitudeMode>relativeToGround</altitudeMode>
                </LineString>
            </Placemark>
        </Document>
    </kml>"""



elif args.Torque:

    df = pd.read_csv(inputf, low_memory=False)
    df[' Latitude'] = ',' + df[' Latitude'].astype(str) + ',0'
    df['coords'] = df[' Longitude'].astype(str) + df[' Latitude']
    df = pd.DataFrame(df, columns=['coords'])
    df = df.convert_objects(convert_numeric='True').dropna()
    df = df.drop_duplicates(take_last=True)


    coords = df.to_string(header=False, index=False, justify='Left', index_names=False)

    fname = output
    with open(fname, 'w') as fout:
        print >> fout, """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
        <Document id="feat_23">
            <Style id="stylesel_11">
                <LineStyle id="substyle_11">
                    <color>ff0000ff</color>
                    <colorMode>normal</colorMode>
                    <width>5</width>
                </LineStyle>
            </Style>
            <Placemark id="feat_24">
                <name>Path</name>
                <styleUrl>#stylesel_11</styleUrl>
                <LineString id="geom_11">
                    <coordinates>"""
    fname = output
    with open(fname, 'a') as fout:
        print >> fout, coords


    fname = output
    with open(fname, 'a') as fout:
        print >> fout, """               </coordinates>
                    <extrude>1</extrude>
                    <altitudeMode>relativeToGround</altitudeMode>
                </LineString>
            </Placemark>
        </Document>
    </kml>"""
