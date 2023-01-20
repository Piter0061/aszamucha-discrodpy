#import replicate
#f = open("music/Cypis  Jadą świry-fvKavjLyJMw.m4a", "r")
#model = replicate.models.get("openai/whisper")
#version = model.versions.get("089ea17a12d0b9fc2f81d620cc6e686de7a156007830789bf186392728ac25e8")
#output = version.predict(audio=f, model="small", transcription="plain text")
import whisper
model = whisper.load_model("base")

# We can pass in a filename or a tensor (PyTorch or numpy).
result = model.transcribe("music/Cypis  Jadą świry-fvKavjLyJMw.m4a")

# Print the transcript.
print(result["text"])