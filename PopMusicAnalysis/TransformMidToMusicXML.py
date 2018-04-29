from os.path import join, basename
import subprocess, glob

musescoreExePath = r"C:\Program Files (x86)\MuseScore 2\bin\MuseScore.exe"
midiFileDirectoryPath = r".\data_midi"
targetMusicXmlDirectoryPath = r".\data_musicxml"

for midiFile in glob.glob(join(midiFileDirectoryPath, "*.mid")):
    subprocess.run( \
        [musescoreExePath, \
         join(midiFileDirectoryPath, basename(midiFile)), \
         "--export-to", \
         join(targetMusicXmlDirectoryPath, basename(midiFile)[:-4]+".musicxml")])

