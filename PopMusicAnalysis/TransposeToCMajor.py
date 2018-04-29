import music21, sys, glob, os

musicXmlDirectoryPath = r".\data_musicxml"
transformedCMajorXmlDirectoryPath = r".\data_cmajor"

for xmlfile in glob.glob(os.path.join(musicXmlDirectoryPath, "*.musicxml")):
    s = music21.converter.parse(xmlfile)
    k = music21.analysis.discrete.KrumhanslSchmuckler().getSolution(s)
    k1 = music21.analysis.discrete.AardenEssen().getSolution(s)
    k2 = music21.analysis.discrete.BellmanBudge().getSolution(s)
    k3 = music21.analysis.discrete.KeyWeightKeyAnalysis().getSolution(s)
    k4 = music21.analysis.discrete.KrumhanslKessler().getSolution(s)
    k5 = music21.analysis.discrete.SimpleWeights().getSolution(s)
    k6 = music21.analysis.discrete.TemperleyKostkaPayne().getSolution(s)

    if k.mode == "minor":
        k = k.relative

    c = [cInMinusOneOctave, cInSameOctave, cInPlusOneOctave] = \
    [music21.pitch.Pitch("C" + str(k.tonic.implicitOctave - 1)), \
    music21.pitch.Pitch("C" + str(k.tonic.implicitOctave)), \
    music21.pitch.Pitch("C" + str(k.tonic.implicitOctave + 1))]

    ints = [cInMinusOneInterval, cInSameInterval, cInPlusOneInterval] = \
    [music21.interval.Interval(k.tonic, c[0]), \
    music21.interval.Interval(k.tonic, c[1]), \
    music21.interval.Interval(k.tonic, c[2])]

    absMinSemitonesInterval = None
    for i in ints:
        if absMinSemitonesInterval is None or abs(i.semitones) < abs(absMinSemitonesInterval.semitones):
            absMinSemitonesInterval = i

    sNew = s.transpose(absMinSemitonesInterval)
    exporter = music21.musicxml.m21ToXml.ScoreExporter(sNew)

    from xml.etree.ElementTree import ElementTree
    ElementTree(exporter.parse()).write(os.path.join(transformedCMajorXmlDirectoryPath, os.path.basename(xmlfile)), encoding="utf-8")
    