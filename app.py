import PySimpleGUI as sg
import os
from google.transit import gtfs_realtime_pb2

def read_file(filepath):
    try:
        feed = gtfs_realtime_pb2.FeedMessage()

        with open(filepath, 'rb') as f:
            feed.ParseFromString(f.read())
        return feed
    except:
        return "Error reading file"

layout = [
    
          [sg.Text('Select a file to display contents')],
          [sg.Input(), sg.FileBrowse(), sg.Button('Display'), sg.Exit()],
          [sg.Text('File contents:'), sg.Button('Copy')],
          # create a new multiline element which is resizable
          [sg.Multiline(size=(92, 60), key='file_contents')],
          ]

# make below window resizable
window = sg.Window('GTFS .pb file decoder', layout, resizable=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Display':
        filepath = values[0]
        contents = read_file(filepath)
        window['file_contents'].update(contents)
    
    if event == 'Copy':
        contents = window['file_contents'].get()
        # copy contents to clipboard
        window['file_contents'].Widget.event_generate('<<Copy>>')

window.close()
