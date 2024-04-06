from youtube_transcript_api import YouTubeTranscriptApi

# Input
videoCodeId = "Z6nkEZyS9nA"
language = ["en"]

# Main Code
outputList = []

rawText = YouTubeTranscriptApi.get_transcript(videoCodeId, languages=language)
for i in rawText:
    transcript = (i['text'])
    start = (i['start'])
    duration = (i['duration'])
    transcriptLine = str(start) +" "+ transcript

    outputList.append(transcriptLine)

    with open("transcript.txt", "a") as file:
        file.write(transcript + "\n")


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
